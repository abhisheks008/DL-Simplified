import joblib
from tensorflow.keras.models import load_model, save_model

# Load or define the Keras model
cnn_model = load_model("siamese_model.h5")

# Save the Keras model as an HDF5 file
model_path = "siamese_model.h5"
save_model(cnn_model, model_path)

# Dump the model path using joblib
joblib.dump(model_path, "siamese_model.joblib")
