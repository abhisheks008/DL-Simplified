import json
import tensorflow as tf

with open('Information.json' , 'rb') as file:
    INFORMATION = json.load(file)

MODEL = tf.keras.models.load_model('model.h5')
MODEL.compile(loss="binary_crossentropy",
                optimizer=tf.keras.optimizers.Adam(),
                metrics=["accuracy"])
tf.get_logger().setLevel('ERROR') 

