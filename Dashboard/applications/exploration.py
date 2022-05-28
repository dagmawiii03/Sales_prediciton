import streamlit as st
import pandas as pd
import sys
import pickle


def app():

    st.title("Rosmann Pharmaceutical Sales Prediction")

    st.header("Visualization")

    st.subheader("month based on distribution")
    st.image('data/month based distribution.png')

    st.subheader("sales and customer based on holiday")
    st.image('data/sales and custom on holi.png')
    
    st.subheader("train vs test data")
    st.image('data/train vs test.png')


    