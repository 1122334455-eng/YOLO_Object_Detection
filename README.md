# YOLO Based Real-Time Object Detection
A real-time object detection system built using YOLOv8, OpenCV, and Python. This project can detect multiple objects from a webcam, images, and videos with bounding boxes and confidence scores.

Features:

✅ Real-Time Webcam Object Detection

✅ Image Object Detection

✅ Video Object Detection

✅ Bounding Boxes and Confidence Scores

✅ Save Detection Results

✅ Class Name and Confidence Display

✅ Easy to Extend for Custom Datasets

Technologies:

Python 3

YOLOv8

OpenCV

PyTorch

NumPy

Matplotlib

📂 Project Structure

YOLO_Object_Detection/

│ ├── models/
│          └── yolov8n.pt

│ ├── images/
│          └── test.jpg

│ ├── videos/
│          └── test.mp4

│ ├── output/

│ 
├── detect_webcam.py

├── detect_image.py 

├── detect_video.py 

├── detection_info.py

├── save_detection.py 

├── download_model.py 

├── requirements.txt

├── README.md

└── .gitignore


⚙️ Installation
Clone Repository

git clone https://github.com/YourUsername/YOLO_Object_Detection.git

cd YOLO_Object_Detection

Create Virtual Environment

python -m venv venv

Activate Virtual Environment


Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

Install Dependencies

pip install -r requirements.txt

▶️ Download YOLO Model
python download_model.py

▶️ Run Webcam Detection
python detect_webcam.py

▶️ Run Image Detection
python detect_image.py

▶️ Run Video Detection
python detect_video.py

▶️ Save Detection Results
python save_detection.py

▶️ Display Detection Information
python detection_info.py

🎯 Detectable Objects

The pre-trained YOLOv8 model can detect 80+ object classes, including:

Person

Car

Dog

Cat

Bicycle

Bus

Truck

Mobile Phone

Laptop

Chair

Bottle

And many more...

🔮 Future Improvements
Custom Dataset Training

Helmet Detection System

Face Mask Detection System

Vehicle Detection and Counting

People Counting System

Object Tracking using DeepSORT

Smart Traffic Management System

👨‍💻 Author

Sharif Ullah

Artificial Intelligence Student

Interested in Artificial Intelligence, Computer Vision, and Deep Learning.
⭐ Support

If you found this project useful, please consider giving it a Star ⭐ on GitHub.
