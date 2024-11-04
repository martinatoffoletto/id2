import streamlit as st
from main import (
    obtener_habitaciones, modificar_habitacion, eliminar_habitacion, obtener_hoteles, agregar_habitacion
)

def manage_rooms():
    st.subheader("Modificar o Eliminar Habitación")

    # Seleccionar habitación para modificar/eliminar
    habitaciones = obtener_habitaciones()
    habitacion_seleccionada = st.selectbox("Seleccione una habitación", habitaciones, format_func=lambda h: h["_id"])

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
            modificar_habitacion(habitacion_seleccionada["_id"], updates)
            st.success("Habitación modificada exitosamente")

        # Botón para eliminar habitación
        if st.button("Eliminar Habitación"):
            eliminar_habitacion(habitacion_seleccionada["_id"])
            st.success("Habitación eliminada exitosamente")
            
            


    st.subheader("Agregar Habitación")

    # Obtener lista de hoteles desde la base de datos
    hoteles = obtener_hoteles()

    if not hoteles:
        st.warning("No hay hoteles disponibles. Agrega un hotel antes de crear habitaciones.")
    else:
        # Crear lista desplegable con nombres de hoteles
        hotel_opciones = {hotel["nombre"]: hotel["_id"] for hotel in hoteles}
        hotel_seleccionado_nombre = st.selectbox("Selecciona el Hotel", list(hotel_opciones.keys()))
        hotel_seleccionado_id = hotel_opciones[hotel_seleccionado_nombre]

        # Captura de detalles de la habitación
        habitacion_tipo = st.text_input("Tipo de Habitación (Ej: Suite, Estándar, etc.)")
        amenities = st.text_input("Amenities (separados por coma)").split(",")

        # Botón para agregar habitación
        if st.button("Agregar Habitación"):
            if habitacion_tipo and amenities:
                # Llamar a la función de main.py para agregar la habitación
                agregar_habitacion(
                    hotel_id=hotel_seleccionado_id,
                    tipo=habitacion_tipo,
                    amenities=amenities
                )
                st.success(f"Habitación tipo '{habitacion_tipo}' agregada al hotel '{hotel_seleccionado_nombre}' exitosamente.")
            else:
                st.error("Por favor, completa todos los campos de la habitación.")
