
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Asistente Legal Interactivo", layout="centered")

st.title("👨‍⚖️ Ale - Abogado Interactivo")
st.markdown("Hola, soy **Ale**, tu abogado interactivo especializado en Derecho Laboral argentino. "
            "Podés preguntarme sobre despidos, indemnizaciones, trabajo en negro y más. "
            "Estoy acá para ayudarte.")

components.iframe(
    src="https://labs.heygen.com/interactive-avatar/share?share=eyJxdWFsaXR5IjoiaGlnaCIsImF2YXRhck5hbWUiOiI0ZTI5Mzk1YmM2OGI0NzI1YjIxNzM0YzJmNGYwYzJhMiIsInByZXZpZXdJbWciOiJodHRwczovL2ZpbGVzMi5oZXlnZW4uYWkvYXZhdGFyL3YzLzRlMjkzOTViYzY4YjQ3MjViMjE3MzRjMmY0ZjBjMmEyL2Z1bGwvMi4yL3ByZXZpZXdfdGFyZ2V0LndlYnAiLCJuZWVkUmVtb3ZlQmFja2dyb3VuZCI6ZmFsc2UsImtub3dsZWRnZUJhc2VJZCI6Ijc5YzdjYmQ2YWM3MjQxZDhhOTkxYTAzMmIwNjQ1M2NkIiwic2hhcmVfY29kZSI6IjAwYzQ2OWYyLTVkOGQtNDVmYi05M2NhLTI4Mzc1NzM3NjA1YSIsInVzZXJuYW1lIjoiMGRmMmUwMzc4MTMyNDk2ODgzNjhiYmQxMGQ0OWZmY2QifQ%3D%3D",
    height=600,
    width=800,
    scrolling=False
)
