import streamlit as st
from main import (
    agregar_huesped, obtener_huespedes
)

def manage_guests():
    st.subheader("Agregar Huésped")
    nombre = st.text_input("Nombre")
    apellido = st.text_input("Apellido")
    telefonos = st.text_input("Teléfonos (separados por coma)")
    emails = st.text_input("Correos Electrónicos (separados por coma)")
    direccion = st.text_input("Dirección")

    if st.button("Agregar Huésped"):
        telefonos_list = telefonos.split(",")
        emails_list = emails.split(",")
        agregar_huesped(nombre, apellido, telefonos_list, emails_list, direccion)
        st.success("Huésped agregado exitosamente")

    # Mostrar lista de huéspedes
    st.subheader("Lista de Huéspedes")
    huespedes = obtener_huespedes()
    for huesped in huespedes:
        st.write(huesped)

