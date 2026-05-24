# Brain Stroke Risk Assessment & Multi-Architecture ANN Comparison

## Project Overview
This project targets the prediction of brain stroke clinical susceptibility using key physiological factors (e.g., age, average glucose levels, BMI, hypertension, and heart disease status). The underlying dataset presents a severe real-world class imbalance (~5% positive stroke instances), making standard predictive metrics misleading.

To address this, we designed, executed, and benchmarked **4 distinct Artificial Neural Network (ANN) topologies** using TensorFlow/Keras to analyze architectural behaviors under high-skew target environments.

---

## Evaluation Matrix Summary

| Model Architecture | F1-Score | PR-AUC | Primary Structural Trait |
| :--- | :---: | :---: | :--- |
| **1. Vanilla Tabular MLP** | 0.0377 | 0.1938 | Standard Sequential Baseline Feedforward Layers |
| **2. Regularized MLP** | 0.0392 | 0.1729 | Integrated Batch Normalization & Dropout (0.3) |
| **3. Class-Weighted MLP** | **0.2182** | 0.1760 | Loss function gradients scaled by class penalties |
| **4. Residual Tabular MLP** | 0.1127 | 0.1603 | Keras Functional API Skip-Connections (Residual Blocks) |

### Core Takeaways & Key Insights
1. **Class-Weighting Superiority:** Standard architectures (Vanilla and Regularized MLPs) failed to optimize for minority risk labels. Assigning structural sample weights based on label scarcity inside **Model 3** delivered a **~478% increase in F1-Score performance**, proving the absolute necessity of loss-scaling in medical diagnostic forecasting.
2. **Residual Signal Flow:** Incorporating functional residual skip blocks inside **Model 4** boosted F1 performance over the vanilla baseline without explicit weight parameters, confirming that shortcut routes enhance structural representation capacity for continuous features.

---

## Environment & Setup Instructions
Dependencies are detailed inside the localized `requirements.txt` file.

### Local Initialization
1. Ensure dependencies are satisfied:
   ```bash
   pip install -r requirements.txt
