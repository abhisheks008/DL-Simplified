#!pip install mrcnn

import mrcnn
from mrcnn import utils
from mrcnn import visualize
from mrcnn.visualize import display_images
from mrcnn import model as modellib
from mrcnn.model import log

from mrcnn.config import Config

class RoadMarkConfig(Config):
    NAME = "roadmark"
    IMAGES_PER_GPU = 1
    NUM_CLASSES = 1 + num_classes  # background + num_classes
    DETECTION_MIN_CONFIDENCE = 0.9

class RoadMarkDataset(utils.Dataset):
    def load_roadmark(self, dataset_dir, subset):
        ...
    def load_mask(self, image_id):
        ...
    def image_reference(self, image_id):
        ...

model = modellib.MaskRCNN(mode="training", config=config, model_dir=MODEL_DIR)

weights_path = model.get_imagenet_weights()
model.load_weights(weights_path, by_name=True)

model.train(dataset_train, dataset_val, learning_rate=config.LEARNING_RATE, epochs=10, layers='heads')
