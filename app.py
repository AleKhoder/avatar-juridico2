
import streamlit as st

st.set_page_config(page_title="Asistente Legal Interactivo", layout="centered")

st.title("👨‍⚖️ Ale - Abogado Interactivo")

st.markdown("""
Hola, soy **Ale**, tu abogado interactivo especializado en Derecho Laboral argentino.  
Podés preguntarme sobre despidos, indemnizaciones, trabajo en negro y más.  
Estoy acá para ayudarte.  

🔸 *Este asistente responde únicamente en español.*
""")

# URL del avatar de HeyGen (truncada por seguridad y longitud)
avatar_url = "https://labs.heygen.com/interactive-avatar/share?share=eyJxdWFsaXR5IjoiaGlnaCIsImF2..."

st.markdown(f'''
<p style='text-align:center; margin-top:40px;'>
    <a href="{avatar_url}" target="_blank">
        <button style='font-size:18px;padding:10px 20px;border:none;background-color:#4CAF50;color:white;border-radius:8px;cursor:pointer;'>
            Hacé clic acá para hablar con Ale, el abogado interactivo
        </button>
    </a>
