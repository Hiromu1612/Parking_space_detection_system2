import os
os.chdir(r"C:/Users/1612h/Parking-space-detection/Mask_RCNN/")

import numpy as np
import cv2
import mrcnn.config
import mrcnn.utils
from collections.abc import Iterable
from mrcnn.model import MaskRCNN
from pathlib import Path
# from google.colab.patches import cv2_imshow
import pickle

from shapely.geometry import box
from shapely.geometry import Polygon as shapely_poly
from IPython.display import clear_output, Image, display, HTML
import io
import base64
#%matplotlib inline


class Config(mrcnn.config.Config):
    NAME = "coco_pretrained_model_config"
    IMAGES_PER_GPU = 1
    GPU_COUNT = 1
    NUM_CLASSES = 81

config = Config()
config.display()


ROOT_DIR = Path(".")
MODEL_DIR = os.path.join(ROOT_DIR, "logs")
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")


if not os.path.exists(COCO_MODEL_PATH):
    mrcnn.utils.download_trained_weights(COCO_MODEL_PATH)


model = MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=Config())