import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración inicial
st.set_page_config(page_title="Analizador de Vehículos", layout="wide")

# Título principal
st.title("📊 Analizador de Datos de Vehículos Usados")

# Descripción del proyecto
st.markdown("""
## Descripción del Proyecto
Esta aplicación web permite visualizar y analizar datos de vehículos usados en venta. 
Proporciona herramientas interactivas para explorar distribuciones de kilometraje (odómetro) 
y relaciones entre diferentes variables mediante gráficos estadísticos.

**Funcionalidades principales:**
- Generación de histogramas para ver distribución de kilometraje
- Creación de gráficos de dispersión para analizar relaciones entre variables
- Interfaz intuitiva con controles interactivos
- Visualizaciones dinámicas con Plotly
""")

# Carga de datos
car_data = pd.read_csv('vehicles_us.csv')

# Sidebar con controles
st.sidebar.header("Opciones de Visualización")
visualization_type = st.sidebar.radio(
    "Seleccione el tipo de gráfico:",
    ('Histograma', 'Gráfico de Dispersión')
)

# Sección de gráficos
st.header("Visualización de Datos")

if visualization_type == 'Histograma':
    st.write("### Distribución del Kilometraje (Odómetro)")
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'], nbinsx=50)])
    fig.update_layout(
        title_text='Distribución del Odómetro',
        xaxis_title='Kilometraje',
        yaxis_title='Cantidad de Vehículos'
    )
    st.plotly_chart(fig, use_container_width=True)

elif visualization_type == 'Gráfico de Dispersión':
    st.write("### Relación entre Kilometraje y Año del Modelo")
    fig = go.Figure(data=[go.Scatter(
        x=car_data['model_year'],
        y=car_data['odometer'],
        mode='markers'
    )])
    fig.update_layout(
        title_text='Kilometraje vs Año del Modelo',
        xaxis_title='Año del Modelo',
        yaxis_title='Kilometraje'
    )
    st.plotly_chart(fig, use_container_width=True)

# Información adicional
st.markdown("---")
st.info("ℹ️ Utilice los controles en la barra lateral para cambiar entre diferentes visualizaciones.")