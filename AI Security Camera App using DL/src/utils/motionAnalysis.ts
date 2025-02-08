import * as tf from '@tensorflow/tfjs';

/**
 * MotionAnalyzer: Custom implementation for real-time motion detection
 * using temporal difference analysis and adaptive thresholding.
 */
export class MotionAnalyzer {
  private lastFrame: tf.Tensor3D | null = null;
  private readonly sensitivity = 15;
  private readonly blockSize = 16;

  async processFrame(frame: ImageData): Promise<{
    hasMotion: boolean;
    activityLevel: number;
    activeZones: number[][];
  }> {
    const currentFrame = tf.browser.fromPixels(frame);
    const processedFrame = this.preprocessFrame(currentFrame);

    if (!this.lastFrame) {
      this.lastFrame = processedFrame;
      return { hasMotion: false, activityLevel: 0, activeZones: [] };
    }

    const motionData = await this.analyzeMotion(processedFrame);
    
    tf.dispose([this.lastFrame]);
    this.lastFrame = processedFrame;

    return motionData;
  }

  private preprocessFrame(frame: tf.Tensor3D): tf.Tensor3D {
    return tf.tidy(() => {
      const normalized = tf.div(frame, 255);
      return this.applyGaussianSmoothing(normalized);
    });
  }

  private applyGaussianSmoothing(input: tf.Tensor3D): tf.Tensor3D {
    return tf.sequential({
      layers: [
        tf.layers.avgPool2d({ poolSize: [2, 2], strides: [2, 2] }),
        tf.layers.upSampling2d({ size: [2, 2] })
      ]
    }).apply(input) as tf.Tensor3D;
  }

  private async analyzeMotion(frame: tf.Tensor3D): Promise<{
    hasMotion: boolean;
    activityLevel: number;
    activeZones: number[][];
  }> {
    const frameDiff = tf.sub(frame, this.lastFrame!);
    const diffMagnitude = tf.abs(frameDiff);
    const averageChange = tf.mean(diffMagnitude).dataSync()[0];
    
    const zones = await this.identifyActiveZones(diffMagnitude);
    
    tf.dispose([frameDiff, diffMagnitude]);

    return {
      hasMotion: averageChange > this.sensitivity / 255,
      activityLevel: averageChange * 255,
      activeZones: zones
    };
  }

  private async identifyActiveZones(diff: tf.Tensor3D): Promise<number[][]> {
    const zones: number[][] = [];
    const diffData = await tf.mean(diff, -1).data();
    
    for (let y = 0; y < diff.shape[0] - this.blockSize; y += this.blockSize / 2) {
      for (let x = 0; x < diff.shape[1] - this.blockSize; x += this.blockSize / 2) {
        if (this.isActiveZone(diffData, x, y, diff.shape[1])) {
          zones.push([x, y, this.blockSize, this.blockSize]);
        }
      }
    }
    
    return this.mergeOverlappingZones(zones);
  }

  private isActiveZone(data: Float32Array, x: number, y: number, width: number): boolean {
    let sum = 0;
    for (let i = 0; i < this.blockSize; i++) {
      for (let j = 0; j < this.blockSize; j++) {
        sum += data[(y + i) * width + (x + j)];
      }
    }
    return (sum / (this.blockSize * this.blockSize)) * 255 > this.sensitivity;
  }

  private mergeOverlappingZones(zones: number[][]): number[][] {
    return zones.reduce((merged, current) => {
      const overlap = merged.find(zone => this.zonesOverlap(current, zone));
      if (!overlap) return [...merged, current];
      
      const [x1, y1, w1, h1] = overlap;
      const [x2, y2, w2, h2] = current;
      
      overlap[0] = Math.min(x1, x2);
      overlap[1] = Math.min(y1, y2);
      overlap[2] = Math.max(x1 + w1, x2 + w2) - overlap[0];
      overlap[3] = Math.max(y1 + h1, y2 + h2) - overlap[1];
      
      return merged;
    }, [zones[0]] || []);
  }

  private zonesOverlap(a: number[], b: number[]): boolean {
    return !(
      a[0] >= b[0] + b[2] ||
      a[0] + a[2] <= b[0] ||
      a[1] >= b[1] + b[3] ||
      a[1] + a[3] <= b[1]
    );
  }
}