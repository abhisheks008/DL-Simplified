# Movie Recommender System

## 📌 Project Description
This **Movie Recommender System** suggests movies based on user preferences using content-based filtering and Natural Language Processing (NLP). It analyzes movie metadata such as genres, cast, crew, and keywords to find similarities and recommend relevant movies.

## 🚀 Features
- Provides **personalized movie recommendations**
- Uses **TF-IDF Vectorization** and **Cosine Similarity** for content-based filtering
- Processes movie metadata like **genres, cast, and overview**
- Simple and interactive **user interface**
- Built with **Python, Pandas, Scikit-learn, and Streamlit (if applicable)**

## 📂 Dataset
The dataset used for this project is:
- **tmdb_5000_movies.csv** (Movie metadata)
- **tmdb_5000_credits.csv** (Cast and crew details)

Dataset Source: [Kaggle - TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## 🛠️ Technologies Used
- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn** (for text vectorization & similarity calculation)
- **NLTK** (for text preprocessing & stemming)
- **Streamlit** (for web deployment, if applicable)

## 🔧 Installation & Usage

### For the movies.pkl and similarity.pkl files 
```sh
visit this link [Google-Drive](https://drive.google.com/drive/folders/1XQoA4ff2ScaD-D5OnnCSjhgd6Zf67dIt?usp=sharing)
```
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/kanak227/Movie_recommender_system.git
cd Movie_recommender_system
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Script
```sh
python app.py
```

For **Streamlit UI**, run:
```sh
streamlit run app.py
```

## 📊 Working Principle
1. **Data Preprocessing**: Cleaning and transforming movie metadata.
2. **Feature Extraction**: Creating a combined "tags" column using movie overviews, genres, and crew details.
3. **Vectorization**: Converting text data into numerical format using **TF-IDF**.
4. **Similarity Calculation**: Using **Cosine Similarity** to measure the closeness of movies.
5. **Recommendation Generation**: Sorting and displaying the top 5 similar movies.

## 🔗 Deployment
The project is deployed on Streamlit and can be accessed using the following link:
[Movie_recommendation](https://movie-recommender-system-kv.streamlit.app/)


## 🎯 Future Improvements
- Adding **collaborative filtering** for better recommendations
- Implementing a **hybrid recommendation model**
- Integrating with a **real-time API** to fetch movie details
- Improving the **user interface**

## 📜 License
This project is open-source and available under the **MIT License**.

Enjoy the recommendations! 🎬🍿

