import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

st.header('Mi app con DataFrames y gráficos en Streamlit')

# Mensaje 1
st.write('¡Bienvenido a mi app personalizada de Streamlit!')

# Mensaje 2
st.write('Aquí muestro algunos datos y gráficos usando pandas, numpy y Altair.')

# Creo un DataFrame con datos ficticios de ventas mensuales de una tienda
df_ventas = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'Ventas': [15000, 18000, 17000, 19000, 21000, 23000]
})
st.write('Ventas mensuales de la tienda:', df_ventas)

# Mensaje 3
st.write('Ahora un DataFrame con datos aleatorios de temperaturas y humedad:')

# Creo un DataFrame con datos meteorológicos simulados
np.random.seed(42)
df_clima = pd.DataFrame({
    'Día': np.arange(1, 31),
    'Temperatura (°C)': np.random.normal(25, 5, 30).round(1),
    'Humedad (%)': np.random.uniform(40, 80, 30).round(1)
})
st.write(df_clima)

# Mensaje 4
st.write('Gráfico interactivo de Temperatura vs Humedad:')

# Gráfico Altair para mostrar relación entre temperatura y humedad
chart = alt.Chart(df_clima).mark_circle(size=60).encode(
    x='Temperatura (°C)',
    y='Humedad (%)',
    tooltip=['Día', 'Temperatura (°C)', 'Humedad (%)'],
    color='Temperatura (°C)',
    size='Humedad (%)'
).interactive()

st.write(chart)

# Mensaje 5
st.write('Gracias por visitar mi app Streamlit!')