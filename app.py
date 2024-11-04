import streamlit as st
from hotel_management import hotels, guests, reservations, rooms, login

from main import (
    agregar_hotel, obtener_hoteles, modificar_hotel, eliminar_hotel,
    agregar_habitacion, obtener_habitaciones, modificar_habitacion, eliminar_habitacion,
    agregar_huesped, obtener_huespedes, agregar_reserva, obtener_reservas,
    buscar_hoteles_cerca_poi, obtener_info_hotel, encontrar_poi_cerca_hotel,
    buscar_habitacion_disponible, obtener_amenities_habitacion,
    obtener_reserva_por_codigo, obtener_reservas_por_huesped, obtener_reservas_por_fecha,
    ver_detalles_huesped,logout,is_authenticated
)



if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = None

if st.session_state["authenticated"]:
    if is_authenticated(st.session_state["authenticated"]):
        st.title("Hotel Management System")

        menu = ["Hoteles", "Habitaciones", "Huéspedes", "Reservas"]
        choice = st.sidebar.selectbox("Selecciona una sección", menu)

        if choice == "Hoteles":
            hotels.manage_hotels()  
        elif choice == "Habitaciones":
            rooms.manage_rooms()  
        elif choice == "Huéspedes":
            guests.manage_guests()  
        elif choice == "Reservas":
            reservations.manage_reservations() 
        
        if st.sidebar.button("Cerrar Sesión"):
            logout(st.session_state["authenticated"])
            st.session_state["authenticated"] = None
            st.success("Has cerrado sesión exitosamente.")
            st.rerun()  

    else:
        st.error("La sesión ha expirado. Por favor, inicia sesión nuevamente.")
        st.session_state["authenticated"] = None
        st.rerun()  
else:
    login.login_screen()
