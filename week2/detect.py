from ultralytics import YOLO

# Load pretrained model
model = YOLO("yolov8n.pt")

# Run detection on an image
results = model("zidane.jpg", show=True)

# Save results
results[0].save()