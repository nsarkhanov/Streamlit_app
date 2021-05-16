import streamlit as st
import src.func.graphics_function
import src.func.functions
import pandas as pd


def load_data(upload_data):
    df_train = pd.read_csv(upload_data)
    return df_train


def app():
    st.title("Application - :male-construction-worker: ")
    st.subheader("Upload  Dataset")
    train_data = st.file_uploader("", type=['csv'])
    if train_data is not None:
        # st.write(type(train_data))
        # st.write(dir(data))
        file_info = {'file name': train_data.name,
                     'file type': train_data.type}
        st.write(file_info)
        st.subheader('Train data loaded ')
        st.write(load_data(train_data))
