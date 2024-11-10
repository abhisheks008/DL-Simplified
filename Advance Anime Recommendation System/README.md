# Anime Recommendation System

This project implements an Anime Recommendation System using both content-based and collaborative filtering techniques. It provides recommendations based on user preferences and anime content, leveraging deep learning for enhanced collaborative filtering.


## Usage

1. **Upload Datasets**
   - `anime.csv`: Contains information about anime titles, genres, and types.
   - `rating.csv`: Contains user ratings for various anime.

2. **Run the Notebook**
   Execute the `Anime Recommendation System v1.ipynb` Jupyter notebook, either locally or on platforms like Google Colab.

3. **Training**
   The model can be trained using the provided cells in the notebook. Adjust hyperparameters like `epochs` and `batch_size` as needed for training on your hardware.

4. **Recommendations**
   The notebook includes several functions for making recommendations based on different strategies, such as content-based filtering, collaborative filtering, and genre-based diversity.

## Dataset

The dataset is available on Kaggle:
- [Anime.csv and Rating.csv - Kaggle Dataset](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database)

| File       | Description                                                                                  |
|------------|----------------------------------------------------------------------------------------------|
| `anime.csv` | Contains anime metadata, including `anime_id`, `name`, `genre`, `type`, and `rating`.       |
| `rating.csv` | Contains user ratings for various anime, with fields `user_id`, `anime_id`, and `rating`.   |

## Features

- **Data Preprocessing**: Cleans and preprocesses `anime.csv` and `rating.csv` datasets.
- **Exploratory Data Analysis (EDA)**: Provides an overview of anime types, genres, ratings, and other insights.
- **Content-Based Filtering**: Generates recommendations based on anime genres, type, and average ratings.
- **Collaborative Filtering**: A deep learning-based recommendation model that learns user preferences.
- **Genre-Based Recommendations**: Ensures diverse recommendations by including various genres in top recommendations.
- **New User and New Anime Recommendations**: Customized recommendations for new users and newly added anime.

## Recommendation Strategies

### Content-Based Filtering
- Uses anime metadata (e.g., genre, type, and rating) to recommend similar anime based on a selected anime.

### Collaborative Filtering (Deep Learning)
- Leverages a neural network to predict user ratings for anime based on user preferences and anime embeddings.
- Designed to provide personalized recommendations to each user.

### Diverse Genre-Based Recommendations
- Recommends a variety of anime by selecting top anime per genre to ensure a diverse list.

### Recommendations for New Users and Anime
- **New Users**: Recommends top-rated anime across all users.
- **New Anime**: Recommends to users who have shown interest in similar genres.

### Favorite Genre Recommendations
- Identifies the top genres preferred by each user and recommends anime from these genres.

