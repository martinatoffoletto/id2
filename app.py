import streamlit as st
from hotel_management import hotels, guests, reservations, rooms, login, poi

from main import (
logout,is_authenticated
)


def main_app():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = None

    if st.session_state["authenticated"]:
        if is_authenticated(st.session_state["authenticated"]):
            st.title("Gestion de Cadena de Hoteles")

            menu = ["Hoteles", "Habitaciones", "Huéspedes", "Reservas","Puntos de Interes"]
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
            elif choice=="Puntos de Interes":
                poi.manage_poi()
            
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

main_app()