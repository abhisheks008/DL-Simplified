from ultralytics import YOLO


# Load the pretrained yolo-v8-cls (classification)
model = YOLO("yolov8n-cls.pt")
result = model.train(data="./data", epochs=300, imgsz=224)
