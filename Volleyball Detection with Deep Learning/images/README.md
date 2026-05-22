# 🏐 Volleyball Tracking & Object Detection Benchmark

## 🎯 Project Goal
The primary objective of this project is to build, train, and benchmark multiple object detection architectures to determine the optimal algorithm for tracking a fast-moving, small object (a volleyball) in video footage. The project compares single-stage and two-stage detectors, evaluating them on a strict matrix of **Accuracy (mAP)** and **Inference Speed (FPS)** to find the best fit for real-world sports analytics.

## 💾 Dataset
* **Source:** [\[Insert link to Kaggle/Roboflow/Drive dataset here\]](https://www.kaggle.com/datasets/pythonistasamurai/volleyball-ball-object-detection-dataset)
* **Format:** The dataset was originally annotated in YOLO format (normalized `x_center, y_center, width, height`).
* **Processing:** For the PyTorch-native models, a custom PyTorch `Dataset` class was engineered to dynamically parse YOLO `.txt` files and convert them into Pascal VOC absolute coordinates (`xmin, ymin, xmax, ymax`) on the fly during the training loop.

## 🧠 Models Evaluated
1. **YOLOv8 (Nano & Medium):** State-of-the-art single-stage detector.
2. **Faster R-CNN (ResNet50 FPN):** Heavyweight, highly accurate two-stage detector.
3. **SSD300 (VGG16):** Single Shot MultiBox Detector bridging the gap between speed and architectural complexity.
4. **RetinaNet (ResNet50 FPN):** Single-stage detector utilizing **Focal Loss** to handle extreme foreground-background class imbalance (critical for finding a small ball on a large court).

## 🛠️ Libraries & Tech Stack
* **Deep Learning:** `PyTorch`, `Torchvision`, `Ultralytics`
* **Computer Vision:** `OpenCV (cv2)`
* **Metrics & Math:** `Torchmetrics`, `NumPy`
* **Visualization:** `Matplotlib`
* **Environment:** Google Colab (T4 GPU for Training), VS Code (Local Inference)

## 🚀 Methodology & Approach
1. **Baseline Establishment:** Trained YOLOv8 Nano to establish a fast but easily confused baseline. Scaled up to YOLOv8 Medium to solve motion blur and tracking inconsistencies.
2. **Custom Data Pipeline:** Engineered a PyTorch DataLoader to bridge YOLO text annotations into tensor dictionaries required by `torchvision` models.
3. **Model Head Modification:** Loaded pre-trained backbones (ResNet50/VGG16) and manually modified the prediction heads to output exactly 2 classes: `Background (0)` and `Volleyball (1)`.
4. **Training Stability:** Implemented **Gradient Clipping** (`max_norm=1.0`) and reduced learning rates (`0.0005`) to prevent exploding gradients (`NaN` loss) during the highly volatile early epochs of SSD and RetinaNet training.
5. **Evaluation Engine:** Wrote a custom local Python script (`benchmark.py`) using OpenCV to run exactly 100 frames of a test video through all four architectures back-to-back to calculate true inference speed (FPS). Utilized `torchmetrics` to calculate Mean Average Precision (mAP) for the PyTorch models.

## 📊 Results: Accuracy & Speed Benchmark

| Algorithm | Architecture Type | Final Validation Loss | Accuracy (mAP@50) | Speed (Inference FPS) |
| :--- | :--- | :--- | :--- | :--- |
| **YOLOv8 Medium** | Single-Stage | [Insert Loss] | **[Insert YOLO mAP]%** | **4.68 FPS** |
| **SSD300** | Single-Stage | 1.6742 | **41.12%** | **2.86 FPS** |
| **RetinaNet** | Single-Stage (Focal Loss) | 0.2662 | **92.63%** | **0.51 FPS** |
| **Faster R-CNN** | Two-Stage | 0.0070 | **96.04%** | **0.16 FPS** |

*(Note: FPS benchmarks were conducted on CPU using OpenCV.)*

## 🔍 Key Observations
* **YOLOv8:** Smaller models (like YOLOv8 Nano) aggressively lost tracking confidence when the ball moved rapidly due to motion blur. Scaling the parameters up (Medium/ResNet50) allowed the models to recognize the shape of a blurred object.
* **SSD:** SSD proved highly unstable in early training epochs compared to Faster R-CNN. Implementing gradient clipping was mandatory to prevent the loss from hitting infinity (`NaN`).
* **RetinaNet:** Because a volleyball takes up <1% of the pixels in an image, standard models spend too much time learning the background. RetinaNet's focal loss mathematically forced the network to focus on the "hard" examples (the ball), making it highly efficient at small object detection.
* **Faster R-CNN:** Faster R-CNN provided highly accurate and tight bounding boxes, but its Region Proposal Network makes it far too slow for real-time video processing compared to single-stage architectures.

## 🏆 Conclusion
For real-time sports analytics, **YOLOv8 Medium** proved to be the best-fitted algorithm for this model. It successfully tracked the ball through motion blur and net occlusion while maintaining a high enough FPS to process live video. While architectures like Faster R-CNN and RetinaNet offer incredible accuracy and robust theoretical approaches (like Focal Loss), their heavier computational load makes them better suited for static image analysis rather than high-speed video tracking.

**Ashwast**
* **LinkedIn:** //https://www.linkedin.com/in/ashwast-gupta/
* **GitHub:** https://github.com/ash-heinz