import cv2
from ultralytics import YOLO

model = YOLO("models/yolov8n.pt")

image = cv2.imread("images/test.jpg")

results = model(image)

annotated = results[0].plot()

cv2.imwrite("output/result.jpg", annotated)

print("Result Saved Successfully")