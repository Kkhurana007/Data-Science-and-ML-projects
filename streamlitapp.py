import streamlit as st
import pandas as pd
import altair as alt

# Function to load data (this should be adjusted to your actual data source)
@st.cache
def load_data():
    # Adjust the file path below to where your data is located
    path = 'bi5EoWE9QkiqEMz37MceAw_2edba123616f40909cb8896b374a31a1_Fenix-Shipping-Data.xlsx'
    data = pd.read_excel(path)
    return data

data = load_data()

# Sidebar Filters
st.sidebar.header('Filters')

# Date Range Selector
date_range = st.sidebar.date_input('Select date range', [])

# Ship Via Selector
ship_via_options = sorted(data['ship_via'].unique())
ship_via_selected = st.sidebar.selectbox('Select shipping method', options=ship_via_options, index=0)

# Filter data based on selections
filtered_data = data.copy()
if date_range:
    filtered_data = filtered_data[(filtered_data['order_date'] >= date_range[0]) & (filtered_data['order_date'] <= date_range[1])]
if ship_via_selected:
    filtered_data = filtered_data[filtered_data['ship_via'] == ship_via_selected]

# Group by region
orders_per_region = filtered_data.groupby('region').size().reset_index(name='orders')

# Creating a Chart
chart = alt.Chart(orders_per_region).mark_bar().encode(
    x=alt.X('region:N', sort='-y'),
    y='orders:Q',
    color='region:N',
    tooltip=['region', 'orders']
).properties(
    title='Orders Per Region',
    width=700,
    height=400
)

# Display the chart
st.altair_chart(chart, use_container_width=True)