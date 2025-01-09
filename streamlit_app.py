import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title='Analyzer By raj',
    page_icons='🧞‍♂️'
)
st.title(':rainbow[Data Analyzer For Everyone]')
st.header(':gray[Explore Data with ease.]',divider='rainbow')

file = st.file_uploader('Drop csv or excel file')
