import pandas as pd
import streamlit as st 
import plotly.express as px 

# Load the data
vehicle_df = pd.read_csv('vehicles_us.csv')

# Display the data
print(vehicle_df.head())
vehicle_df.info()

# Display a header title for the web app
st.header('Vehicle Dataset')

# Crear una casilla de verificacion
build_histogram = st.checkbox('Build Histogram for Vehicle Model')

# Create an Histogram triggered by the checkbox showing the model column data
if build_histogram:
    fig = px.histogram(vehicle_df, x='model', nbins=50)
    st.plotly_chart(fig, use_container_width=True)

# Scatter Plot Button
scatter_button = st.button('Show Scatter Plot for Vehicle Odometer and Price')

# Creates a Scatter Plot trigerred by the above button showing the relation between model_year and vehicle cylinders
if scatter_button:
    fig = px.scatter(vehicle_df, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)

