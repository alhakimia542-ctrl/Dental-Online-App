import argparse
import cv2
from ultralytics import YOLO

def predict(model_path, image_path, conf=0.4):
    model = YOLO(model_path)
    results = model.predict(image_path, conf=conf)
    return results[0].plot()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, required=True, help='path to best.pt')
    parser.add_argument('--image', type=str, required=True, help='path to input image')
    parser.add_argument('--conf', type=float, default=0.4)
    args = parser.parse_args()
    
    result = predict(args.model, args.image, args.conf)
    cv2.imshow('Result', result)
    cv2.waitKey(0)