import streamlit as st

def load_fluid_geometry_style():
    """
    Inyecta el CSS personalizado para el diseño 'Fluid Geometry' (Diseño 3).
    Aplica fondo degradado y el efecto Glassmorphism a los contenedores.
    """
    st.markdown("""
    <style>
    /* 1. Fondo fluido con degradados */
    body {
        background: linear-gradient(135deg, #1A1A2E 0%, #0F0F2A 50%, #0A0A1F 100%); /* Degradado base */
        background-color: #1A1A2E !important; /* fallback si el degradado falla */
    }
    .stApp {
        background-color: transparent; /* Permite ver el degradado del body */
    }

    /* 2. Glassmorphism y bordes redondeados para contenedores */
    .stChat, .stBlock, .stContainer, .stMarkdown {
        background: rgba(255, 255, 255, 0.08); /* Fondo semi-transparente */
        border-radius: 15px; /* Bordes redondeados */
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1); /* Sombra sutil */
        backdrop-filter: blur(8px); /* Efecto de desenfoque de vidrio */
        -webkit-backdrop-filter: blur(8px); /* Para compatibilidad con Safari */
        border: 1px solid rgba(255, 255, 255, 0.1); /* Borde translúcido */
        padding: 10px;
    }

    /* 3. Ajustes para la barra de chat inferior */
    .stChatInputContainer {
        background: rgba(255, 255, 255, 0.15) !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }

    /* Color del texto y ajustes globales */
    h1, h2, h3, h4, h5, h6, .stMarkdown, .stTextInput > div > div > input {
        color: #E0E0E0; /* Texto claro */
    }
    </style>
    """, unsafe_allow_html=True)

# Llama a la función de estilo para inicializar si es necesario
if __name__ == "__main__":
    load_fluid_geometry_style()
    st.title("Estilo de Prueba Cargado")
