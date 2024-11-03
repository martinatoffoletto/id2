import streamlit as st
from main import (
    obtener_habitaciones, modificar_habitacion, eliminar_habitacion
)

def manage_rooms():
    st.subheader("Modificar o Eliminar Habitación")

    # Seleccionar habitación para modificar/eliminar
    habitaciones = obtener_habitaciones()
    habitacion_seleccionada = st.selectbox("Seleccione una habitación", habitaciones, format_func=lambda h: h["habitacion_id"])

    # Mostrar datos actuales de la habitación
    if habitacion_seleccionada:
        st.write("Datos actuales de la habitación:")
        st.json(habitacion_seleccionada)

        # Formulario para modificar la habitación
        nuevo_tipo = st.text_input("Nuevo Tipo de Habitación", value=habitacion_seleccionada["tipo"])
        nuevos_amenities = st.text_input("Nuevos Amenities (separados por coma)", value=",".join(habitacion_seleccionada["amenities"]))

        if st.button("Guardar Cambios de Habitación"):
            updates = {
                "tipo": nuevo_tipo,
                "amenities": nuevos_amenities.split(",")
            }
            modificar_habitacion(habitacion_seleccionada["habitacion_id"], updates)
            st.success("Habitación modificada exitosamente")

        # Botón para eliminar habitación
        if st.button("Eliminar Habitación"):
            eliminar_habitacion(habitacion_seleccionada["habitacion_id"])
            st.success("Habitación eliminada exitosamente")