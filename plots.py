import streamlit as st
import pandas as pd
#import plotly.express as px

#st.title('Popular US Names')


df = pd.read_html('https://www.baseball-reference.com/awards/hof.shtml')
df = df[0]
#print(df)
st.dataframe(df)

#user_input = st.text_input('Enter a Year', 2023)

#st.write(user_input)
