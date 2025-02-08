import * as tf from '@tensorflow/tfjs';
import * as cocossd from '@tensorflow-models/coco-ssd';

const MODEL_SETTINGS = {
  architecture: 'mobilenet_v2',
  minConfidence: 0.28,
  targetFPS: 24
};

export async function loadSecurityModel() {
  try {
    await tf.setBackend('webgl');
    await tf.ready();

    return await cocossd.load({
      base: MODEL_SETTINGS.architecture
    });
  } catch (err) {
    console.error('Model loading failed:', err);
    throw err;
  }
}