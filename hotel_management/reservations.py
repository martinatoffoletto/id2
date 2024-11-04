import streamlit as st
from main import (
    agregar_reserva, obtener_reservas, obtener_huespedes, obtener_hoteles, buscar_habitacion_disponible, obtener_reserva_por_codigo, obtener_reservas_por_huesped, obtener_reservas_por_fecha
)
from datetime import datetime

def manage_reservations():
    tab1, tab2,tab3,tab4,tab5 = st.tabs(["Agregar Reserva","Reserva por codigo", "Reserva por huesped", "Reserva por fecha","Lista de Reservas"])
    with tab1:
        st.subheader("Agregar Reserva")
        
        # Obtener datos de huéspedes y hoteles desde MongoDB
        huespedes = obtener_huespedes()
        hoteles = obtener_hoteles()

        # Lista de IDs de huéspedes
        huespedes_opciones = {f"{huesped['nombre']} {huesped['apellido']}": huesped["_id"] for huesped in huespedes}
        huesped_seleccionado_id = st.selectbox("Selecciona el Huésped", list(huespedes_opciones.keys()))
        huesped_id = huespedes_opciones[huesped_seleccionado_id]

        # Lista de IDs de hoteles
        hoteles_opciones = {hotel["nombre"]: hotel["_id"] for hotel in hoteles}
        hotel_seleccionado_nombre = st.selectbox("Selecciona el Hotel", list(hoteles_opciones.keys()))
        hotel_id = hoteles_opciones[hotel_seleccionado_nombre]
        
        fecha_inicio = st.date_input("Fecha de Inicio")
        fecha_salida = st.date_input("Fecha de Salida")
        
        fecha_inicio_str = fecha_inicio.strftime("%Y-%m-%d")
        fecha_salida_str = fecha_salida.strftime("%Y-%m-%d")

        # Filtrar habitaciones según el hotel seleccionado
        habitaciones = buscar_habitacion_disponible(hotel_id, fecha_inicio_str, fecha_salida_str)

        habitaciones_opciones = {habitacion["tipo"]: habitacion["_id"] for habitacion in habitaciones}
        
        if habitaciones_opciones:
            habitacion_seleccionada_tipo = st.selectbox("Habitaciones disponibles", list(habitaciones_opciones.keys()))
            habitacion_id = habitaciones_opciones[habitacion_seleccionada_tipo]
        else:
            st.warning("Este hotel no tiene habitaciones disponibles.")
            return


        tarifa = st.number_input("Tarifa", min_value=0.0)
        


        if st.button("Agregar Reserva"):
            codigo_reserva = agregar_reserva( [huesped_id], habitacion_id, fecha_inicio_str, fecha_salida_str, tarifa)
            st.success("Reserva agregada exitosamente con codigo: " + codigo_reserva)
    with tab2:
        cr=st.text_input("Ingrese Código de Reserva")
        if cr:
            st.dataframe(obtener_reserva_por_codigo(cr))
    
    with tab3:
        huespedes = obtener_huespedes()
        huespedes_opciones = {f"{huesped['nombre']} {huesped['apellido']}": huesped["_id"] for huesped in huespedes}
        huesped_seleccionado_id = st.selectbox("Selecciona el Huésped", list(huespedes_opciones.items()))
        huesped_id = huesped_seleccionado_id[1]
        st.json(obtener_reservas_por_huesped(huesped_id))
    
    with tab4: 
        hoteles = obtener_hoteles()
        hoteles_opciones = {hotel["nombre"]: hotel["_id"] for hotel in hoteles}
        hotel_seleccionado_nombre = st.selectbox("Selecciona el Hotel", list(hoteles_opciones.keys()), key="Seleccion-reserva-fecha")
        hotel_id = hoteles_opciones[hotel_seleccionado_nombre]
        fecha_inicio2 = st.date_input("Fecha de reserva")
        fecha_inicio_str_2 = fecha_inicio2.strftime("%Y-%m-%d")
        st.dataframe(obtener_reservas_por_fecha(hotel_id,fecha_inicio_str_2))
        
    with tab5: 
        # Mostrar lista de reservas
        st.subheader("Lista de Reservas")
        reservas = obtener_reservas()
        st.json(reservas)