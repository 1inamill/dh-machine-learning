import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.write('This is a machine learning model!')

with st.expander('Data'):
df = pd.read_csv()
