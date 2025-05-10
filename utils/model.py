# Contains model loading and prediction functions
import tensorflow as tf
import numpy as np
from utils.data import get_model_class_names

def disease_recognition(input_image):
    """
    Analyzes leaf image to detect and classify plant diseases.

    Args:
        input_image: Image file uploaded by user

    Returns:
        tuple: (detected plant, detected condition)
    """
    class_names = get_model_class_names()

    # Load the CNN model
    cnn = tf.keras.models.load_model("model/plant_disease_detection_and_classification.keras")

    # Process the image for prediction
    image = tf.keras.preprocessing.image.load_img(input_image, target_size=(128, 128))
    input_array = tf.keras.preprocessing.image.img_to_array(image)
    input_array = np.array([input_array])

    # Make prediction and return result
    return class_names[np.argmax(cnn.predict(input_array))]