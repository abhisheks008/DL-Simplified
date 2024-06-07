from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import torch
import numpy as np
import streamlit as st
import tensorflow as tf
import pandas as pd
import papermill as pm
import os

# Set the app title and favicon
st.set_page_config(page_title='Book Recommendation System',
                   page_icon='📚', layout='wide')


# Run .ipynb file if model doesn't contain the final_data & cosine_sim

# Execute the IPython Notebook

if not (os.path.exists('AI Based Book Recommendation System/Dataset/final_data.csv') and os.path.exists('AI Based Book Recommendation System/Model/cosine_sim.npy')):
    warn = st.warning(
        'Models not found! Running the notebook to create models.')
    pm.execute_notebook(
        'AI Based Book Recommendation System/Model/recommendation_model.ipynb',
        'AI Based Book Recommendation System/output_notebook.ipynb'
    )
    warn.empty()

else:
    model_present = st.success('Models already exist!')


# Function to load the pickled model

@st.cache_resource()
def load_models():
    cosine_sim = np.load('AI Based Book Recommendation System/Model/cosine_sim.npy')
    ncf_model = load_model('AI Based Book Recommendation System/Model/ncf_model.h5')
    cnn_model = load_model("AI Based Book Recommendation System/Model/cnn_model.h5")
    df = pd.read_csv("AI Based Book Recommendation System/Dataset/final_data_with_ratings.csv")
    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(df['Desc'])
    message = st.success('Models loaded successfully!')
    # message.empty()
    return cosine_sim, df, ncf_model, cnn_model, tokenizer


cosine_sim, final_data, ncf_model, cnn_model, tokenizer = load_models()


# Get the list of book titles from the final_data DataFrame using pandas
options = final_data['Title'].values.tolist()

# print(options[:5]) # Output check


# Create the Streamlit app
def main():

    # Set the app title
    st.title('Book Recommendation System')

    # Add a dropdown to the main content
    selected_option = st.selectbox(
        'Select an option', pd.Series(options).sort_values().unique())
    # Display the selected option
    st.write('You selected:', selected_option)

    def hybrid_recommendation(book_title, df, cosine_sim, ncf_model, cnn_model, tokenizer, max_len=200):
        # Baseline Recommendation System
        def recommend_books_cosine(book_title, final_data, cosine_sim):

            # Check if the final_data DataFrame is empty
            if not final_data.empty:
                # Get the index of the book title
                idx = final_data[final_data['Title'] == book_title].index
                print(f"idx: {idx}")
                if len(idx) > 0:
                    idx = idx[0]
                    sim_scores = list(enumerate(cosine_sim[idx]))
                    print(f"sim_scores: {sim_scores}")
                    sim_scores = sorted(
                        sim_scores, key=lambda x: x[1], reverse=True)
                    sim_scores = sim_scores[1:11]
                    print(f"sim_scores top 10: {sim_scores}")
                    book_indices = [i[0] for i in sim_scores]
                    print(f"book_indices: {book_indices}")
                    # return book title with image url and author
                    return final_data[['Title', 'Image', 'Author', 'Pages']].iloc[book_indices]
                else:
                    return "Book not found"
            else:
                return "No data available"

        # Cosine similarity recommendations
        cosine_recs = recommend_books_cosine(book_title, df, cosine_sim)

        # NCF recommendations using the trained model
        user_id = df['user_id'].iloc[0]  # Replace with the actual user ID
        book_ids = [df[df['Title'] == title]['ISBN'].values[0]
                    for title in cosine_recs['Title']]
        ncf_recs = []
        for book_id in book_ids:
            user_tensor = torch.tensor([int(user_id)], dtype=torch.long)
            book_tensor = torch.tensor([int(book_id)], dtype=torch.long)
            rating_pred = ncf_model([user_tensor, book_tensor])[0].numpy()
            # rating_pred = tf.reshape(ncf_model([user_tensor, book_tensor]), [-1]).numpy()
            ncf_recs.append((book_id, rating_pred))

        ncf_recs = sorted(ncf_recs, key=lambda x: x[1], reverse=True)

        # CNN recommendations
        cnn_recs = []
        for book_id in book_ids:
            book_desc = df[df['ISBN'] == book_id]['Desc'].values[0]
            book_seq = tokenizer.texts_to_sequences([book_desc])
            book_pad = pad_sequences(book_seq, maxlen=max_len)
            rating_pred = cnn_model.predict(book_pad).item()
            cnn_recs.append((book_id, rating_pred))

        cnn_recs = sorted(cnn_recs, key=lambda x: x[1], reverse=True)

        # Combine and rank recommendations
        combined_recs = list(set([book for book, _ in cnn_recs]))
        final_recs = [(df[df['ISBN'] == book_id]['Title'].values[0],
                       df[df['ISBN'] == book_id]['Image'].values[0],
                       df[df['ISBN'] == book_id]['Author'].values[0],
                       df[df['ISBN'] == book_id]['Pages'].values[0])
                      for book_id in combined_recs]

        return pd.DataFrame(final_recs, columns=['Title', 'Image', 'Author', 'Pages'])

    book = hybrid_recommendation(
        selected_option, final_data, cosine_sim, ncf_model, cnn_model, tokenizer)

    # Display book recommendations
    st.subheader('Recommended Books')

    # align books in a row
    col1, col2, col3, col4, col5 = st.columns(5, gap='large')

    with col1:
        st.image(book.iloc[0, 1], caption=book.iloc[0, 0], width=150)
        # st.write(book.iloc[0, 0])
        st.write(book.iloc[0, 2])
        st.write("Pages: ", book.iloc[0, 3])

    with col2:
        st.image(book.iloc[1, 1], caption=book.iloc[1, 0], width=150)
        # st.write(book.iloc[1, 0])
        st.write(book.iloc[1, 2])
        st.write("Pages: ", book.iloc[1, 3])

    with col3:
        st.image(book.iloc[2, 1], caption=book.iloc[2, 0], width=150)
        # st.write(book.iloc[2, 0])
        st.write(book.iloc[2, 2])
        st.write("Pages: ", book.iloc[2, 3])

    with col4:
        st.image(book.iloc[3, 1], caption=book.iloc[3, 0], width=150)
        # st.write(book.iloc[3, 0])
        st.write(book.iloc[3, 2])
        st.write("Pages: ", book.iloc[3, 3])

    with col5:
        st.image(book.iloc[4, 1], caption=book.iloc[4, 0], width=150)
        # st.write(book.iloc[4, 0])
        st.write(book.iloc[4, 2])
        st.write("Pages: ", book.iloc[4, 3])


    # Books Recommended in a column
    # for i in range(5):
    #     st.image(book.iloc[i, 1], width=150)
    #     st.write(book.iloc[i, 0])
    #     st.write(book.iloc[i, 2])
    #     st.write(book.iloc[i, 3])
    #     st.write('______')
if __name__ == '__main__':
    main()
