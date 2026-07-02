import cv2
from ultralytics import YOLO

model = YOLO("models/yolov8n.pt")

image_path = "images/test.jpg"

results = model(image_path)

annotated = results[0].plot()

cv2.imshow("Image Detection", annotated)

cv2.waitKey(0)
cv2.destroyAllWindows()