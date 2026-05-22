# 🩸 Blood Disease Detection Using CNN

### 🎯 Goal
The main goal of this project is to develop a robust Convolutional Neural Network (CNN) capable of automating the classification of different cell types from microscopic blood smear images. This assists medical professionals by speeding up screening processes for various blood disorders.

### 🧵 Dataset
The project utilizes the public **Blood Cells Dataset** available on Kaggle. You can access it directly via the link below:
👉 [Kaggle Blood Cells Dataset](https://www.kaggle.com/datasets/paultimothymooney/blood-cells)

### 🧾 Description
This dataset contains a total of 12,500 augmented microscopic blood cell images (320x240 RGB pixels in JPEG format) along with accompanying cell type labels. The data features approximately 3,000 sample images for each of the 4 main blood cell types: **Eosinophil, Lymphocyte, Monocyte, and Neutrophil**.

The directory structure contains two primary collections:
* `dataset-master`: Contains the original, unaugmented 410 images of the different cell types.
* `dataset2-master`: Contains 3,000 heavily augmented images per cell type, cleanly partitioned into distinct subfolders for training, testing, and validation processing.

### 🧮 What I had done!
1. **Input Data Pipeline:** Created an efficient image loading setup utilizing the `tf.keras.utils.image_dataset_from_directory` utility to streamline training, validation, and testing divisions directly from the local folder ecosystem.
2. **Data Rescaling:** Integrated a preprocessing layer to normalize pixel intensity matrices uniformly.
3. **Model Construction:** Formed a sequential CNN architecture consisting of 4 distinct 2D Convolutional and Max Pooling layer pairings, followed by dense processing nodes.
4. **Regularization Setup:** Introduced a Dropout layer set to 10% between the dense connections to mitigate risk of model overfitting.
5. **Optimization Testing:** Experimented comprehensively with 5 separate training optimizers (`Adadelta`, `Adagrad`, `Adam`, `RMSprop`, and `SGD`) using `SparseCategoricalCrossentropy` loss to identify the absolute best compilation configuration.

### 🚀 Models Implemented
A custom Deep **Convolutional Neural Network (CNN)** was designed and implemented for this task. 

**Why this architecture was chosen:**
CNNs are the gold standard for image processing because their localized convolutional filters automatically extract spatial features—such as cellular wall boundaries, color concentrations, and nuclear structures—without requiring manual feature engineering. 

#### Model Layers Architecture Summary:
![MODEL SUMMARY](../Images/model_summary.png)

* `Rescaling Layer` (Input Shape: 320 x 240 x 3)
* `Conv2D` (32 filters, 3x3 kernel) + `MaxPooling2D`
* `Conv2D` (64 filters, 3x3 kernel) + `MaxPooling2D`
* `Conv2D` (64 filters, 3x3 kernel) + `MaxPooling2D`
* `Conv2D` (32 filters, 3x3 kernel) + `MaxPooling2D`
* `Flatten Layer`
* `Dense Layer` (Hidden nodes with ReLU activation)
* `Dropout Layer` (10% rate parameter)
* `Dense Layer` (Output layer utilizing Softmax)

### 📚 Libraries Needed
* `matplotlib == 3.5.1`
* `numpy == 1.22.3`
* `Pillow == 9.2.0`
* `protobuf == 4.21.5`
* `tensorboard == 2.9.1`
* `tensorflow == 2.9.1`

### 📊 Exploratory Data Analysis Results
Below are the sample microscopic blood cell visualizations reflecting the four distinct cell class targets present within the dataset pipeline:

<p align="center">
  <img src="../Images/cell_types.png" alt="Microscopic Blood Cell Types Sample Grid" width="85%"/>
</p>

### 📈 Performance of the Models based on the Accuracy Scores
The network model layout was systematically compiled and evaluated across five distinct optimization variations to monitor performance differences.

#### Individual Optimizer Learning Slopes:
| OPTIMIZER | LOSS FUNCTION | ACTIVATION FUNCTION | ____ ACCURACY ____ | _______ LOSS _______ |
| :---: | :---: | :---: | :---: | :---: |
| **adadelta** | sparse categorical crossentropy | relu | ![ACCURACY](../Images/adadelta_scc_relu_accuracy.svg) | ![LOSS](../Images/adadelta_scc_relu_loss.svg) |
| **adagrad** | sparse categorical crossentropy | relu | ![ACCURACY](../Images/adagrad_scc_relu_accuracy.svg) | ![LOSS](../Images/adagrad_scc_relu_loss.svg) |
| **adam** | sparse categorical crossentropy | relu | ![ACCURACY](../Images/adam_scc_relu_accuracy.svg) | ![LOSS](../Images/adam_scc_relu_loss.svg) |
| **rmsprop** | sparse categorical crossentropy | relu | ![ACCURACY](../Images/rmsprop_scc_relu_accuracy.svg) | ![LOSS](../Images/rmsprop_scc_relu_loss.svg) |
| **sgd** | sparse categorical crossentropy | relu | ![ACCURACY](../Images/sgd_scc_relu_accuracy.svg) | ![LOSS](../Images/sgd_scc_relu_loss.svg) |

#### Overall Combined Performance Metrics:
| ___________ ACCURACY ___________ | ______________ LOSS ______________ |
| :---: | :---: |
| ![COMBINED ACCURACY](../Images/all_combined_accuracy.svg) | ![COMBINED LOSS](../Images/all_combined_loss.svg) |

> 🌐 **Interactive Analysis View:** You can inspect the live compilation training charts directly on [TensorBoard Tracker](https://tensorboard.dev/experiment/tw0dn4WIQYa6upR0v1oXug/).

#### Core Metric Performance Analysis:
From the comparative data logs compiled above, the network achieved its fastest convergence rates and highest validation metrics when pairing training with the **RMSprop (Root Mean Squared Propagation)** optimizer configuration. One thing to take note of is that RMSprop may not always show this kind of performance on every model layout; it varies based on dataset density and initialization weights.

### 📢 Conclusion
Based on the optimization metrics observed, selecting the correct algorithm significantly impacts training convergence velocities. While standard algorithms like `SGD` converge slowly and require a much larger number of training epochs to hit absolute minimum loss thresholds, `RMSprop` dynamically adapts learning paces to navigate deep medical feature sets efficiently. 

The resulting framework establishes a reliable foundation for automated classification pipelines. Future iterations can scale this architecture into lightweight edge platforms for rapid, remote clinical evaluations.

---

### ✒️ Your Signature

**Original Project Contributor:**
* **Name:** Uttkarsh Patel
* **LinkedIn:** [Uttkarsh Patel Profile](https://www.linkedin.com/in/uttkarsh-patel-62b011218/)
* **GitHub:** [@Uttkarsh09](https://github.com/Uttkarsh09)

**Documentation Enhanced By:**
* **Name:** Dharani Ponnala
* **GitHub Profile:** https://github.com/dharaniiii1208
* **LinkedIn Profile:** https://www.linkedin.com/in/dharani-ponnala/
* **GSSoC '26 Contributor**
