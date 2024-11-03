from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["hotel_management"]


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
    db.hoteles.update_one({"hotel_id": hotel_id}, {"$set": updates})

def eliminar_hotel(hotel_id):
    db.hoteles.delete_one({"hotel_id": hotel_id})


def agregar_habitacion(hotel_id, tipo, amenities):
    db.habitaciones.insert_one({
        "hotel_id": hotel_id,
        "tipo": tipo,
        "amenities": amenities,
    })

def obtener_habitaciones():
    return list(db.habitaciones.find())

def modificar_habitacion(habitacion_id, updates):
    db.habitaciones.update_one({"habitacion_id": habitacion_id}, {"$set": updates})

def eliminar_habitacion(habitacion_id):
    db.habitaciones.delete_one({"habitacion_id": habitacion_id})


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
    return db.hoteles.find_one({"hotel_id": hotel_id})

def encontrar_poi_cerca_hotel(hotel_id):
    hotel = db.hoteles.find_one({"hotel_id": hotel_id})
    if hotel:
        return hotel["puntos_de_interés"]

def buscar_habitacion_disponible(hotel_id, fecha_inicio, fecha_salida):
    habitaciones = [h["habitacion_id"] for h in db.habitaciones.find({"hotel_id": hotel_id})]
    reservadas = list(db.reservas.find({
        "habitacion_id": {"$in": habitaciones},
        "$or": [
            {"fecha_inicio": {"$lt": fecha_salida, "$gte": fecha_inicio}},
            {"fecha_salida": {"$gt": fecha_inicio, "$lte": fecha_salida}},
        ]
    }))

    return reservadas


def obtener_amenities_habitacion(habitacion_id):
    habitacion = db.habitaciones.find_one({"habitacion_id": habitacion_id})
    return habitacion["amenities"] if habitacion else None

def obtener_reserva_por_codigo(codigo_reserva):
    return db.reservas.find_one({"codigo_reserva": codigo_reserva})

def obtener_reservas_por_huesped(huesped_id):
    return list(db.reservas.find({"huesped_id": huesped_id}))

def obtener_reservas_por_fecha(hotel_id, fecha):
    return list(db.reservas.find({"habitacion_id": {"$in": [h["habitacion_id"] for h in db.habitaciones.find({"hotel_id": hotel_id})]}, "fecha_inicio": fecha}))

def ver_detalles_huesped(huesped_id):
    return db.huespedes.find_one({"huesped_id": huesped_id})
