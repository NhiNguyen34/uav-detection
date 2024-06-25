import os

import torch
from ultralytics import YOLO

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

class Yolov8:
    def __init__(self, weight):
        self.model_yolo = YOLO(weight)

    def load_model(self):
        return self.model_yolo.to(DEVICE)
    
    def info_model(self):
        return self.model_yolo.info()
    
    def detect(self, image_path):
        results = self.model_yolo.predict(image_path)
        return results
    
