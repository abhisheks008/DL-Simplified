# [VisAlgae 2023 Challenge Dataset](https://www.kaggle.com/datasets/marquis03/high-throughput-algae-cell-detection?select=train) 🌿🔬

## Overview

Microalgae play a vital role in various fields, including marine environments, biomedical research, clean energy, and food engineering. Monitoring the abundance and species composition of microalgae is crucial for identifying environmental issues and maintaining ecological balance. The VisAlgae 2023 Challenge Dataset addresses the need for a high-throughput, multi-classification, and multi-scale microalgae cell detection method using microfluidic chip technology.

## Dataset Description 📊

### Objective
The dataset aims to facilitate the development of object detection algorithms for high-throughput algae cell detection. The challenges include detecting small targets, handling multiscale issues, managing motion blur, dealing with complex backgrounds, and maximizing detection accuracy.

### Microfluidic Platform 💧
Experiments were conducted on a high-throughput microfluidic platform, capturing dynamic video data of microalgal cells under different fields of view and imaging conditions.

### Algal Cell Types 🦠
The dataset comprises six types of microalgal cells:

- Platymonas (Class 0)
- Chlorella (Class 1)
- Dunaliella salina (Class 2)
- Effrenium (Class 3)
- Porphyridium (Class 4)
- Haematococcus (Class 5)

### Data Split 📂
- Training Set: 700 images
- Testing Set: 300 images

### Annotation Format 🗒️
Annotations for the training set are provided in YOLO format, with each image having a corresponding .txt file. The format for each line in the .txt file is as follows:

```
Class, x_center, y_center, w, h
```

### Classes 📋
- 0: Platymonas
- 1: Chlorella
- 2: Dunaliella salina
- 3: Effrenium
- 4: Porphyridium
- 5: Haematococcus

## VisAlgae Challenge and Workshop 🚀

The dataset is part of the second International "Vision Meets Algae" (VisAlgae) Challenge and Workshop, held in conjunction with the IEEE Cybermatics Conference. Researchers and developers are invited to participate in the challenge to address practical issues in high-throughput algae cell detection. The dataset provides a real-world scenario for developing innovative object detection algorithms that can contribute to the advancement of microalgae research and ecological protection.

## Acknowledgments 🙌

This dataset is made possible by the collaborative efforts of the organizers of VisAlgae 2023 and contributors to microalgae research. We encourage participants to explore creative solutions and contribute to the development of tools that will enhance ecological protection and resource management in the field of microalgae research. 🌍🔍