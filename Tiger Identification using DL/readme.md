# Tiger Identification Project Using Deep Learning

## Problem Statement
Tiger identification is a critical task in wildlife conservation, enabling researchers to track and monitor individual tigers in their natural habitat. The goal of this project is to develop a robust tiger re-identification (Re-ID) system using deep learning techniques. This system will help in identifying and distinguishing individual tigers from a set of images, facilitating better management and protection of tiger populations.

### Dataset link : https://www.kaggle.com/datasets/quadeer15sh/amur-tiger-reidentification?select=Amur+Tigers

![000002](https://github.com/jeet-Abhi123/Email-SMS-spam-classifier/assets/143840497/b8eb2ce5-18a6-410d-9d14-4312220adf61)
![000024](https://github.com/jeet-Abhi123/Email-SMS-spam-classifier/assets/143840497/d79e39dd-6985-4737-aa7f-54d860df1ad2)

## Project Overview
This project implements multiple deep learning models to perform the tiger Re-ID task. The models used include DenseNet, VGG16, ResNet50, and EfficientNet. The primary objective is to build and evaluate models on a provided training set and then test their performance on a separate test set. Each test image is used as a query image, and all other images in the test set are considered as the "gallery" or "database." The query results are expected to be a rank-list of the gallery images, indicating the most likely matches.

