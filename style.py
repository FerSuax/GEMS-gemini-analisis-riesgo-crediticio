import streamlit as st

def load_fluid_geometry_style():
    """
    Inyecta el CSS avanzado para el diseño 'Fluid Geometry', eliminando artefactos 
    y puliendo el Glassmorphism y la estética del chat.
    """
    st.markdown("""
    <style>
    /* 1. CONFIGURACIÓN DEL FONDO (Mantenemos el degradado) */
    body {
        background: linear-gradient(135deg, #1A1A2E 0%, #0F0F2A 50%, #0A0A1F 100%) !important;
        background-color: #1A1A2E !important; 
    }
    .stApp {
        background-color: transparent !important;
        /* Aplicamos una pequeña sombra general para profundidad */
        box-shadow: inset 0 0 50px rgba(0, 0, 0, 0.5); 
    }

    /* 2. LIMPIEZA DE ARTEFACTOS Y FRANJAS VACÍAS */
    /* Apunta a contenedores vacíos o contenedores que no tienen contenido de usuario */
    div.stContainer:has( > div:only-child[data-testid="stVerticalBlock"]) {
        display: none; /* Elimina las franjas superiores que no tienen uso */
    }
    /* Elimina el espacio blanco extra alrededor del título y cabeceras */
    header {
        visibility: hidden;
        height: 0px !important;
    }
    /* Ocultar el footer y la marca de agua */
    footer {visibility: hidden;}

    /* 3. ESTILO DEL TÍTULO CENTRAL (H1) */
    /* Hace el título más suave para el diseño Fluid Geometry */
    .centered-title {
        color: #F0F0F0 !important;
        text-shadow: 0 0 10px rgba(0, 191, 255, 0.4); /* Brillo sutil */
        font-size: 3rem;
        margin-top: 2rem;
        margin-bottom: 2rem;
    }

    /* 4. GLASSMORHISM MEJORADO PARA BURBUJAS DE CHAT */
    .stChatMessage {
        margin-bottom: 1rem;
    }
    .stChatMessage [data-testid="stChatMessageContent"] {
        /* Glassmorphism aplicado al contenido real del chat */
        background: rgba(255, 255, 255, 0.08); /* Tono muy sutil */
        border-radius: 18px; 
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3); 
        backdrop-filter: blur(12px); /* Desenfoque fuerte */
        -webkit-backdrop-filter: blur(12px); 
        border: 1px solid rgba(255, 255, 255, 0.1); /* Borde sutil */
        padding: 20px;
        color: #E0E0E0;
    }

    /* 5. ESTILO DE LA BARRA DE ENTRADA (MÁS PROFUNDO) */
    .stChatInputContainer {
        /* Más profundidad y borde de acento */
        background: rgba(255, 255, 255, 0.18) !important;
        border-radius: 25px !important; 
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4) !important; /* Sombra más oscura */
        backdrop-filter: blur(18px) !important;
        border: 2px solid #00BFFF !important; /* Borde de acento (cian brillante) */
    }

    /* 6. CORRECCIÓN DE COLORES GENERALES */
    .stMarkdown, .stTextInput > div > div > input, .stButton > button {
        color: #E0E0E0 !important;
    }
    </style>
    """, unsafe_allow_html=True)
