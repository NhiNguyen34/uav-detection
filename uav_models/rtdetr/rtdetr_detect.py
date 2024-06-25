import os

import torch
from ultralytics import RTDETR


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

class ModelRTDETR:
    def __init__(self, weight):
        self.model_rtdetr = RTDETR(weight)

    def load_model(self):
        return self.model_rtdetr.to(DEVICE)
    
    def info_model(self):
        return self.model_rtdetr.info()
    
    def detect(self, image_path):
        results = self.model_rtdetr(image_path)
        return results
    


    