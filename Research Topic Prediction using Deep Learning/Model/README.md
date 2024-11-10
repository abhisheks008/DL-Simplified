# Research-topic-Prediction

## Overview

Researchers have access to large online archives of scientific articles. As a consequence, finding relevant articles has become more difficult. Tagging or topic modelling provides a way to give token of identification to research articles which facilitates recommendation and search process.

## Dataset

The dataset used in this challenge consists of research papers with their titles, abstracts, and corresponding categories. The categories include:

- Computer Science
- Physics
- Mathematics
- Statistics
- Quantitative Biology
- Quantitative Finance

## Approach

The approach used to solve this challenge is as follows:

1. **Data Preprocessing**: The title and abstract of each research paper are combined and preprocessed by removing punctuation, converting to lowercase, and removing stop words.
2. **Feature Extraction**: The preprocessed text data is then converted into numerical features using the CountVectorizer and TfidfTransformer from scikit-learn.
3. **Model Training**: A MultiOutputClassifier with a LinearSVC estimator is trained on the feature data to predict the categories of the research papers.
4. **Model Evaluation**: The performance of the model is evaluated using accuracy score, precision, recall, and F1-score.
5. **Submission**: The predicted categories for the test data are submitted in a CSV file.

## Code Structure

The code is organized into the following sections:

1. **Importing Libraries**: The necessary libraries, including scikit-learn, pandas, and numpy, are imported.
2. **Loading Data**: The training and test data are loaded from CSV files.
3. **Data Preprocessing**: The title and abstract of each research paper are combined and preprocessed.
4. **Feature Extraction**: The preprocessed text data is converted into numerical features.
5. **Model Training**: The MultiOutputClassifier with a LinearSVC estimator is trained on the feature data.
6. **Model Evaluation**: The performance of the model is evaluated using accuracy score, precision, recall, and F1-score.
7. **Submission**: The predicted categories for the test data are submitted in a CSV file.

## Dependencies

The following dependencies are required to run the code:

- scikit-learn
- pandas
- numpy

