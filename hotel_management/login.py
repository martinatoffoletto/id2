import streamlit as st
from app import main_app
from main import login


def login_screen():
    st.title("Inicio de Sesion")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    
    if st.button("Iniciar Sesión"):
        if login(username, password):
            st.session_state["authenticated"] = username
            st.success("Inicio de sesión exitoso.")
        else:
            st.error("Usuario o contraseña incorrectos.")

