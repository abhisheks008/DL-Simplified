# Ship Detection using DL 

## PROJECT TITLE

Ship Detection from Aerial Images

## GOAL

To detect whether there are any ships in the given picture or not. 

## DATASET

The link for the dataset used in this project:  https://www.kaggle.com/datasets/andrewmvd/ship-detection <br>
For making annotations manually: https://www.makesense.ai


## DESCRIPTION

This project aims to identify whether there are ships present in the given image.

## WHAT I HAD DONE

For YOLOv5 and YOLOv8:
1. First converted the XML annotations into YOLO format.
2. Created a new file called 'custom_ship_data.yaml' which will have basic info related to our custom data.
3. Passed this yaml file to pre-trained YOLOv5/YOLOv8 model.
4. Fine-tuned the model so as it will not exhaust the available RAM.
5. Computed mAP50 score.
6. Visualised the predictions made by the model.

## MODELS USED

1. YOLOv5s
2. YOLOv5m
3. YOLOv5x
4. YOLOv8


## LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0
- pytorch

## VISUALIZATION
![yolov5s_val_pred](https://github.com/achrekarom12/DL-Simplified/assets/88442486/21edbe30-6f75-4f36-8551-090c6a79c326)



## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Precision
- Recall
- mAP50
- mAP50-95


## RESULTS
Results on Val dataset:

| Model      | Precision | Recall    |  mAP50   |
|------------|----------|---------|-----------|
| YOLOv5s    | 0.914     | 0.784   | 0.913   |
| YOLOv5m    | 0.851     | 0.926   | 0.949   |
| YOLOv5x    | 0.894     | 0.935   | 0.961   |
| YOLOv8    | 0.955     | 0.791   | 0.941   |



## CONCLUSION
Based on results we can draw following conclusions:
1. YOLOv5s achieved high precision (0.914) and recall (0.784), with a mean Average Precision at 50% (mAP50) of 0.913. It demonstrates a good balance between detecting ships accurately and minimizing false positives.
2. YOLOv5m performed slightly better in recall (0.926) compared to YOLOv5s, resulting in a higher mAP50 of 0.949. This model is better at capturing more ship instances, but it may have a few more false positives.
3. YOLOv5x showed the highest recall (0.935) and mAP50 (0.961) among all models, indicating its capability to detect most ship instances accurately.
4. YOLOv8 achieved the highest precision (0.955) among the models, but its recall (0.791) is comparatively lower, leading to an mAP50 of 0.941. It is efficient at reducing false positives, but it may miss some ship instances.
