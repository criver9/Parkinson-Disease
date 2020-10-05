# -*- coding: utf-8 -*-
"""
Created on Oct 1 02:20:31 2020

@author: Catalina Rivera
"""

# -*- coding: utf-8 -*-
"""
Created on Oct 1 02:20:31 2020

@author: Catalina Rivera
"""


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("logreg.pkl","rb")
logreg=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(TapPerform,age,Male,GenderMissing):
    
   
   
    prediction=logreg.predict([[TapPerform,age,Male,GenderMissing]])
    print(prediction)
    return prediction



def main():
    st.title("Parkinson Symptoms")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Parkinson ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    TapPerform = st.text_input("Tap Performance","Type Here")
    age = st.text_input("Age","Type Here")
    Male = st.text_input("Gender 0:F, 1:M","Type Here")
    GenderMissing = st.text_input("Prefer not answer","Type Here")
    result=""
    if st.button("Should I stay alert?"):
        result=predict_note_authentication(TapPerform,age,Male,GenderMissing)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    