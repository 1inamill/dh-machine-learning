import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.write('This is a machine learning model!')

with st.expander('Data'):
with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/1inamill/datasets/master/penguins_cleaned.csv')
  df
