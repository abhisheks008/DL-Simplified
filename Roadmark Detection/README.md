# Road Mark Detection

## Objective

The primary objective of this project is to develop and compare the performance of multiple image segmentation CNN models for road mark detection. The models employed include UNet, Mask R-CNN, and DeepLab. These models are pre-trained on standard datasets and fine-tuned on a specialized road mark detection dataset to evaluate their accuracy and effectiveness.

## Project Structure

- **Datasets Folder:** Contains the datasets used for training, validation, and testing. Detailed information regarding the datasets can be found in this folder.
- **Models Folder:** Includes the code and configurations for the various models developed and used in this project.

## How to Use

1. **Dataset:** Refer to the `Dataset` folder for information on the datasets used.
2. **Models:**  Refer to the `Models` folder for the code and configurations of the developed models.
   - [UNet Model](Models/Unet_model.ipynb)
   - [Mask R-CNN Model Template](Models/Mask_R_CNN_template.py)
   - [DeepLab Model Template](Models/DeepLab_template.py)

## Baseline CNN Model

A baseline CNN model was initially developed but showed no room for improvement. Hence, its use is deemed invalid for this project.

- [Baseline Model](Models/baseline_model.ipynb)

## Future Work

Future improvements and research directions include:
- Increasing the number of epochs for training
- Adjusting the batch size
- Implementing data augmentation techniques
- Hyperparameter tuning

## Conclusion

This project demonstrates the potential of using advanced image segmentation models for road mark detection. With adequate resources and further optimization, the performance of these models can be significantly enhanced. Contributions and suggestions for improvements are welcome.

## Contributions

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

