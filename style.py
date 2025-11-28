import streamlit as st

def load_fluid_geometry_style():
    """
    Inyecta el CSS personalizado para el diseño 'Fluid Geometry' (Diseño 3).
    Refuerza el Glassmorphism y la estética de las burbujas de chat.
    """
    st.markdown("""
    <style>
    /* 1. Fondo fluido con degradados (Se mantiene y se fuerza con !important) */
    body {
        background: linear-gradient(135deg, #1A1A2E 0%, #0F0F2A 50%, #0A0A1F 100%) !important;
        background-color: #1A1A2E !important;
    }
    .stApp {
        background-color: transparent !important; 
    }

    /* 2. Glassmorphism para contenedores y burbujas */
    /* Se aplica el color de la burbuja y se refina el Glassmorphism */
    .stChat, .stBlock, .stContainer, .stMarkdown {
        background: rgba(255, 255, 255, 0.08); 
        border-radius: 15px; 
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2); /* Sombra más pronunciada para profundidad */
        backdrop-filter: blur(10px); /* Desenfoque más fuerte */
        -webkit-backdrop-filter: blur(10px); 
        border: 1px solid rgba(255, 255, 255, 0.15); /* Borde más visible */
        padding: 20px; /* Mayor padding para más aire */
        transition: transform 0.2s ease-in-out; /* Nueva: Animación sutil al interactuar */
    }
    
    /* 3. Estilo para la Burbuja del Asistente (Gemini) */
    /* Se le da un color sutil para diferenciar la respuesta */
    .stChatMessage [data-testid="stChatMessageContent"] {
        background: rgba(180, 180, 255, 0.08); /* Tono azulado semi-transparente para el asistente */
        border-radius: 12px;
        padding: 15px;
    }

    /* 4. Estilo para la Burbuja del Usuario */
    .stChatMessage [data-testid="stChatMessageContent"]:first-child {
        background: rgba(255, 255, 255, 0.05); /* Ligeramente más transparente */
        border-radius: 12px;
        padding: 15px;
    }
    
    /* 5. Ajustes para la barra de chat inferior (Glassmorphism fuerte) */
    .stChatInputContainer {
        background: rgba(255, 255, 255, 0.18) !important; /* Más transparencia */
        border-radius: 20px !important; /* Bordes más grandes */
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3) !important; 
        backdrop-filter: blur(15px) !important;
        border: 2px solid #5B3C88 !important; /* Nuevo: Borde de color de acento */
    }

    /* 6. Color del texto y algunos ajustes globales */
    h1, h2, h3, h4, h5, h6, .stMarkdown, .stTextInput > div > div > input, .stButton > button {
        color: #E0E0E0 !important; /* Texto claro consistente */
    }

    /* Ocultar el 'Manage app' button para limpiar la UI */
    footer {visibility: hidden;}

    </style>
    """, unsafe_allow_html=True)

# Llama a la función de estilo para inicializar si es necesario
if __name__ == "__main__":
    load_fluid_geometry_style()
