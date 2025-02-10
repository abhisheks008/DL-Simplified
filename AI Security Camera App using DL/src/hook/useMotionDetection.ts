import { useState, useCallback, useRef } from 'react';
import * as tf from '@tensorflow/tfjs';
import { MotionDetector } from '../utils/motionDetection';

export function useMotionDetection() {
  const [motionRegions, setMotionRegions] = useState<number[][]>([]);
  const detector = useRef(new MotionDetector());
  const frameBuffer = useRef<tf.Tensor3D[]>([]);
  const BUFFER_SIZE = 5;

  const detectMotion = useCallback(async (imageData: ImageData) => {
    // Convert frame to tensor
    const frame = tf.browser.fromPixels(imageData);
    
    // Add to buffer
    frameBuffer.current.push(frame);
    if (frameBuffer.current.length > BUFFER_SIZE) {
      tf.dispose(frameBuffer.current.shift());
    }
    
    // Analyze motion
    const result = await detector.current.analyze(imageData);
    
    // Update regions only if significant motion detected
    if (result.intensity > 15) {
      setMotionRegions(result.regions);
    }
    
    return {
      isMoving: result.intensity > 10,
      intensity: result.intensity
    };
  }, []);

  return { detectMotion, motionRegions };
}