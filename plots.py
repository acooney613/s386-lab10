import streamlit as st
import seaborn as sns
import pandas as pd

df = pd.read_html('https://www.baseball-reference.com/awards/hof.shtml')[0]

user_input = st.text_input('Enter a Year', 2023)

st.write(user_input)
