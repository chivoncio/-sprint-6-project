# primero importamos todas las librerias necesarias
import streamlit as st
import pandas as pd
import plotly_express as px

# leere el archivo CSV y se le asignara una variable
car_data = pd.read_csv('vehicles_us.csv')
# se creara la variable que se usara al momento de presionar un boton
hist_button = st.button('Construir histograma')
disp_button = st.button('Construir diagrama de dispersion')

st.header("Graficas para Vehiculos vendidos en US :car:",)

if hist_button:  # al hacer clic en el botón
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.scatter(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
