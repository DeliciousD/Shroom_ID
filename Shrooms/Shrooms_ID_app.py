import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import pandas as pd

# are we actually using this?
# import tensorflow.keras.backend as K

checkpoint_path = 'C:\\Users\\danie\\Downloads\\results\\checkpoints\\test_save\\'

@st.cache(allow_output_mutation=True)
def open_model():
    model = tf.keras.models.load_model(checkpoint_path)
    model.summary()
    return model

st.title('Shroom ID')
             
df = pd.read_csv('Shroom_DB.csv')

model = open_model()

img_size = (300, 300)


if __name__ == '__main__':

    uploaded_file = st.file_uploader('', type="jpg")
    if uploaded_file is not None:
        
        img = Image.open(uploaded_file)
        image = np.expand_dims(img.resize(img_size), axis=0)

        prediction = model.predict(image).argmax(axis=1)

        scientific = df.iloc[prediction]['scientific']
        common = df.iloc[prediction]['common']
        start = df.iloc[prediction]['season start']
        end = df.iloc[prediction]['season end']
        edible = df.iloc[prediction]['Type']

        caption = f'{scientific}\nCommon name: {common}\n{edible}\nSeason: {start} - {end}'

        st.image(img, caption='', use_column_width=True)
        
        st.write(df.iloc[prediction])
        