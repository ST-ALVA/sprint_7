import pandas as pd
import streamlit as st 
import plotly.express as px 

# Load the data
vehicle_df = pd.read_csv('vehicles_us.csv')

# Mostrar un mensaje sobre la estructura de los datos
st.write("Información sobre el dataset de vehículos")
st.write(vehicle_df.head())
        
# Controles de filtrado
st.sidebar.header("Filtros de datos")
        
# Filtro para precio
price_min = int(vehicle_df['price'].min())
price_max = int(vehicle_df['price'].max())
selected_price = st.sidebar.slider('Rango de Precio', price_min, price_max, (price_min, price_max))

# Filtro para odometro
odometer_min = int(vehicle_df['odometer'].min())
odometer_max = int(vehicle_df['odometer'].max())
selected_odometer = st.sidebar.slider('Rango de Odómetro', odometer_min, odometer_max, (odometer_min, odometer_max))
        
# Aplicar filtros al DataFrame
filtered_df = vehicle_df[(vehicle_df['price'].between(selected_price[0], selected_price[1])) & 
                         (vehicle_df['odometer'].between(selected_odometer[0], selected_odometer[1]))]

# Display a header title for the web app
st.header('Visualización de Datos de Vehículos')

# Crear una casilla de verificacion
build_histogram = st.checkbox('Crear Histograma de Modelos de Vehículo')

# Create an Histogram triggered by the checkbox showing the model column data
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos filtrado')
    fig = px.histogram(filtered_df, x='model', nbins=50, labels={'model' : 'Modelo de Vehículo', 'count' : 'Número de Vehículos'})
    fig.update_layout(yaxis_title='Número de Vehículos') 
    st.plotly_chart(fig, use_container_width=True)

# Scatter Plot Button
scatter_button = st.button('Crear Scatter Plot de Odómetro vs Precio')

# Creates a Scatter Plot trigerred by the above button showing the relation between model_year and vehicle cylinders
if scatter_button:
    st.write('Scatter plot de Odómetro vs Precio de los vehículos')
    fig = px.scatter(filtered_df, x='odometer', y='price', labels={'odometer' : 'Odometro', 'price' : 'Precio'})
    st.plotly_chart(fig, use_container_width=True)