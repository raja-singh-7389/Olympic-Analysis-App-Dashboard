import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit page configuration
st.set_page_config(
    page_title='Analyzer By Raj',
    page_icon='🧞‍♂️',
    layout='wide'
)

# Page title and header
st.title(':rainbow[🧞‍♂️ Data Analyzer For Everyone]')
st.header(':gray[Explore Data with ease.]', divider='rainbow')

# File uploader
file = st.file_uploader('Drop CSV or Excel file', type=['csv', 'xlsx'])
built_in_datasets = {
    "Diabetes": "diabetes.csv",
    "Heart": "heart.csv",
    "Parkinsons": "parkinsons.csv",
    "Tips": "tips.csv",
    "Titanic": "titanic.csv"
}

# Choose built-in dataset if no file is uploaded
if file is None:
    dataset_choice = st.selectbox("Or choose a built-in dataset:", options=list(built_in_datasets.keys()))
    if dataset_choice:
        file_path = built_in_datasets[dataset_choice]
        data = pd.read_csv(file_path)
        st.success(f"Using built-in dataset: {dataset_choice}")
else:
    if file.name.endswith('csv'):
        data = pd.read_csv(file)
    else:
        data = pd.read_excel(file)
    st.info('File uploaded successfully!', icon='🧞‍♂️')

# Display dataset
st.dataframe(data)

# Basic information
st.subheader(':rainbow[Basic Information of the Dataset]', divider='rainbow')
tab1, tab2, tab3, tab4 = st.tabs(['Summary', 'Top and Bottom Rows', 'Data Types', 'Columns'])

with tab1:
    st.write(f'There are {data.shape[0]} rows and {data.shape[1]} columns in the dataset.')
    st.subheader(':gray[Statistical Summary]')
    st.dataframe(data.describe())

with tab2:
    st.subheader(':gray[Top Rows]')
    top_rows = st.slider('Number of rows to display:', 1, data.shape[0], 5, key='topslider')
    st.dataframe(data.head(top_rows))
    st.subheader(':gray[Bottom Rows]')
    bottom_rows = st.slider('Number of rows to display:', 1, data.shape[0], 5, key='bottomslider')
    st.dataframe(data.tail(bottom_rows))

with tab3:
    st.subheader(':gray[Data Types of Columns]')
    st.dataframe(data.dtypes)

with tab4:
    st.subheader(':gray[Column Names]')
    st.write(list(data.columns))

# Value Counts
st.subheader(':rainbow[Column Values Count]', divider='rainbow')
with st.expander('Value Count'):
    col1, col2 = st.columns(2)
    with col1:
        column = st.selectbox('Choose a Column', options=list(data.columns))
    with col2:
        top_n = st.number_input('Top N values to display', min_value=1, step=1, value=5)
    
    if st.button('Count'):
        result = data[column].value_counts().reset_index().head(top_n)
        result.columns = [column, 'Count']
        st.dataframe(result)

        st.subheader('Visualizations', divider='gray')
        fig1 = px.bar(result, x=column, y='Count', template='plotly_white', title='Bar Chart')
        st.plotly_chart(fig1)
        fig2 = px.line(result, x=column, y='Count', markers=True, template='plotly_white', title='Line Chart')
        st.plotly_chart(fig2)
        fig3 = px.pie(result, names=column, values='Count', title='Pie Chart')
        st.plotly_chart(fig3)

# Groupby Operations
st.subheader(':rainbow[Group By: Simplify Data Analysis]', divider='rainbow')
st.write('Group data by specific columns and perform aggregate operations.')
with st.expander('Group By Options'):
    col1, col2, col3 = st.columns(3)
    with col1:
        groupby_cols = st.multiselect('Choose columns to group by', options=list(data.columns))
    with col2:
        operation_col = st.selectbox('Choose column for aggregation', options=list(data.columns))
    with col3:
        operation = st.selectbox('Choose operation', options=['sum', 'max', 'min', 'mean', 'count'])

    if groupby_cols and operation_col:
        result = data.groupby(groupby_cols).agg({operation_col: operation}).reset_index()
        result.columns = groupby_cols + [f'{operation_col}_{operation}']
        st.dataframe(result)

        st.subheader('Visualizations', divider='gray')
        graphs = st.selectbox('Choose a graph', options=['Line', 'Bar', 'Scatter', 'Pie', 'Sunburst', 'Histogram', 'Boxplot'])
        if graphs == 'Line':
            x_axis = st.selectbox('X Axis', options=list(result.columns))
            y_axis = st.selectbox('Y Axis', options=list(result.columns))
            color = st.selectbox('Color Information', options=[None] + list(result.columns))
            fig = px.line(result, x=x_axis, y=y_axis, color=color, markers=True)
            st.plotly_chart(fig)
        elif graphs == 'Bar':
            x_axis = st.selectbox('X Axis', options=list(result.columns))
            y_axis = st.selectbox('Y Axis', options=list(result.columns))
            color = st.selectbox('Color Information', options=[None] + list(result.columns))
            fig = px.bar(result, x=x_axis, y=y_axis, color=color, barmode='group')
            st.plotly_chart(fig)
        elif graphs == 'Scatter':
            x_axis = st.selectbox('X Axis', options=list(result.columns))
            y_axis = st.selectbox('Y Axis', options=list(result.columns))
            color = st.selectbox('Color Information', options=[None] + list(result.columns))
            size = st.selectbox('Size Information', options=[None] + list(result.columns))
            fig = px.scatter(result, x=x_axis, y=y_axis, color=color, size=size)
            st.plotly_chart(fig)
        elif graphs == 'Pie':
            names = st.selectbox('Names', options=list(result.columns))
            values = st.selectbox('Values', options=list(result.columns))
            fig = px.pie(result, names=names, values=values)
            st.plotly_chart(fig)
        elif graphs == 'Sunburst':
            path = st.multiselect('Path', options=list(result.columns))
            values = st.selectbox('Values', options=list(result.columns))
            fig = px.sunburst(result, path=path, values=values)
            st.plotly_chart(fig)
        elif graphs == 'Histogram':
            x_axis = st.selectbox('X Axis', options=list(result.columns))
            color = st.selectbox('Color Information', options=[None] + list(result.columns))
            fig = px.histogram(result, x=x_axis, color=color, nbins=30)
            st.plotly_chart(fig)
        elif graphs == 'Boxplot':
            x_axis = st.selectbox('X Axis', options=list(result.columns))
            y_axis = st.selectbox('Y Axis', options=list(result.columns))
            color = st.selectbox('Color Information', options=[None] + list(result.columns))
            fig = px.box(result, x=x_axis, y=y_axis, color=color)
            st.plotly_chart(fig)
