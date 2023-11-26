import streamlit as st
import pandas as pd
#import plotly.express as px

#st.title('Popular US Names')

df = pd.DataFrame({'column1' : [1, 2, 3, 4, 5], 'column2' : [1, 2, 3, 4, 5]})

st.dataframe(df)

# Display each dataframe using st.write()

#user_input = st.text_input('Enter a Year', 2023)

#st.write(user_input)
