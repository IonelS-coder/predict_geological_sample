import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

import matplotlib.pyplot as plt

model_path = 'models/M3_rock_mineral_transfer.h5'
classes = ['amethyst', 'ammonite', 'aventurin', 'empty_space', 'obsidian']

st.header("Is this a mineral, a rock or a fossil?")
st.write("Choose any image and I'll predict what it is:")
uploaded_file = st.file_uploader("Choose an image...")


#@st.cache
def load_transfer_model(path_):
    model = load_model(path_)
    return model

#prediction in decimals
def predict_class(img, model):
    a = image.img_to_array(img)
    a = np.expand_dims(a, axis = 0)
    prediction = model.predict(a)[0].round(decimals = 2)
    #prediction = model.predict(a)
    return prediction 

model = load_transfer_model(model_path)
if uploaded_file is not None:
    test_image = image.load_img(uploaded_file) 
    st.image(uploaded_file, caption='Input Image', width=350) #use_column_width=True)
    prediction = predict_class(test_image, model)
    #st.write(prediction)
    st.write(f'This seems to be an ` {classes[np.where(prediction == np.amax(prediction))[0][0]]}`') #,size= 20
    

    #bar_data = pd.DataFrame({'amethyst': [prediction[0]], 'ammonite': [prediction[1]], 'aventurin': [prediction[2]], 'empty_space' : [prediction[3]], 'obsidian' : [prediction[4]]})
    #st.bar_chart(bar_data)
    

    #define df as list of lists
    bar_data = pd.DataFrame([[classes[0],prediction[0]], [classes[1], prediction[1]], [classes[2], prediction[2]], [classes[3], prediction[3]], [classes[4], prediction[4]]], columns = ['prediction', 'probability'])
    fig, ax = plt.subplots(figsize = (4,1.5)) #figsize = (2,1))

    plt.axis((0,1,0,1))
    ax.set_title('Sample prediction',fontweight="bold", size=10) # Title
    ax.set_ylabel('Score', fontsize = 8.0) # Y label
    ax.set_xlabel('Labels', fontsize = 8.0) # X label


    ax = bar_data.groupby('prediction')['probability'].mean().plot.bar()
    st.pyplot(fig)
