---
title: Dental API V2
emoji: 🦷
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# Dental API V2

YOLO-based object detection API for dental image analysis.

## Endpoints

- `GET /` - Health check
- `POST /predict` - Upload image for detection

## Usage

```bash
curl -X POST https://your-space.hf.space/predict \
  -F "file=@dental_image.jpg"