import streamlit as st
from main import (
    agregar_hotel, obtener_hoteles, modificar_hotel, eliminar_hotel
)

# Función para manejar la gestión de hoteles
def manage_hotels():
    # Agregar nuevo hotel
    st.subheader("Agregar Hotel")
    nombre = st.text_input("Nombre del Hotel")
    direccion = st.text_input("Dirección")
    telefonos = st.text_input("Teléfonos (separados por coma)")
    email = st.text_input("Correo Electrónico")
    # Ingresar múltiples puntos de interés
    puntos_de_interes = []
    st.write("Agregar Puntos de Interés")

    # Crear un formulario dinámico para los puntos de interés
    if "puntos_de_interes" not in st.session_state:
        st.session_state["puntos_de_interes"] = []

    nombre_poi = st.text_input("Nombre del Punto de Interés")
    detalles_poi = st.text_input("Detalles del Punto de Interés")

    if st.button("Agregar Punto de Interés"):
        if nombre_poi:
            # Añadir el punto de interés a la lista en session_state
            st.session_state["puntos_de_interes"].append({"nombre": nombre_poi, "detalles": detalles_poi})
            st.success(f"Punto de Interés '{nombre_poi}' agregado")
        else:
            st.error("El nombre del punto de interés es obligatorio")

    puntos_de_interes = st.session_state["puntos_de_interes"]
    # Mostrar puntos de interés actuales
    for idx, poi in enumerate(st.session_state["puntos_de_interes"]):
        st.write(f"{idx+1}. {poi['nombre']} - {poi['detalles']}")

    if st.button("Agregar Hotel"):
        telefonos_list = telefonos.split(",")
        puntos_de_interes_list = puntos_de_interes
        agregar_hotel(nombre, direccion, telefonos_list, email, puntos_de_interes_list)
        st.success("Hotel agregado exitosamente")

    # Mostrar lista de hoteles
    st.subheader("Lista de Hoteles")
    hoteles = obtener_hoteles()
    for hotel in hoteles:
        st.write(hotel)
        
        
    st.subheader("Modificar o Eliminar Hotel")

    # Seleccionar hotel para modificar/eliminar
    hoteles = obtener_hoteles()
    hotel_seleccionado = st.selectbox("Seleccione un hotel", hoteles, format_func=lambda h: h["nombre"])

    # Mostrar datos actuales del hotel
    if hotel_seleccionado:
        st.write("Datos actuales del hotel:")
        st.json(hotel_seleccionado)

        # Formulario para modificar el hotel
        st.subheader("Modificar Hotel")
        nuevo_nombre = st.text_input("Nuevo Nombre del Hotel", value=hotel_seleccionado["nombre"])
        nueva_direccion = st.text_input("Nueva Dirección", value=hotel_seleccionado["dirección"])
        nuevos_telefonos = st.text_input("Nuevos Teléfonos (separados por coma)", value=",".join(hotel_seleccionado["teléfono"]))
        nuevo_email = st.text_input("Nuevo Correo Electrónico", value=hotel_seleccionado["email"])
        nuevos_pois = st.text_input("Nuevos Puntos de Interés (separados por coma)", value=",".join(poi["nombre"] for poi in hotel_seleccionado["puntos_de_interés"]))

        if st.button("Guardar Cambios"):
            updates = {
                "nombre": nuevo_nombre,
                "dirección": nueva_direccion,
                "teléfono": nuevos_telefonos.split(","),
                "email": nuevo_email,
                "puntos_de_interés": [{"nombre": nombre} for nombre in nuevos_pois.split(",")]
            }
            modificar_hotel(hotel_seleccionado["hotel_id"], updates)
            st.success("Hotel modificado exitosamente")

        # Botón para eliminar hotel
        if st.button("Eliminar Hotel"):
            eliminar_hotel(hotel_seleccionado["hotel_id"])
            st.success("Hotel eliminado exitosamente")

