import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)


pickle_in = open("classTapApp.pkl","rb")
classifierTap=pickle.load(pickle_in)


#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predictionParkinson(age,Male,TapPerform):
    
    
    predictionTap=classifierTap.predict([[TapPerform, age,Male]])
    
    if predictionTap==0:
        pred=0
    else:
        pred=1            
    return pred



def main():
    st.title("AM Parkinson")
    #html_temp = """
    #<div style="background-color:tomato;padding:10px">
    #<h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    #</div>
    #"""
    #st.markdown(html_temp,unsafe_allow_html=True)
    Im=Image.open("PicApp.jpg")
    st.image(Im,width=300)
    
    age = st.text_input("Age","Type Here")
    Male = st.text_input("Gender: 1 if Male, 0 if Female","Type Here")
    TapPerform = st.text_input("Tapping Performance","Type Here")
    result=""
    if st.button("Evaluate my performance"):
        result=predictionParkinson(int(age),int(Male),int(TapPerform))
        if result==0:
            st.success('You do not present Parkinson related symptoms')
        else:       
            st.success('Based on your general performance, you should stay alert and visit your doctor')

if __name__=='__main__':
    main()