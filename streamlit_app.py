import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

# Load data
df = pd.read_csv('medal_tally.csv')
region_df = pd.read_csv('noc_regions.csv')

# Preprocess data
def preprocess(df, region_df):
    df = df[df['Season'] == 'Summer']  # Filter for Summer Olympics
    df = df.merge(region_df, on='NOC', how='left')  # Merge with region data
    df.drop_duplicates(inplace=True)  # Drop duplicates
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)  # One-hot encode medals
    return df

df = preprocess(df, region_df)

# Sidebar menu
st.sidebar.title("Olympics Analysis")
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete wise Analysis')
)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    
    # Ensure helper functions exist
    import helper
    
    years, country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
    
    # Display titles based on selected options
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    elif selected_year != 'Overall' and selected_country == 'Overall':
        st.title(f"Medal Tally in {selected_year} Olympics")
    elif selected_year == 'Overall' and selected_country != 'Overall':
        st.title(f"{selected_country} Overall Performance")
    else:
        st.title(f"{selected_country}'s Performance in {selected_year} Olympics")
    
    st.table(medal_tally)
