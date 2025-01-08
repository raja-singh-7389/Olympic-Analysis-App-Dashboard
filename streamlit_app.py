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
    # Filter for Summer Olympics
    df = df[df['Season'] == 'Summer']
    # Merge with region data
    df = df.merge(region_df, on='NOC', how='left')
    # Drop duplicates
    df.drop_duplicates(inplace=True)
    # One-hot encode medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df

df = preprocess(df, region_df)

# Generate lists of years and countries
def country_year_list(df):
    years = ['Overall'] + sorted(df['Year'].dropna().unique().tolist())
    countries = ['Overall'] + sorted(df['region'].dropna().unique().tolist())
    return years, countries

# Fetch medal tally based on filters
def fetch_medal_tally(df, year, country):
    if year == 'Overall' and country == 'Overall':
        tally = df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].reset_index()
    elif year == 'Overall' and country != 'Overall':
        tally = df[df['region'] == country].groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].reset_index()
    elif year != 'Overall' and country == 'Overall':
        tally = df[df['Year'] == year].groupby('region').sum()[['Gold', 'Silver', 'Bronze']].reset_index()
    else:
        tally = df[(df['Year'] == year) & (df['region'] == country)].groupby('region').sum()[['Gold', 'Silver', 'Bronze']].reset_index()
    
    return tally

# Sidebar for user input
st.sidebar.title("Olympics Analysis")
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete wise Analysis')
)

# Medal Tally functionality
if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    
    # Get dropdown options
    years, countries = country_year_list(df)
    
    # User selections
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", countries)
    
    # Fetch filtered medal tally
    medal_tally = fetch_medal_tally(df, selected_year, selected_country)
    
    # Display appropriate title
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Medal Tally")
    elif selected_year != 'Overall' and selected_country == 'Overall':
        st.title(f"Medal Tally in {selected_year} Olympics")
    elif selected_year == 'Overall' and selected_country != 'Overall':
        st.title(f"{selected_country} Overall Performance")
    else:
        st.title(f"{selected_country}'s Performance in {selected_year} Olympics")
    
    # Display the medal tally table
    st.table(medal_tally)
