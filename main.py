from pymongo import MongoClient
import redis
import streamlit as st

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["hotel_management"]

#Conexion a redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


def agregar_hotel(nombre, direccion, telefonos, email, puntos_de_interes):
    db.hoteles.insert_one({
        "nombre": nombre,
        "dirección": direccion,
        "teléfono": telefonos,
        "email": email,
        "puntos_de_interés": puntos_de_interes,
        "habitaciones": []
    })

def obtener_hoteles():
    return list(db.hoteles.find())


def modificar_hotel(hotel_id, updates):
    db.hoteles.update_one({"_id": hotel_id}, {"$set": updates})

def eliminar_hotel(hotel_id):
    db.habitaciones.delete_many({"hotel_id": hotel_id})
    db.hoteles.delete_one({"_id": hotel_id})


def agregar_habitacion(hotel_id, tipo, amenities):
    result = db.habitaciones.insert_one({
        "hotel_id": hotel_id,
        "tipo": tipo,
        "amenities": amenities,
    })
    
    habitacion_id = result.inserted_id
    
    db.hoteles.update_one(
        {"_id": hotel_id},
        {"$push": {"habitaciones": habitacion_id}}
    )

def obtener_habitaciones():
    return list(db.habitaciones.find())

def modificar_habitacion(habitacion_id, updates):
    db.habitaciones.update_one({"_id": habitacion_id}, {"$set": updates})

def eliminar_habitacion(habitacion_id):
    habitacion = db.habitaciones.find_one({"_id": habitacion_id})
    if habitacion:
        hotel_id = habitacion["hotel_id"]
    
        db.hoteles.update_one(
            {"_id": hotel_id},
            {"$pull": {"habitaciones": habitacion_id}}
        )
        
        db.habitaciones.delete_one({"_id": habitacion_id})


def agregar_huesped( nombre, apellido, telefonos, emails, direccion):
    db.huespedes.insert_one({
        "nombre": nombre,
        "apellido": apellido,
        "teléfonos": telefonos,
        "emails": emails,
        "dirección": direccion,
        "reservas": []
    })

def obtener_huespedes():
    return list(db.huespedes.find())



def agregar_reserva( huesped_id, habitacion_id, codigo_reserva, fecha_inicio, fecha_salida, tarifa):
    db.reservas.insert_one({
        "huesped_id": huesped_id, # es una lista de huespedes
        "habitacion_id": habitacion_id,
        "codigo_reserva": codigo_reserva,
        "fecha_inicio": fecha_inicio,
        "fecha_salida": fecha_salida,
        "tarifa": tarifa
    })

def obtener_reservas():
    return list(db.reservas.find())


def buscar_hoteles_cerca_poi(poi):
    return list(db.hoteles.find({"puntos_de_interés": poi}))

def obtener_info_hotel(hotel_id):
    return db.hoteles.find_one({"_id": hotel_id})

def encontrar_poi_cerca_hotel(hotel_id):
    hotel = db.hoteles.find_one({"_id": hotel_id})
    if hotel:
        return hotel["puntos_de_interés"]

def buscar_habitacion_disponible(hotel_id, fecha_inicio, fecha_salida):
    habitaciones = list(db.habitaciones.find({"hotel_id": hotel_id}))
    ids_habitaciones = [h["_id"] for h in habitaciones]
    reservadas = list(db.reservas.find({
        "habitacion_id": {"$in": ids_habitaciones},
        "$or": [
            {"fecha_inicio": {"$lte": fecha_salida, "$gte": fecha_inicio}},
            {"fecha_salida": {"$gte": fecha_inicio, "$lte": fecha_salida}},
        ]
    }))

    ids_habitaciones_reservadas = {reserva["habitacion_id"] for reserva in reservadas}
    habitaciones_disponibles = [habitacion for habitacion in habitaciones if habitacion["_id"] not in ids_habitaciones_reservadas]

    return habitaciones_disponibles


def obtener_amenities_habitacion(habitacion_id):
    habitacion = db.habitaciones.find_one({"_id": habitacion_id})
    return habitacion["amenities"] if habitacion else None

def obtener_reserva_por_codigo(codigo_reserva):
    return db.reservas.find_one({"codigo_reserva": codigo_reserva})

def obtener_reservas_por_huesped(huesped_id):
    return list(db.reservas.find({"huesped_id": huesped_id}))

def obtener_reservas_por_fecha(hotel_id, fecha):
    return list(db.reservas.find({"habitacion_id": {"$in": [h["habitacion_id"] for h in db.habitaciones.find({"hotel_id": hotel_id})]}, "fecha_inicio": fecha}))

def ver_detalles_huesped(huesped_id):
    return db.huespedes.find_one({"_id": huesped_id})


#Inicio session

def authenticate_user(username, password):
    user = db.users.find_one({"user": username})
    if user and user["password"] == password:
        return True
    return False

# Función para iniciar sesión
def login(username, password):
    if authenticate_user(username, password):
        redis_client.setex(username, 3600, "logged_in")  # Sesión expira en 1 hora
        return True
    return False

# Función para verificar si el usuario está autenticado
def is_authenticated(username):
    return redis_client.get(username) == "logged_in"

# Función para cerrar sesión
def logout(username):
    redis_client.delete(username)


def verificar_conexion_redis():
    try:
        # Prueba de conexión: guardar un valor temporal
        redis_client.set("test_connection", "success", ex=5)
        # Recuperar el valor para confirmar
        result = redis_client.get("test_connection")
        
        if result == "success":
            print("Conexión a Redis exitosa.")
            return True
        else:
            print("Error en la prueba de conexión a Redis.")
            return False
    except redis.ConnectionError as e:
        print(f"Error de conexión a Redis: {e}")
        return False


