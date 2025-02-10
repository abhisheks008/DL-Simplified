import * as tf from '@tensorflow/tfjs';

export class MotionDetector {
  private previousFrame: tf.Tensor3D | null = null;
  private readonly motionThreshold = 10; // Lowered from 25
  private readonly regionThreshold = 15; // Lowered from 30

  public async analyze(frame: ImageData): Promise<{ isMoving: boolean; intensity: number; regions: number[][] }> {
    // Convert frame to tensor and normalize
    const currentFrame = tf.browser.fromPixels(frame);
    const normalized = tf.div(currentFrame, 255);
    
    if (!this.previousFrame) {
      this.previousFrame = normalized;
      return { isMoving: false, intensity: 0, regions: [] };
    }

    // Calculate frame difference with Gaussian blur for noise reduction
    const blurred = tf.sequential({
      layers: [
        tf.layers.avgPool2d({ poolSize: [2, 2], strides: [2, 2] }),
        tf.layers.upSampling2d({ size: [2, 2] })
      ]
    }).apply(normalized) as tf.Tensor3D;

    const diff = tf.sub(blurred, this.previousFrame);
    const absDiff = tf.abs(diff);
    const meanDiff = tf.mean(absDiff).dataSync()[0];
    
    // Detect motion regions
    const regions = await this.findMotionRegions(absDiff, frame.width, frame.height);
    
    // Update previous frame with current blurred frame
    tf.dispose([this.previousFrame, diff, absDiff, normalized]);
    this.previousFrame = blurred;

    const intensity = meanDiff * 100;
    const isMoving = intensity > this.motionThreshold;

    return {
      isMoving,
      intensity,
      regions
    };
  }

  private async findMotionRegions(diff: tf.Tensor3D, width: number, height: number): Promise<number[][]> {
    const regions: number[][] = [];
    const blockSize = 16; // Reduced from 32 for finer detection
    
    // Convert to grayscale and get data
    const grayDiff = tf.mean(diff, -1);
    const diffData = await grayDiff.data();
    
    // Scan image in blocks with overlap
    for (let y = 0; y < height - blockSize; y += blockSize/2) {
      for (let x = 0; x < width - blockSize; x += blockSize/2) {
        let blockSum = 0;
        
        // Calculate average difference in block
        for (let by = 0; by < blockSize; by++) {
          for (let bx = 0; bx < blockSize; bx++) {
            const idx = (y + by) * width + (x + bx);
            blockSum += diffData[idx];
          }
        }
        
        const blockAvg = blockSum / (blockSize * blockSize);
        
        // If block has significant motion, add to regions
        if (blockAvg * 255 > this.regionThreshold) {
          regions.push([x, y, blockSize, blockSize]);
        }
      }
    }
    
    tf.dispose(grayDiff);
    return this.mergeRegions(regions);
  }

  private mergeRegions(regions: number[][]): number[][] {
    if (regions.length === 0) return [];
    
    return regions.reduce((merged, current) => {
      const overlapping = merged.find(region => this.overlaps(current, region));
      
      if (!overlapping) {
        return [...merged, current];
      }
      
      // Merge overlapping regions
      const minX = Math.min(overlapping[0], current[0]);
      const minY = Math.min(overlapping[1], current[1]);
      const maxX = Math.max(overlapping[0] + overlapping[2], current[0] + current[2]);
      const maxY = Math.max(overlapping[1] + overlapping[3], current[1] + current[3]);
      
      overlapping[0] = minX;
      overlapping[1] = minY;
      overlapping[2] = maxX - minX;
      overlapping[3] = maxY - minY;
      
      return merged;
    }, [regions[0]]);
  }

  private overlaps(r1: number[], r2: number[]): boolean {
    return !(
      r1[0] > r2[0] + r2[2] || // r1 is right of r2
      r1[0] + r1[2] < r2[0] || // r1 is left of r2
      r1[1] > r2[1] + r2[3] || // r1 is below r2
      r1[1] + r1[3] < r2[1]    // r1 is above r2
    );
  }
}