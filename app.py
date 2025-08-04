
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
avatar_url = "https://labs.heygen.com/interactive-avatar/share?share=eyJxdWFsaXR5IjoiaGlnaCIsImF2YXRhck5hbWUiOiI0ZTI5Mzk1YmM2OGI0NzI1YjIxNzM0YzJm%0D%0ANGYwYzJhMiIsInByZXZpZXdJbWciOiJodHRwczovL2ZpbGVzMi5oZXlnZW4uYWkvYXZhdGFyL3Yz%0D%0ALzRlMjkzOTViYzY4YjQ3MjViMjE3MzRjMmY0ZjBjMmEyL2Z1bGwvMi4yL3ByZXZpZXdfdGFyZ2V0%0D%0ALndlYnAiLCJuZWVkUmVtb3ZlQmFja2dyb3VuZCI6ZmFsc2UsImtub3dsZWRnZUJhc2VJZCI6Ijc5%0D%0AYzdjYmQ2YWM3MjQxZDhhOTkxYTAzMmIwNjQ1M2NkIiwic2hhcmVfY29kZSI6IjAwYzQ2OWYyLTVk%0D%0AOGQtNDVmYi05M2NhLTI4Mzc1NzM3NjA1YSIsInVzZXJuYW1lIjoiMGRmMmUwMzc4MTMyNDk2ODgz%0D%0ANjhiYmQxMGQ0OWZmY2QifQ%3D%3D"

st.markdown(f'''
<p style='text-align:center; margin-top:40px;'>
    <a href="{avatar_url}" target="_blank">
        <button style='font-size:18px;padding:10px 20px;border:none;background-color:#4CAF50;color:white;border-radius:8px;cursor:pointer;'>
            Hacé clic acá para hablar con Ale, el abogado interactivo
        </button>
    </a>
</p>
''', unsafe_allow_html=True)
