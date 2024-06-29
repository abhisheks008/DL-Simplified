import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


with open('poem.txt', 'r', encoding='utf-8') as file:
    poems = file.readlines()

# tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(poems)
total_words = len(tokenizer.word_index) + 1

# training datapreparation
input_sequences = []
for line in poems:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

xs, labels = input_sequences[:,:-1],input_sequences[:,-1]

# ys = tf.keras.utils.to_categorical(labels, num_classes=total_words)

# to load the model
model = tf.keras.models.load_model('poemgenerator2.keras')

# poem generator
def generate_poem(seed_text, next_words):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predict = np.argmax(model.predict(token_list))
        # predicted = model.predict_classes(token_list, verbose=0)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predict:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text


#---streamlit ---
#css for streamlit
bg_img  = """
<style>
[data-testid="stAppViewContainer"]{
    background-color : black;
    secondaryBackgroundColor : #55B2FF;
    color : white;
}
</style>
 """


st.title("Poem Generator 🤖")
st.markdown(bg_img , unsafe_allow_html=True)

prom = st.text_input('Enter how the poem should be started')
with st.sidebar:
    st.header("POEM GPT")
    st.write("This AI Model gives poems with the text you enter . This might produce missplaced letters in it , kindly ignore those mistakes")
if st.button('Generate Poem'):
    poem = generate_poem(prom, 50)
    st.write(poem)

# print(generate_poem("i like nature" , 30))
