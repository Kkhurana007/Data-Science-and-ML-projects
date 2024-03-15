import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define a function to load and preprocess the data, now using st.experimental_memo
@st.experimental_memo
def load_data():
    # Adjust the file path as necessary
    file_path = '3JvQGpyXTZ-PFweepiZKSQ_47a207dade754ec7a57c068a31f4ffa1_Chinook-Sample-Data.xlsx'
    xls = pd.ExcelFile(file_path)
    data_df = pd.read_excel(xls, sheet_name='Data')
    data_df['LengthMinutes'] = data_df['Milliseconds'] / 60000  # Convert milliseconds to minutes
    return data_df

data_df = load_data()

# Sidebar filters
st.sidebar.header('Filters')
genre_filter = st.sidebar.multiselect(
    'Select Genres',
    options=data_df['Genre'].unique(),
    default=data_df['Genre'].unique()
)

mediatype_filter = st.sidebar.multiselect(
    'Select Media Types',
    options=data_df['MediatType'].unique(),
    default=data_df['MediatType'].unique()
)

# Filter data based on selection
filtered_data = data_df[data_df['Genre'].isin(genre_filter) & data_df['MediatType'].isin(mediatype_filter)]

# App title
st.title('Chinook Sample Data Insights')

# Visualizations with filtered data
st.header('Distribution of Tracks by Genre')
genre_counts = filtered_data['Genre'].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="viridis")
st.pyplot(fig)

st.header('Average Track Length by Genre')
avg_track_length_by_genre = filtered_data.groupby('Genre')['LengthMinutes'].mean().sort_values(ascending=False)
fig, ax = plt.subplots()
sns.barplot(x=avg_track_length_by_genre.values, y=avg_track_length_by_genre.index, palette="rocket")
st.pyplot(fig)

st.header('Distribution of Tracks by MediaType')
mediatype_counts = filtered_data['MediatType'].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=mediatype_counts.values, y=mediatype_counts.index, palette="coolwarm")
st.pyplot(fig)

st.header('Histogram of Track Lengths')
fig, ax = plt.subplots()
sns.histplot(filtered_data['LengthMinutes'], bins=30, color='skyblue')
st.pyplot(fig)
