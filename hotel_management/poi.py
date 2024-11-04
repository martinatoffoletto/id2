import streamlit as st
from main import agregar_poi, modificar_poi, eliminar_poi, obtener_hoteles_por_poi, obtener_pois

def manage_poi():
    st.title("Gestión de Puntos de Interés")

    # Tab options for creating/modifying/deleting POIs and searching hotels by POI
    tabs = st.tabs(["Crear/Modificar/Eliminar", "Buscar Hoteles por Punto de Interés"])

    # Tab 1: Create/Modify/Delete POIs
    with tabs[0]:
        st.subheader("Crear/Modificar/Eliminar Puntos de Interés")

        # Select mode: Add, Modify, or Delete
        modo = st.selectbox("Selecciona una acción", ["Crear", "Modificar", "Eliminar"])
        pois = obtener_pois()
        if modo == "Crear":
            nombre = st.text_input("Nombre del Punto de Interés")
            detalles = st.text_area("Detalles del Punto de Interés")

            if st.button("Agregar Punto de Interés"):
                agregar_poi(nombre, detalles)
                st.success(f"Punto de interés '{nombre}' agregado exitosamente.")

        elif modo == "Modificar":
            poi_seleccionado = st.selectbox(
                "Seleccione el Punto de Interés a modificar", 
                pois, 
                format_func=lambda poi: poi["nombre"]  # Mostrar el nombre del punto de interés
            )

            if poi_seleccionado:
                nuevo_nombre = st.text_input("Nuevo Nombre del Punto de Interés", value=poi_seleccionado["nombre"])
                nuevos_detalles = st.text_area("Nuevos Detalles del Punto de Interés", value=poi_seleccionado["detalles"])

            if st.button("Modificar Punto de Interés"):
                modificar_poi(poi_seleccionado["_id"], nuevo_nombre, nuevos_detalles)
                st.success(f"Punto de interés '{nuevo_nombre}' modificado exitosamente.")

        elif modo == "Eliminar":
            poi_seleccionado = st.selectbox(
                "Seleccione el Punto de Interés a eliminar", 
                pois, 
                format_func=lambda poi: poi["nombre"]  # Mostrar el nombre del punto de interés
            )

            if st.button("Eliminar Punto de Interés"):
                eliminar_poi(poi_seleccionado["_id"])
                st.success("Punto de interés eliminado exitosamente.")

    # Tab 2: Search Hotels by POI
    with tabs[1]:
        st.subheader("Buscar Hoteles por Punto de Interés")

        # Obtener la lista de puntos de interés desde la base de datos
        pois = obtener_pois()

        # Seleccionar un Punto de Interés de la lista
        poi_seleccionado = st.selectbox(
            "Seleccione el Punto de Interés para buscar hoteles", 
            pois, 
            format_func=lambda poi: poi["nombre"]  # Mostrar el nombre del punto de interés
        )

        if st.button("Buscar Hoteles"):
            if poi_seleccionado:
                hoteles = obtener_hoteles_por_poi(poi_seleccionado["_id"])
                if hoteles:
                    for hotel in hoteles:
                        st.write(f"Hotel: {hotel['nombre']}")
                        st.write(f"Dirección: {hotel['dirección']}")
                        st.write(f"Teléfono: {', '.join(hotel['teléfono'])}")
                        st.write("---")
                else:
                    st.info("No se encontraron hoteles asociados a este punto de interés.")