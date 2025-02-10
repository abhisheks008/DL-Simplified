/**
 * Custom Security Monitoring System
 * 
 * Features:
 * - Multi-source data integration
 * - Real-time threat detection
 * - Motion analysis
 * - Privacy-preserving processing
 */

import * as tf from '@tensorflow/tfjs';
import { MotionAnalyzer } from './motionAnalysis';

interface SecurityDetection {
  bbox: number[];
  class: string;
  confidence: number;
  timestamp: number;
}

export class SecurityMonitor {
  private model: tf.GraphModel | null = null;
  private motionAnalyzer: MotionAnalyzer;
  private readonly modelPath = 'path/to/custom/model';
  private readonly confidenceThreshold = 0.35;

  constructor() {
    this.motionAnalyzer = new MotionAnalyzer();
  }

  async initialize(): Promise<void> {
    try {
      await tf.setBackend('webgl');
      await tf.ready();
      this.model = await tf.loadGraphModel(this.modelPath);
    } catch (error) {
      console.error('Security system initialization failed:', error);
      throw new Error('System initialization failed');
    }
  }

  async analyzeFrame(frame: ImageData): Promise<SecurityDetection[]> {
    if (!this.model) throw new Error('System not initialized');

    const tensor = this.preprocessFrame(frame);
    const motionData = await this.motionAnalyzer.processFrame(frame);
    const detections = await this.detectObjects(tensor);

    return this.combineResults(detections, motionData);
  }

  private preprocessFrame(frame: ImageData): tf.Tensor4D {
    return tf.tidy(() => {
      const tensor = tf.browser.fromPixels(frame);
      const normalized = tf.div(tensor, 255);
      return tf.expandDims(normalized, 0);
    });
  }

  private async detectObjects(input: tf.Tensor4D): Promise<SecurityDetection[]> {
    const predictions = await this.model!.execute(input) as tf.Tensor[];
    return this.processDetections(predictions);
  }

  private processDetections(predictions: tf.Tensor[]): SecurityDetection[] {
    const [boxes, scores, classes] = predictions;
    const detections: SecurityDetection[] = [];

    const boxesData = boxes.dataSync();
    const scoresData = scores.dataSync();
    const classesData = classes.dataSync();

    for (let i = 0; i < scores.size; i++) {
      if (scoresData[i] < this.confidenceThreshold) continue;

      detections.push({
        bbox: this.extractBoundingBox(boxesData, i),
        class: this.getClassName(classesData[i]),
        confidence: scoresData[i],
        timestamp: Date.now()
      });
    }

    tf.dispose(predictions);
    return detections;
  }

  private extractBoundingBox(boxes: Float32Array, index: number): number[] {
    return [
      boxes[index * 4],
      boxes[index * 4 + 1],
      boxes[index * 4 + 2],
      boxes[index * 4 + 3]
    ];
  }

  private getClassName(classId: number): string {
    const classes = [
      'person',
      'suspicious_object',
      'weapon',
      'vehicle',
      'bag',
      'restricted_area'
    ];
    return classes[classId] || 'unknown';
  }

  private combineResults(
    detections: SecurityDetection[],
    motionData: any
  ): SecurityDetection[] {
    return detections.map(detection => ({
      ...detection,
      confidence: this.adjustConfidence(
        detection.confidence,
        motionData.activityLevel
      )
    }));
  }

  private adjustConfidence(
    baseConfidence: number,
    motionLevel: number
  ): number {
    const motionFactor = 0.2;
    return Math.min(
      baseConfidence * (1 + motionLevel * motionFactor),
      1.0
    );
  }
}