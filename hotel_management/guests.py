import streamlit as st
from main import (
    agregar_huesped, obtener_huespedes, ver_detalles_huesped
)

def manage_guests():
    tab1, tab2, tab3= st.tabs(["Agregar Huesped", "Ver detalles huesped", "Lista de Huespedes"])
    with tab1:
        st.subheader("Agregar Huésped")
        nombre = st.text_input("Nombre")
        apellido = st.text_input("Apellido")
        telefonos = st.text_input("Teléfonos (separados por coma)")
        emails = st.text_input("Correos Electrónicos (separados por coma)")
        direccion_calle = st.text_input("Calle")
        direccion_numero = st.text_input("Número")
        direccion_codigo_postal = st.text_input("Código Postal")
        direccion_provincia = st.text_input("Provincia")
        direccion_pais = st.text_input("País")
        
        direccion = {
        "calle": direccion_calle,
        "número": direccion_numero,
        "código_postal": direccion_codigo_postal,
        "provincia": direccion_provincia,
        "país": direccion_pais
    }

        if st.button("Agregar Huésped"):
            telefonos_list = telefonos.split(",")
            emails_list = emails.split(",")
            agregar_huesped(nombre, apellido, telefonos_list, emails_list, direccion)
            st.success("Huésped agregado exitosamente")
    
    with tab2:
        guests = obtener_huespedes()
        huesped_seleccionador = st.selectbox("Seleccione un huesped", guests, format_func=lambda h: h["nombre"] + " " + h["apellido"])
        st.dataframe(ver_detalles_huesped(huesped_seleccionador["_id"]))
        
    with tab3:
        # Mostrar lista de huéspedes
        st.subheader("Lista de Huéspedes")
        huespedes = obtener_huespedes()
        st.dataframe(huespedes)

