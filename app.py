import streamlit as st
from hotel_management import hotels, guests, reservations, rooms, poi

st.title("Hotel Management System")

# Menú de navegación
menu = ["Puntos de Interes", "Hoteles", "Habitaciones", "Huéspedes", "Reservas" ]
choice = st.sidebar.selectbox("Selecciona una sección", menu)

if choice == "Puntos de Interes":    
    poi.manage_poi()
elif choice == "Hoteles":
    hotels.manage_hotels()
elif choice == "Habitaciones":
    rooms.manage_rooms()
elif choice == "Huéspedes":
    guests.manage_guests()
elif choice == "Reservas":
    reservations.manage_reservations()
