import streamlit as st 


header = st.container()
dataset = st.container()
analysis = st.container() 
features = st.container() 
model_training = st.container() 

with header: 
    st.title("Welcome to our Python labs project : Books rating")


with dataset: 
    st.header("Books rating dataset")



with analysis: 
    st.header("Preliminary analysis")



with features:
    st.header("Feature engineering")


with model_training: 
    st.header("Training our data model")
