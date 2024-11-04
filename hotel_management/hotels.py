import streamlit as st
from main import (
    agregar_hotel, obtener_hoteles, modificar_hotel, eliminar_hotel, obtener_pois
)

# Función para manejar la gestión de hoteles
def manage_hotels():
    # Tabs para las acciones de hotel
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Agregar Hotel", "Modificar Hotel", "Eliminar Hotel", "Ver Detalles de Hotel", "Lista de Hoteles"])

    # Tab para agregar hotel
    with tab1:
        st.subheader("Agregar Hotel")
        nombre = st.text_input("Nombre del Hotel")
        direccion = st.text_input("Dirección")
        telefonos = st.text_input("Teléfonos (separados por coma)")
        email = st.text_input("Correo Electrónico")
        
        # Obtener la lista de puntos de interés disponibles desde la base de datos
        pois = obtener_pois()

        # Inicializar los puntos de interés seleccionados
        if "puntos_de_interes_seleccionados" not in st.session_state:
            st.session_state["puntos_de_interes_seleccionados"] = []

        # Filtrar puntos de interés no seleccionados aún
        pois_disponibles = [
            poi for poi in pois 
            if poi["_id"] not in [p["_id"] for p in st.session_state["puntos_de_interes_seleccionados"]]
        ]

        # Selección de punto de interés
        poi_seleccionado = st.selectbox(
            "Seleccione un Punto de Interés para agregar", 
            pois_disponibles, 
            format_func=lambda poi: poi["nombre"],
            key="selectbox_poi"
        )

        # Agregar el punto de interés a la lista de seleccionados
        if st.button("Agregar Punto de Interés"):
            if poi_seleccionado:
                st.session_state["puntos_de_interes_seleccionados"].append(poi_seleccionado)
                st.success(f"Punto de Interés '{poi_seleccionado['nombre']}' agregado")

        # Mostrar puntos de interés seleccionados
        st.write("Puntos de Interés seleccionados:")
        for idx, poi in enumerate(st.session_state["puntos_de_interes_seleccionados"]):
            st.write(f"{idx+1}. {poi['nombre']} - {poi['detalles']}")

        if st.button("Agregar Hotel"):
            telefonos_list = telefonos.split(",")
            puntos_de_interes_list = [poi["_id"] for poi in st.session_state["puntos_de_interes_seleccionados"]]
            agregar_hotel(nombre, direccion, telefonos_list, email, puntos_de_interes_list)
            st.success("Hotel agregado exitosamente")
            st.session_state["puntos_de_interes"] = []  # Limpiar los puntos de interés
            

    # Tab para modificar hotel
    with tab2:
        st.subheader("Modificar Hotel")
        hoteles = obtener_hoteles()
        hotel_seleccionado = st.selectbox("Seleccione un hotel", hoteles, format_func=lambda h: h["nombre"], key="selectbox_modificar_hotel")

        if hotel_seleccionado:
            st.write("Datos actuales del hotel:")
            st.dataframe(hotel_seleccionado)

            nuevo_nombre = st.text_input("Nuevo Nombre del Hotel", value=hotel_seleccionado["nombre"])
            nueva_direccion = st.text_input("Nueva Dirección", value=hotel_seleccionado["dirección"])
            nuevos_telefonos = st.text_input("Nuevos Teléfonos (separados por coma)", value=",".join(hotel_seleccionado["teléfono"]))
            nuevo_email = st.text_input("Nuevo Correo Electrónico", value=hotel_seleccionado["email"])
            # nuevos_pois = st.text_input("Nuevos Puntos de Interés (separados por coma)", value=",".join(poi["nombre"] for poi in hotel_seleccionado["puntos_de_interés"]))

            if st.button("Guardar Cambios"):
                updates = {
                    "nombre": nuevo_nombre,
                    "dirección": nueva_direccion,
                    "teléfono": nuevos_telefonos.split(","),
                    "email": nuevo_email,
                    # "puntos_de_interés": [{"nombre": nombre} for nombre in nuevos_pois.split(",")]
                }
                modificar_hotel(hotel_seleccionado["_id"], updates)
                st.success("Hotel modificado exitosamente")

    # Tab para eliminar hotel
    with tab3:
        st.subheader("Eliminar Hotel")
        hoteles = obtener_hoteles()
        hotel_seleccionado = st.selectbox("Seleccione un hotel a eliminar", hoteles, format_func=lambda h: h["nombre"],key="selectbox_eliminar_hotel")

        if hotel_seleccionado:
            st.write("¿Está seguro de que desea eliminar el siguiente hotel?")
            st.dataframe(hotel_seleccionado)

            if st.button("Eliminar Hotel"):
                eliminar_hotel(hotel_seleccionado["_id"])
                st.success("Hotel eliminado exitosamente")

    # Tab para ver detalles de un hotel
    with tab4:
        st.subheader("Ver Detalles de Hotel")
        hoteles = obtener_hoteles()
        hotel_seleccionado = st.selectbox("Seleccione un hotel para ver detalles", hoteles, format_func=lambda h: h["nombre"], key="selectbox_ver_detalles")

        if hotel_seleccionado:
            st.write("Detalles del hotel seleccionado:")
            st.dataframe(hotel_seleccionado)
            
    # Tab para ver lista de hoteles
    with tab5:
        st.subheader("Lista de Hoteles")
        hoteles = obtener_hoteles()
        st.json(hoteles)
