# Models — Animal Detection using Advanced DL Models

## Overview

This project implements **5 deep learning models** for animal detection and classification on the Animals-10 dataset. It includes 1 object detection model (YOLOv8n) and 4 image classification models compared side-by-side.

---

## Models Used

### 1. YOLOv8n — Object Detection
| Property | Value |
|---|---|
| **Architecture** | CSPDarknet + PANet + Detect Head |
| **Pretrained On** | COCO (80 classes) |
| **Parameters** | 3.2M |
| **mAP@0.5** | 37.3% (COCO benchmark) |
| **Task** | Multi-object detection with bounding boxes |
| **Strength** | Real-time detection, multiple animals per frame |

### 2. InceptionV3 — Classification
| Property | Value |
|---|---|
| **Architecture** | Inception modules with factorized convolutions |
| **Layers** | 48 |
| **Parameters** | 23.9M |
| **Pretrained On** | ImageNet |
| **Strength** | Best accuracy-efficiency tradeoff |

### 3. ResNet50 — Classification
| Property | Value |
|---|---|
| **Architecture** | Residual learning with skip connections |
| **Layers** | 50 |
| **Parameters** | 25.6M |
| **Pretrained On** | ImageNet |
| **Strength** | Solves vanishing gradient, robust general-purpose CNN |

### 4. MobileNetV2 — Classification
| Property | Value |
|---|---|
| **Architecture** | Inverted residuals + depthwise separable convolutions |
| **Layers** | 53 |
| **Parameters** | 3.4M |
| **Pretrained On** | ImageNet |
| **Strength** | Fastest inference — ideal for edge/mobile/IoT |

### 5. VGG16 — Classification
| Property | Value |
|---|---|
| **Architecture** | Sequential 3×3 convolutions |
| **Layers** | 16 |
| **Parameters** | 138.4M |
| **Pretrained On** | ImageNet |
| **Strength** | Simple architecture, strong baseline |

---

## Model Performance Comparison

| Model | Task | Accuracy / mAP | Inference (ms/img) | Params (M) |
|---|---|---|---|---|
| YOLOv8n | Detection | mAP@0.5: 37.3% | ~12 ms | 3.2 |
| InceptionV3 | Classification | ~88–92% | ~18 ms | 23.9 |
| ResNet50 | Classification | ~85–89% | ~22 ms | 25.6 |
| MobileNetV2 | Classification | ~83–87% | ~9 ms | 3.4 |
| VGG16 | Classification | ~81–85% | ~35 ms | 138.4 |

> Results vary based on dataset split, epochs, and hardware.

---

## Transfer Learning Strategy

All classification models use the same transfer learning approach:
1. **Freeze** pretrained base layers (ImageNet weights)
2. Add custom **classification head**: GAP → BN → Dense(512) → Dropout(0.4) → Dense(256) → Dropout(0.3) → Softmax(10)
3. Train with **Adam optimizer** (lr=0.0001)
4. **EarlyStopping** + **ReduceLROnPlateau** callbacks

---

## How to Run

### Kaggle (Recommended — dataset pre-attached)
1. Open `animal_detection_using_DL.ipynb` in Kaggle
2. Attach dataset: `alessiocorrado99/animals10`
3. Enable GPU (P100)
4. Run All

### Google Colab
1. Upload notebook
2. Enable T4 GPU
3. Run Section 3 Kaggle download block
4. Run All

---

## Requirements

See `requirements.txt` in the root folder.