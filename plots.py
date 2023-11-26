import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Popular US Names')
url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'
df = pd.read_csv(url)

selected_name = st.text_input('Enter a name', 'John') 

name_df = df[df['name'] == selected_name]
if name_df.empty:
    st.write('Name not found')
else:
    fig = px.line(name_df, x='year', y='n', color='sex',
                  color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig)

selected_year = st.selectbox('Select a year', df['year'].unique())


year_df = df[df['year'] == selected_year]
girl_names = (year_df[year_df['sex'] == 'F'].sort_values(by='n', ascending=False)
              .head(5)['name'].reset_index(drop=True))
boy_names = (year_df[year_df['sex'] == 'M'].sort_values(by='n', ascending=False)
             .head(5)['name'].reset_index(drop=True))
top_names = pd.concat([girl_names, boy_names], axis=1)
top_names.columns = ['girl','boy']

st.write(f"Top names in {selected_year}")
st.dataframe(top_names)

'''df = pd.read_html('https://www.baseball-reference.com/awards/hof.shtml')[0]

user_input = st.text_input('Enter a Year', 2023)

st.write(user_input)'''
