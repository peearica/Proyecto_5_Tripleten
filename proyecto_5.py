import streamlit as st 
import pandas as pd 
import plotly_express as px 

st.header('Desarrollo de app web y su despliegue en un servicio en la nube público')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)
             

scat_button = st.button('Construir gráfico de dispersión') # crear un botón
        
if scat_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
            # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True) 
    
