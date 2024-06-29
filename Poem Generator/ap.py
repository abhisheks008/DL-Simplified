
import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the Dataset
with open('poem.txt', 'r', encoding='utf-8') as file:
    poems = file.readlines()

# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(poems)
total_words = len(tokenizer.word_index) + 1

# training Data Preparation
input_sequences = []
for line in poems:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))
xs, labels = input_sequences[:,:-1],input_sequences[:,-1]

ys = tf.keras.utils.to_categorical(labels, num_classes=total_words)

# build the Model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(total_words, 100),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(150)),
    tf.keras.layers.Dense(total_words, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# train the Model
model.fit(xs, ys, epochs=10, verbose=1)

model.save('poemgenerator2.keras')
# model = tf.keras.models.load_model('poemgenerator2.keras')

# def generate_poem(seed_text, next_words):
#     for _ in range(next_words):
#        # token_list = tokenizer.texts_to_sequences([seed_text])[0]
#         token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
#         predicted = model.predict_classes(token_list, verbose=0)
#         output_word = ""
#         for word, index in tokenizer.word_index.items():
#             if index == predicted:
#                 output_word = word
#                 break
#         seed_text += " " + output_word
#     return seed_text

# st.title("Poem Generator")

# prom = st.text_input('Enter how the poem should be started')
# if st.button('Generate Poem'):
#     poem = generate_poem(prom, 50)
#     st.write(poem)
