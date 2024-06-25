import argparse
import cv2
import torch

from uav_models import Yolov8, ModelRTDETR


def main(args):
    
    if args.model_detect == 'yolov8':
        model = Yolov8(args.model_path)
    #elif args.model_detect == 'yolov10':
    #    model = UAVModel(args.moodel_path)
    elif args.model_detect == 'rt-detr':
        model = ModelRTDETR(args.model_path)
    else:
        print(f"Error: Unsupported model type {args.model_path}")
        return
    
    model.load_model()
    model.info_model()
    
    image = cv2.imread(args.image_path)
    if image is None:
        print(f"Error: Unsupported image path {args.image_path}")
        return
    
    predictions = model.detect(image)
    print(predictions[0])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detection on Image.")
    parser.add_argument("--model_path", type=str, required=True)
    parser.add_argument("--image_path", type=str, required=True)
    parser.add_argument("--model_detect", type=str, required=True)

    args = parser.parse_args()
    main(args)


