import streamlit as st
from hotel_management import hotels, guests, reservations, rooms

from main import (
    agregar_hotel, obtener_hoteles, modificar_hotel, eliminar_hotel,
    agregar_habitacion, obtener_habitaciones, modificar_habitacion, eliminar_habitacion,
    agregar_huesped, obtener_huespedes, agregar_reserva, obtener_reservas,
    buscar_hoteles_cerca_poi, obtener_info_hotel, encontrar_poi_cerca_hotel,
    buscar_habitacion_disponible, obtener_amenities_habitacion,
    obtener_reserva_por_codigo, obtener_reservas_por_huesped, obtener_reservas_por_fecha,
    ver_detalles_huesped
)

st.title("Hotel Management System")

# Menú de navegación
menu = ["Hoteles", "Habitaciones", "Huéspedes", "Reservas" ]
choice = st.sidebar.selectbox("Selecciona una sección", menu)

if choice == "Hoteles":
    hotels.manage_hotels()
elif choice == "Habitaciones":
    rooms.manage_rooms()
elif choice == "Huéspedes":
    guests.manage_guests()
elif choice == "Reservas":
    reservations.manage_reservations()
