# Web App Dashboard for Online Shoppers Intention Prediction

## Interactive Dashboard
This dashboard is designed as an analytics workspace for visualizing model performance and purchase intention insights from online shopping session data. It is built for analysis and demonstration rather than full production deployment.

## Model Comparison Dashboard
The dashboard displays side-by-side model metrics and highlights the best performing architecture for purchase intent prediction.

## Performance Visualization Dashboard
The dashboard provides key performance charts, ROC-AUC comparisons, and prediction insights that help review model effectiveness clearly.

## Dashboard Features
- Interactive performance overview of all trained models
- Comparison of accuracy, precision, recall, F1-score, and ROC-AUC
- Visualization of prediction distributions and confusion matrices
- Session-level purchase intent analytics and model calibration insights
- Summary of the best performing model and recommended decision thresholds

## Dashboard Workflow
1. Open `dashboard.html` inside the `Web App` folder.
2. Review the model comparison section to understand each architecture's performance.
3. Use the visual panels to compare training history, class balance, and predictive behavior.
4. Check the prediction insights section for how purchase intent is estimated against session features.

## How to Interpret the Results
- **Model Comparison**: Review the metrics table and choose the model with the best balance between precision and recall for your business objective.
- **Confusion Matrix**: Understand false positives and false negatives for each model. This helps determine the risk of misclassifying purchase intent.
- **ROC Curve**: Use the ROC-AUC visualization to compare discrimination power across models.
- **Feature Importance**: Identify which session behavior features are most predictive of purchase decisions.

## Included Files
- `dashboard.html` — Analytics dashboard page
- `demo.mp4` — Demo video of the dashboard workflow
- `ui_home.png` — Home screen visualization placeholder
- `ui_prediction.png` — Prediction details screen placeholder
- `ui_results.png` — Model results screen placeholder

## Notes for Reviewers
- The dashboard is intended as a demonstration layer for analysis and model interpretation.
- Visual assets are documented as placeholders so review and QA can validate the planned UX.
- The project is structured to support a clean separation between data, models, images, and web presentation.
