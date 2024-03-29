import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define a function to load and preprocess the data
@st.cache
def load_data():
    # Adjust the file path as necessary
    file_path = 'bi5EoWE9QkiqEMz37MceAw_2edba123616f40909cb8896b374a31a1_Fenix-Shipping-Data.xlsx'
    xls = pd.ExcelFile(file_path)
    data_df = pd.read_excel(xls, sheet_name='Data')
    data_df['LengthMinutes'] = data_df['Milliseconds'] / 60000  # Convert milliseconds to minutes
    return data_df

data_df = load_data()

# App title
st.title('Chinook Sample Data Insights')

# Visualizations
st.header('Distribution of Tracks by Genre')
genre_counts = data_df['Genre'].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="viridis")
st.pyplot(fig)

st.header('Average Track Length by Genre')
avg_track_length_by_genre = data_df.groupby('Genre')['LengthMinutes'].mean().sort_values(ascending=False)
fig, ax = plt.subplots()
sns.barplot(x=avg_track_length_by_genre.values, y=avg_track_length_by_genre.index, palette="rocket")
st.pyplot(fig)

st.header('Distribution of Tracks by MediaType')
mediatype_counts = data_df['MediatType'].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=mediatype_counts.values, y=mediatype_counts.index, palette="coolwarm")
st.pyplot(fig)

st.header('Histogram of Track Lengths')
fig, ax = plt.subplots()
sns.histplot(data_df['LengthMinutes'], bins=30, color='skyblue')
st.pyplot(fig)
