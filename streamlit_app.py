import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit page configuration
st.set_page_config(
    page_title='Analyzer By Raj',
    page_icon='🧞‍♂️'
)

# Page title and header
st.title(':rainbow[Data Analyzer For Everyone]')
st.header(':gray[Explore Data with ease.]', divider='rainbow')

# File uploader
file = st.file_uploader('Drop CSV or Excel file', type=['csv', 'xlsx'])

if file!=None:
    # Check file type and read data
    if file.name.endswith('csv'):
        data = pd.read_csv(file)
    else:
        data = pd.read_excel(file)
    
    # Display data and success message
    st.dataframe(data)
    st.info('File uploaded successfully!', icon='🧞‍♂️')
else:
    st.warning('Please upload a CSV or Excel file to get started.')
