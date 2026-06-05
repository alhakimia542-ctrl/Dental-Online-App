from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO
import io
from PIL import Image

app = FastAPI()

# Load model weights from current directory
model = YOLO("best.pt")

@app.get("/")
def home():
    return {"status": "Dental Cloud API is fully operational!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read and preprocess image
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        
        # Run inference
        results = model(image)
        
        # Parse detections
        detections = []
        for result in results:
            if result.boxes is not None:
                boxes = result.boxes
                for box in boxes:
                    # Get normalized coordinates
                    x1, y1, x2, y2 = box.xyxyn[0].tolist()
                    w = x2 - x1
                    h = y2 - y1
                    
                    # Get label and confidence
                    label = result.names[int(box.cls[0])]
                    confidence = float(box.conf[0])
                    
                    detections.append({
                        "x": x1,
                        "y": y1,
                        "w": w,
                        "h": h,
                        "label": label,
                        "confidence": confidence
                    })
                
        return JSONResponse(content={"detections": detections})
        
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)