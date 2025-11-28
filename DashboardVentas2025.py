import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Análisis de Ventas de Productos')

# --- 1. Leer el archivo de datos ---
st.header('Paso 1: Carga de Datos')
file_path = 'Orders.xlsx'

try:
    df_orders = pd.read_excel(file_path)
    st.success('Archivo Orders.xlsx cargado exitosamente.')
    st.write('Primeras 5 filas del DataFrame:')
    st.dataframe(df_orders.head())

    st.write('Tipos de datos de las columnas:')
    st.write(df_orders.dtypes)

    # --- 2. Calcular los productos más vendidos ---
    st.header('Paso 2: Productos Más Vendidos')
    product_sales = df_orders.groupby('Product Name')['Quantity'].sum().reset_index()

    # Ordenar en orden descendente y obtener los 5 productos principales
    top_5_products = product_sales.sort_values(by='Quantity', ascending=False).head(5)
    st.write('Top 5 Productos Más Vendidos:')
    st.dataframe(top_5_products)

    # --- 3. Crear y mostrar el gráfico de barras ---
    st.header('Paso 3: Gráfico de los Top 5 Productos Más Vendidos')
    fig = px.bar(
        top_5_products,
        x='Product Name',
        y='Quantity',
        title='Top 5 Productos Más Vendidos',
        labels={'Product Name': 'Producto', 'Quantity': 'Cantidad Total Vendida'}
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)

except FileNotFoundError:
    st.error(f"Error: El archivo no se encontró en la ruta especificada: {file_path}. "
             "Asegúrate de que la ruta sea correcta y el archivo exista.")
except Exception as e:
    st.error(f"Ocurrió un error al cargar o procesar el archivo: {e}")
