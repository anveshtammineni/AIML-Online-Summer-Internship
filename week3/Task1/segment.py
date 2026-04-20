from ultralytics import YOLO
import os

model = YOLO("yolov8n-seg.pt")  # segmentation model

input_folder = "images"
output_folder = "segmented_images"

os.makedirs(output_folder, exist_ok=True)

for img in os.listdir(input_folder):
    if img.endswith(".jpg"):
        path = os.path.join(input_folder, img)
        
        results = model(path)
        
        # save segmented image
        results[0].save(filename=os.path.join(output_folder, img))

print("Done")