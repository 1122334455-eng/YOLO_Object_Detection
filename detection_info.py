from ultralytics import YOLO

model = YOLO("models/yolov8n.pt")

results = model("images/test.jpg")

for result in results:

    boxes = result.boxes

    for box in boxes:

        cls = int(box.cls[0])
        conf = float(box.conf[0])

        print(
            "Class:",
            model.names[cls],
            "| Confidence:",
            round(conf, 2)
        )