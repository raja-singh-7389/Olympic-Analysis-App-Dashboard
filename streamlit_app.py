import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title='Analyzer By raj',
    page_icon='🧞‍♂️'
)
st.title(':rainbow[Data Analyzer For Everyone]')
st.header(':gray[Explore Data with ease.]',divider='rainbow')

file = st.file_uploader('Drop csv or excel file',type['csv','xlsx'])
if(file!=None):
  if(file.name.endswith('csv')):
      data = pd.read_csv(file)
  else:
      data = pd.read_excel(file)

st.dataframe(data)
st.info('file uploaded succefully',icon='🧞‍♂️')


