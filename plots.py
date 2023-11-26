import streamlit as st
import pandas as pd
#import plotly.express as px

#st.title('Popular US Names')

url = 'https://www.baseball-reference.com/awards/hof.shtml'
dfs = pd.read_html(url)

# Display each dataframe using st.write()
for i, df in enumerate(dfs):
    st.write(f"DataFrame {i+1}")
    st.dataframe(df)  # You can also use st.table(df) if you prefer a table view
    st.write("---") 

#user_input = st.text_input('Enter a Year', 2023)

#st.write(user_input)
