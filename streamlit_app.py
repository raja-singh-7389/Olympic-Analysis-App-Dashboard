import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit page configuration
st.set_page_config(
    page_title='Analyzer By Raj',
    page_icon='🧞‍♂️'
)

# Page title and header
st.title(':rainbow[🧞‍♂️ Data Analyzer For Everyone]')
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

st.subheader(':rainbow[Basic information of the dataset]',divider='rainbow')
tab1,tab2,tab3,tab4 = st.tabs(['Summary', 'Top and Bottom Rows', 'Data Types', 'Columns'])

with tab1:
    st.write(f'There are {data.shape[0]} rows in dataset and {data.shape[1]} columns in the dataset')
    st.subheader(':gray[Statistical summary of the dataset]')
    st.dataframe(data.describe())

with tab2:
    st.subheader(':gray[Top Rows]')
    toprows = st.slider('Number of rows you want:',1,data.shape[0],key='topslider')
    st.dataframe(data.head())
    st.subheader(':gray[Bottom Rows]')
    toprows = st.slider('Number of rows you want:',1,data.shape[0],key='bottomslider')
    st.dataframe(data.tail())

with tab3:
    st.subheader(':gray[Data Type of column]')
    st.dataframe(data.dtypes)

with tab4:
    st.subheader(':gray[Column Names in Dataset]')
    st.write(list(data.columns))

st.subheader(':rainbow[Column Values To Count]',divider ='rainbow')
with st.expander('Value Count'):
    col1,col2 = st.columns(2)
    with col1:
        column = st.selectbox('Choose Column Name',options=list(data.columns
    with col2:                                                            
        toprows = st.number_input('Top rows',min_values=1,step=1)

    count = st.button('Count')
    if(count==True):
        result = data[column].value_count().reset_index().head(toprows)
        st.dataframes(result)
        st.subheader('Visualization',divider='gray')
        fig = px.bar(data_frame=result,x= column,y = 'count',template='plotly_white')
        st.plotly_chart(fig)
        fig = px.line(data_frame=df,x = column,y = 'count',template='plotly_white')
        st.plotly_chart(fig)
        fig = px.pie(data_frame=result,names= column,values = 'count')
        st.plotly_chart(fig)

st.subheader(':rainbow[Groupby : Simplify your data analysis]', divider ='rainbow')
st.write('The groupby lets you summarize data by specific categories and groups')
with st.expander('Group By your columns'):
    col1,col2,col3 = st.columns(3)
    with col1:
        groupby_cols = st.multiselect('Choose your column to groupby',options = list(data.columns))

    with col2:
        operation_cols = st.selectbox('Choose column for operation',options = list(data.columns))

    with col3:
        operation = st.selectbox('Choose operation',options=['sum','max','min','median','count'])

    if(groupby_cols):
        result= data.groupby(groupby_cols).agg(
            newcol = (operation_col,operation)
        ).reset_index()

       st.dataframe(result)

       st.subheader(':gray[Data Visualization]',divider='gray')
       graphs = st.selectbox('Choose your graphs',options=['line','bar','scatter','pie','sunburst'])
       if(graphs=='line'):
           x_axis = st.selectbox('Choose X axis',options=list(result.columns))
           y_axis = st.selectbox('Choose Y axis',options=list(result.columns))
           color = st.selectbox('Color Information',options=[None] + list(result.columns))
           fig = px.line(data_frame=result,x=x_axis,y=y_axis,color=color,markers='o')
           st.plotly_chart(fig)
                         
       elif(graphs == 'bar'):
           x_axis = st.selectbox('Choose X axis',options=list(result.columns))
           y_axis = st.selectbox('Choose Y axis',options=list(result.columns))
           color = st.selectbox('Choose Information',options=[None] +list(result.columns))
           facet_col = st.selectbox('Choose Information',options=[None] +list(result.columns))
           fig = px.bar(data_frame=result,x=x_axis,y=y_axis,color=color,facet_col=facet_col,barmode='group')
           st.plotly_chart(fig)

       elif(graphs=='scatter'):
           x_axis = st.selectbox('Choose X axis',options=list(result.columns))
           y_axis = st.selectbox('Choose Y axis',options=list(result.columns))
           color = st.selectbox('Choose Information',options=[None] +list(result.columns))
           size = st.selectbox('Size Column',options=[None] +list(result.columns))
           fig = px.scatter(data_frame=result,x=x_axis,y=y_axis,color=color,size=size)
           st.plotly_chart(fig)

      elif(graphs=='pie'):
          values = st.selectbox('Choose Numerical Values',options=list(result.columns))
          fig = px.pie(data_frame=result,path=path,values='newcol')
          st.plotly_chart(fig)

       elif(graphs =='sunburst'):
           path = st.multiselect('Choose your path',options=list(result.columns))
           fig = px.sunburst(data_frame=result,path=path,values='newcol')
           st.plotly_chart(fig)
































        















