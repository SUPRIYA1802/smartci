# Assignment 4_5 – Build-Failure Prediction

## 1. Introduction
Build-Failure Prediction is a machine learning task that predicts whether a software build is likely to fail using historical build information.

## 2. Objective
The objective is to identify potentially risky software builds before execution using machine learning.

## 3. Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest Classifier
- Joblib
- VS Code
- Git and GitHub

## 4. Dataset Generation
A synthetic dataset containing 300 build records was generated using Python.

The dataset was saved as ml/builds.csv.

## 5. Features Used
- files_changed
- lines_changed
- hour
- failed (target variable)

## 6. Model Training
A Random Forest Classifier was trained using the generated dataset.

The dataset was divided into training and testing sets using an 80:20 split.

## 7. Model Evaluation
The model was evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Actual evaluation results:
[Insert your program results here.]

## 8. Feature Importance
The model identifies which input features contribute most to its predictions.

Actual feature importance:
[Insert your program results here.]

## 9. Risky Build Prediction
A large, late-night commit was tested using:
- Files changed: 12
- Lines changed: 450
- Commit hour: 22

Actual failure probability:
[Insert your program result here.]

## 10. Small and Well-Tested Build Prediction
A small commit was tested using:
- Files changed: 2
- Lines changed: 15
- Commit hour: 10

Actual failure probability:
[Insert your program result here.]

## 11. Comparison
The predictions of the risky build and the small build were compared to understand how build characteristics affect estimated failure risk.

## 12. Class Imbalance
Class imbalance occurs when the number of successful builds differs from the number of failed builds.

Precision, recall and F1-score help evaluate the model beyond accuracy. Class weighting was used in the Random Forest model.

## 13. Practical Use of Failure Prediction
High-risk builds can be sent for additional testing, code review and developer verification before merging.

## 14. Learnings
- Learned to generate a machine learning dataset.
- Learned feature selection and target separation.
- Learned training and testing data separation.
- Learned Random Forest classification.
- Learned model evaluation.
- Learned feature importance.
- Learned to estimate build-failure probabilities.
- Learned to use GitHub for project management.

## 15. Conclusion
The assignment demonstrates how machine learning can help identify potentially risky software builds before execution. The Random Forest model provides estimated failure probabilities that can help developers decide where additional testing and review may be useful.

The dataset is synthetic and the predictions are educational demonstrations, not guarantees about real CI builds.
