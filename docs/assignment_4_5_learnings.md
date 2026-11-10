# Assignment 4_5 – Build-Failure Prediction

## 1. Introduction
The objective of this assignment is to build a machine learning model that predicts whether a software build is likely to fail based on changes made to the code.

This project extends the existing SmartCI project by adding a build-failure prediction component.

## 2. Dataset
A synthetic dataset containing 300 build records was generated for this project.

The dataset is stored in `ml/builds.csv`.

The following features are used:

- `files_changed` – Number of files modified in a build.
- `lines_changed` – Number of lines of code changed.
- `hour` – Hour at which the build was made.
- `failed` – Target variable indicating whether the build failed (1) or succeeded (0).

## 3. Data Generation
A Python script named `scripts/generate_builds.py` was used to generate the synthetic build dataset.

The generated data was saved as a CSV file and used for training and testing the machine learning model.

## 4. Machine Learning Model
A Random Forest Classifier was selected to predict build failures.

The implementation is available in `ml/predict_failure.py`.

The dataset was divided into:
- 80% training data.
- 20% testing data.

The model was configured with 100 decision trees and `class_weight="balanced"`.

## 5. Model Evaluation
The model was evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Feature importance

The actual evaluation results are generated when the prediction script is executed.

## 6. Build Failure Prediction
Two example builds were used to demonstrate predictions:

**High-risk build**
- Files changed: 12
- Lines changed: 450
- Build hour: 22

**Lower-risk build**
- Files changed: 2
- Lines changed: 15
- Build hour: 10

The model estimates the probability of failure for both examples.

## 7. Tools and Technologies
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Git and GitHub
- Visual Studio Code

## 8. Learning Outcomes
Through this assignment, I learned:

1. How to generate and work with a synthetic dataset.
2. How to identify input features and a target variable.
3. How to divide a dataset into training and testing sets.
4. How to train a Random Forest classification model.
5. How to evaluate a machine learning model.
6. How to predict build-failure probabilities.
7. How machine learning can help improve Continuous Integration workflows.

## 9. Conclusion
This assignment demonstrates how machine learning can be integrated into a CI project to estimate the risk of build failures. The model provides a basic approach to identifying potentially risky builds based on code changes and build timing.

The project extends the existing SmartCI repository while preserving the previously completed labs.
