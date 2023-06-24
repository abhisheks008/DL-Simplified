# Scientific Research Article Topic Classification

## PROJECT TITLE

Scientific Research Article Topic Classification

## GOAL

To classify the scientific articles based on their topics. 

## DATASET

The dataset used for this project can be found at [link to dataset]( https://www.kaggle.com/datasets/vetrirah/janatahack-independence-day-2020-ml-hackathon?select=train.csv). 

## DESCRIPTION

This project aims to classify the scientific research papers into different domains  such as computer science, physics, mathematics and stats etc.

## WHAT I HAD DONE

1. Data collection: Collected from the kaggle dataset I have mentioned above.
2. Data preprocessing: Cleaned and preprocessed the data. In order to pass the data to the model we have to first embed it.
3. Model selection: Chose CNN, LSTM and Bi-directional LSTM.
4. Comparative analysis: Compared the Accuracy and Loss of all techniques.

## MODELS USED

1. Convolutional Neural Network
2. Long short term memory Neural Netowrk
3. Bi-directional Long short term memory Neural Netowrk


## LIBRARIES NEEDED

The following libraries are required to run this project:

- nltk
- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow

## VISUALIZATION
![pie](https://github.com/achrekarom12/DL-Simplified/assets/88442486/f280d0b8-0ae6-4cf9-9103-7a91f4873dd9)

## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss

## RESULTS
Accuracy for these models were:

| Model | Accuracy | Loss | 
| ----- | ---------------- | ---------------- | 
| CNN   | 0.324       | 0.774        |
| LSTM   | 0.713       | 0.417        |
| Bi-directional LSTM   | 0.266       | 1.326        |

## CONCLUSION
Based on the results we can draw following conclusions:
1. CNN Model: The CNN model achieved an accuracy of 0.324 and a loss of 0.774. It performed the worst among the three models, indicating that the convolutional neural network architecture might not be suitable for this task. The model struggled to capture the complex relationships and dependencies within the research papers' titles and abstracts.
2. LSTM Model: The LSTM model performed better than the CNN model with an accuracy of 0.713 and a lower loss of 0.417. LSTM networks are known for their ability to capture sequential dependencies in text data, which could explain the improved performance compared to the CNN model. However, there is still room for improvement.
3. Bi-directional LSTM Model: The bi-directional LSTM model had the lowest accuracy of 0.266 and a relatively higher loss of 1.326. This indicates that the bi-directional architecture did not provide significant improvements over the standard LSTM model for this particular task.
