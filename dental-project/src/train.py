import argparse
import os
from ultralytics import YOLO

def train_model(data_yaml, epochs, imgsz, batch, model_name):
    if not os.path.exists(data_yaml):
        print(f"Error: {data_yaml} not found")
        return
    
    model = YOLO('yolov8s.pt')
    model.train(data=data_yaml, epochs=epochs, imgsz=imgsz, batch=batch, name=model_name)
    print(f"Training completed. Model saved to runs/detect/{model_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, required=True, help='path to data.yaml')
    parser.add_argument('--epochs', type=int, default=50)
    parser.add_argument('--imgsz', type=int, default=640)
    parser.add_argument('--batch', type=int, default=16)
    parser.add_argument('--name', type=str, default='dental_model')
    args = parser.parse_args()
    
    train_model(args.data, args.epochs, args.imgsz, args.batch, args.name)