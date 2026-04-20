from ultralytics import YOLO
import cv2

# Load segmentation model
model = YOLO("yolov8n-seg.pt")

# Open video
cap = cv2.VideoCapture("raw.mp4")

# Get properties
width = int(cap.get(3))
height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Output video
out = cv2.VideoWriter("segment.mp4",
                      cv2.VideoWriter_fourcc(*'mp4v'),
                      fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run segmentation
    results = model(frame)

    # Draw masks
    annotated_frame = results[0].plot()

    # Write frame
    out.write(annotated_frame)

cap.release()
out.release()
print("Segmentation video saved as segment.mp4")