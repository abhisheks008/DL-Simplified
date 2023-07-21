# PollenDataset

(C) 2017 Ivan Rodriguez, Rémi Mégret, Edgar Acuña, José Agosto, Tugrul Giray

This image dataset has been created from videos captured at the entrance of a bee colony in June 2017 at the Bee facility of the Gurabo Agricultural Experimental Station of the University of Puerto Rico.

## Repository content

- `images/` contains images for pollen bearing and no pollen bearing honey bees.
    - The prefix of the images names define their class: e.g. `NP1268-15r.jpg` for non-pollen and `P7797-103r.jpg` for pollen bearing bees. The numbers correspond to frame and item number respectively, you need to be careful that they are not numbered sequentially. 
  
- `Read-skimage.ipynb` Jupyter notebook for simple script to load the data and create the dataset using `skimage` library. 

## Acknowledgement

_This dataset is based upon work supported by the National Science Foundation
under Grant No. 1707355 and 1633184._

If you publish work based on this dataset, please cite the following  publication:

* Ivan Rodriguez, Rémi Mégret, Edgar Acuña, José Agosto, Tugrul Giray. _Recognition of pollen-bearing bees from Video using Convolutional Neural Network_, IEEE Winter Conf. on Applications of Computer Vision, 2018, Lake Tahoe, NV. https://doi.org/10.1109/WACV.2018.00041

Thanks to UPR students Grace Rodriguez, Christian Esteves and Emmanuel Nieves for their help in the video annotations. Thanks to UPR students Stephanie Feliciano and Janpierre Aleman for their help in the development of the camera system.

# License

This dataset is shared on Kaggle under licenses CC-BY 4.0 and ODC-ODbL 1.0 