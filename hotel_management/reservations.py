import streamlit as st
from main import (
    agregar_reserva, obtener_reservas, obtener_huespedes, obtener_hoteles, buscar_habitacion_disponible
)
from datetime import datetime

def manage_reservations():
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

    
    codigo_reserva = st.text_input("Código de Reserva")

    tarifa = st.number_input("Tarifa", min_value=0.0)
    


    if st.button("Agregar Reserva"):
        agregar_reserva( huesped_id, habitacion_id, codigo_reserva, fecha_inicio_str, fecha_salida_str, tarifa)
        st.success("Reserva agregada exitosamente")

    # Mostrar lista de reservas
    st.subheader("Lista de Reservas")
    reservas = obtener_reservas()
    for reserva in reservas:
        st.write(reserva)