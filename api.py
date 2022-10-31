from copyreg import pickle
from statistics import variance
from flask import Flask, request
import pandas as pd
import numpy as np
import pickle 
import streamlit as st

app=Flask(__name__)

pickle_in = open("regressor.pkl","rb")
regressor = pickle.load(pickle_in)


def predict_note_authentication(variance, skewness, curtosis, entropy):
    """Let's Authenticate the Bank Note
    This is using docstrings for specification.
    ---
    parameters:
     - name: variance
       in: query
       type: number
       required: true
     - name: skewness
       in: query
       type: number
       required: true
     - name: curtosis
       in: query
       type: number
       required: true
     - name: entropy
       in: query
       type: number
       required: true
    responses:
       200:
           descriprion: The output values
    """

    prediction = regressor.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return "The predicted value is"+ str(prediction)

def main():
    st.title("Order quantity prediction")
    html_temp = """
    <div style = "background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("skewness","Type Here")
    curtosis = st.text_input("curtosis","Type Here")
    entropy = st.text_input("entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Laarn")
        st.text("Built with Streamlit")


if __name__=='__main__':
    app.run()