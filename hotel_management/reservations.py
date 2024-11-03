import streamlit as st
from main import (
    agregar_reserva, obtener_reservas
)

def manage_reservations():
    st.subheader("Agregar Reserva")
    huesped_id = st.text_input("ID del Huésped")
    habitacion_id = st.text_input("ID de la Habitación")
    codigo_reserva = st.text_input("Código de Reserva")
    fecha_inicio = st.date_input("Fecha de Inicio")
    fecha_salida = st.date_input("Fecha de Salida")
    tarifa = st.number_input("Tarifa", min_value=0.0)

    if st.button("Agregar Reserva"):
        agregar_reserva( huesped_id, habitacion_id, codigo_reserva, fecha_inicio, fecha_salida, tarifa)
        st.success("Reserva agregada exitosamente")

    # Mostrar lista de reservas
    st.subheader("Lista de Reservas")
    reservas = obtener_reservas()
    for reserva in reservas:
        st.write(reserva)