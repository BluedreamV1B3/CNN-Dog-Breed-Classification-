import streamlit as st
import tensorflow as tf
import tensorflow_datasets as tfds
dataset, info = tfds.load("stanford_dogs", as_supervised=True, with_info=True)

st.set_option('deprecation.showfileUploaderEncoding', False)
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('xception_0')
    return model
model = load_model()
st.write("""
    # Dog Breed Classification
         """
)


file = st.file_uploader("Please upload an doggy image", type = ["jpg", "png"])
from PIL import Image
import numpy as np
def import_and_predict(image_data, model):
    img = tf.keras.layers.Resizing(height = 224, width = 224, crop_to_aspect_ratio = True)(image_data)
    img = tf.keras.applications.xception.preprocess_input(img)
    inputs  = tf.expand_dims( img , axis=0) 
    predictions = model.predict(inputs)
    return predictions

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = f'Class {predicted_class_index}'
    breed_names = info.features['label'].names
    predicted_breed_name = breed_names[predicted_class_index]
    string = "This image most likely is: "+predicted_breed_name 
    st.success(string)
    
