
###  Approach to the problem statement
The encoder-decoder image captioning system would encode the image, using a pre-trained Convolutional Neural Network that would produce a hidden state. Then, it would decode this hidden state by using  LSTM mechanism and generate a caption.

But RNNs tend to be computationally expensive to train and evaluate, so in practice, memory is limited to just a few elements. Attention models can help address this problem by selecting the most relevant elements from an input image.

Rather than compressing an entire image into a static representation, the Attention mechanism allows for salient features to dynamically come to the forefront as and when needed. This is especially important when there is a lot of clutter in an image.

The image is first divided into n parts,when the RNN is generating a new word, the attention mechanism is focusing on the relevant part of the image, so the decoder only uses specific parts of the image.

### Dataset
The dataset for this project is taken from the Kaggle dataset website. Here is the link for the dataset:  https://www.kaggle.com/datasets/adityajn105/flickr8k


### Libraries used:
1. numpy.
2. pandas.
3. matplotlib.
4. seaborn.
5. sklearn.
6. os.
7. time.
8. Keras
9. Tenserflow
10. tqdm

### Author
Code contributed by: **Onkar Viralekar**
- Check out my GitHub Profile: https://github.com/onkar-1432