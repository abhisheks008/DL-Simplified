import streamlit as st

st.title("Butterfly Species classification 🦋")
st.divider()
st.image("https://i.postimg.cc/T1YP6Nr7/s-l1200.jpg")
st.subheader("More about Butterflies")
st.write('''
Butterflies 🦋 are nature's delicate dancers, fluttering gracefully through sunlit meadows and vibrant gardens. With their kaleidoscope of colors and gentle wings, they bring joy and wonder wherever they go. Their metamorphosis from tiny caterpillars to exquisite winged beauties symbolizes transformation and growth 🌱. Watching them flit from flower to flower is a reminder to embrace change and find beauty in every stage of life. 🌸✨''')
st.divider()
st.subheader("Introduction")
st.write('''
The web app is created using streamlit framework. It contains a heading, small introduction and then a image uploader.
          After the user uploads image, the image goes to backend and respected class is predicted by the CNN model and then
          the uploaded image along with prediction is showed. We can play with prediciton time and accuracy by changing batch_size,
          number of epochs and using a different CNN architecture.

''')
st.divider()
uploaded_file = st.file_uploader("Enter image to Predict", type=['png', 'jpg'])
submit = st.button("Submit")
st.write("It may take 2-3 minutes to predict the image")
if submit:
    if uploaded_file is not None:

        import tensorflow as tf
        from keras.preprocessing.image import ImageDataGenerator
        train_datagen = ImageDataGenerator(rescale = 1./255,
                                        shear_range = 0.2,
                                        zoom_range = 0.2,
                                        horizontal_flip = True)
        training_set = train_datagen.flow_from_directory('dataset/train',
                                                        target_size = (64, 64),
                                                        batch_size = 30,
                                                        class_mode = 'categorical')
        test_datagen = ImageDataGenerator(rescale = 1./255)
        test_set = test_datagen.flow_from_directory('dataset/test',
                                                    target_size = (64, 64),
                                                    batch_size = 30,
                                                    class_mode = 'categorical')
        # LeNet-5 architecture
        lenet = tf.keras.models.Sequential()

        # Layer 1: Convolutional layer with 6 filters, kernel size 5x5, and ReLU activation
        lenet.add(tf.keras.layers.Conv2D(filters=6, kernel_size=5, activation='relu', input_shape=[64, 64, 3]))

        # Layer 2: Average pooling layer with pool size 2x2 and strides 2
        lenet.add(tf.keras.layers.AveragePooling2D(pool_size=2, strides=2))

        # Layer 3: Convolutional layer with 16 filters, kernel size 5x5, and ReLU activation
        lenet.add(tf.keras.layers.Conv2D(filters=16, kernel_size=5, activation='relu'))

        # Layer 4: Average pooling layer with pool size 2x2 and strides 2
        lenet.add(tf.keras.layers.AveragePooling2D(pool_size=2, strides=2))

        # Layer 5: Flatten layer
        lenet.add(tf.keras.layers.Flatten())

        # Layer 6: Fully connected layer with 120 units and ReLU activation
        lenet.add(tf.keras.layers.Dense(units=120, activation='relu'))

        # Layer 7: Fully connected layer with 84 units and ReLU activation
        lenet.add(tf.keras.layers.Dense(units=84, activation='relu'))

        # Layer 8: Output layer with 46 units (assuming it's the number of classes) and softmax activation
        lenet.add(tf.keras.layers.Dense(units=100, activation='softmax'))

        # Compile the model with Adam optimizer and categorical crossentropy loss
        lenet.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        lenet.fit(x = training_set, validation_data = test_set, epochs = 15)

        # Part 4 - Making a single prediction
        print(training_set.class_indices)
        import numpy as np
        from keras.preprocessing import image
        if uploaded_file is not None:
            try:
                class_indices = {'ADONIS': 0, 'AFRICAN GIANT SWALLOWTAIL': 1, 'AMERICAN SNOOT': 2, 'AN 88': 3, 'APPOLLO': 4, 'ARCIGERA FLOWER MOTH': 5, 'ATALA': 6, 'ATLAS MOTH': 7, 'BANDED ORANGE HELICONIAN': 8, 'BANDED PEACOCK': 9, 'BANDED TIGER MOTH': 10, 'BECKERS WHITE': 11, 'BIRD CHERRY ERMINE MOTH': 12, 'BLACK HAIRSTREAK': 13, 'BLUE MORPHO': 14, 'BLUE SPOTTED CROW': 15, 'BROOKES BIRDWING': 16, 'BROWN ARGUS': 17, 'BROWN SIPROETA': 18, 'CABBAGE WHITE': 19, 'CAIRNS BIRDWING': 20, 'CHALK HILL BLUE': 21, 'CHECQUERED SKIPPER': 22, 'CHESTNUT': 23, 'CINNABAR MOTH': 24, 'CLEARWING MOTH': 25, 'CLEOPATRA': 26, 'CLODIUS PARNASSIAN': 27, 'CLOUDED SULPHUR': 28, 'COMET MOTH': 29, 'COMMON BANDED AWL': 30, 'COMMON WOOD-NYMPH': 31, 'COPPER TAIL': 32, 'CRECENT': 33, 'CRIMSON PATCH': 34, 'DANAID EGGFLY': 35, 'EASTERN COMA': 36, 'EASTERN DAPPLE WHITE': 37, 'EASTERN PINE ELFIN': 38, 'ELBOWED PIERROT': 39, 'EMPEROR GUM MOTH': 40, 'GARDEN TIGER MOTH': 41, 'GIANT LEOPARD MOTH': 42, 'GLITTERING SAPPHIRE': 43, 'GOLD BANDED': 44, 'GREAT EGGFLY': 45, 'GREAT JAY': 46, 'GREEN CELLED CATTLEHEART': 47, 'GREEN HAIRSTREAK': 48, 'GREY HAIRSTREAK': 49, 'HERCULES MOTH': 50, 'HUMMING BIRD HAWK MOTH': 51, 'INDRA SWALLOW': 52, 'IO MOTH': 53, 'Iphiclus sister': 54, 'JULIA': 55, 'LARGE MARBLE': 56, 'LUNA MOTH': 57, 'MADAGASCAN SUNSET MOTH': 58, 'MALACHITE': 59, 'MANGROVE SKIPPER': 60, 'MESTRA': 61, 'METALMARK': 62, 'MILBERTS TORTOISESHELL': 63, 'MONARCH': 64, 'MOURNING CLOAK': 65, 'OLEANDER HAWK MOTH': 66, 'ORANGE OAKLEAF': 67, 'ORANGE TIP': 68, 'ORCHARD SWALLOW': 69, 'PAINTED LADY': 70, 'PAPER KITE': 71, 'PEACOCK': 72, 'PINE WHITE': 73, 'PIPEVINE SWALLOW': 74, 'POLYPHEMUS MOTH': 75, 'POPINJAY': 76, 'PURPLE HAIRSTREAK': 77, 'PURPLISH COPPER': 78, 'QUESTION MARK': 79, 'RED ADMIRAL': 80, 'RED CRACKER': 81, 'RED POSTMAN': 82, 'RED SPOTTED PURPLE': 83, 'ROSY MAPLE MOTH': 84, 'SCARCE SWALLOW': 85, 'SILVER SPOT SKIPPER': 86, 'SIXSPOT BURNET MOTH': 87, 'SLEEPY ORANGE': 88, 'SOOTYWING': 89, 'SOUTHERN DOGFACE': 90, 'STRAITED QUEEN': 91, 'TROPICAL LEAFWING': 92, 'TWO BARRED FLASHER': 93, 'ULYSES': 94, 'VICEROY': 95, 'WHITE LINED SPHINX MOTH': 96, 'WOOD SATYR': 97, 'YELLOW SWALLOW TAIL': 98, 'ZEBRA LONG WING': 99}
                test_image = image.load_img(uploaded_file, target_size = (64, 64))
                test_image = image.img_to_array(test_image)
                test_image = np.expand_dims(test_image, axis = 0)
                result = lenet.predict(test_image)
                prediction = lenet.predict(test_image)
                predicted_class_index = np.argmax(prediction)
                predicted_class_name = [key for key, value in class_indices.items() if value == predicted_class_index][0]
                st.image(uploaded_file)
                st.write(predicted_class_name)
                print(predicted_class_index)
                
                
            except:
                st.write("There is error in file provided")
                
        elif uploaded_file is None:
            st.markdown(":red[Please enter a image]")


