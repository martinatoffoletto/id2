from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['hotel_management']

# Insertar datos en la colección Hotelescls
hoteles_data = [
    {
        "_id": "H1",
        "nombre": "Hotel Alvear",
        "dirección": "Avenida Alvear 1361, Recoleta",
        "teléfono": ["011 4808-2100"],
        "email": "info@alvear.com.ar",
        "puntos_de_interés": [
            {"nombre": "Museo Nacional de Bellas Artes", "valor": 10},
            {"nombre": "Cementerio de la Recoleta", "valor": 0},
            {"nombre": "Teatro Colón", "valor": 15}
        ],
        "habitaciones": ["R1", "R2"]
    },
    {
        "_id": "H2",
        "nombre": "Hotel Faena",
        "dirección": "Martha Salotti 445, Puerto Madero",
        "teléfono": ["011 4010-9100"],
        "email": "reservas@faenahotels.com",
        "puntos_de_interés": [
            {"nombre": "Puente de la Mujer", "valor": 0},
            {"nombre": "Reserva Ecológica Costanera Sur", "valor": 0},
            {"nombre": "Centro Histórico", "valor": 5}
        ],
        "habitaciones": ["R3", "R4"]
    },
    {
        "_id": "H3",
        "nombre": "Sheraton Buenos Aires",
        "dirección": "Avenida Leandro N. Alem 1200, Microcentro",
        "teléfono": ["011 4318-9000"],
        "email": "info.buenosaires@sheraton.com",
        "puntos_de_interés": [
            {"nombre": "Obelisco", "valor": 0},
            {"nombre": "Teatro Colón", "valor": 15},
            {"nombre": "Plaza de Mayo", "valor": 0}
        ],
        "habitaciones": ["R5", "R6"]
    },
    {
        "_id": "H4",
        "nombre": "Palacio Duhau - Park Hyatt Buenos Aires",
        "dirección": "Av. Alvear 1661, Recoleta",
        "teléfono": ["011 5171-1234"],
        "email": "reservas.buenosaires@hyatt.com",
        "puntos_de_interés": [
            {"nombre": "Museo de Arte Latinoamericano de Buenos Aires", "valor": 12},
            {"nombre": "Jardín Japonés", "valor": 10},
            {"nombre": "El Rosedal", "valor": 0}
        ],
        "habitaciones": ["R7", "R8"]
    },
    {
        "_id": "H5",
        "nombre": "Hotel Intercontinental",
        "dirección": "Moreno 809, Monserrat",
        "teléfono": ["011 5279-9200"],
        "email": "info.buenosaires@ihg.com",
        "puntos_de_interés": [
            {"nombre": "Casa Rosada", "valor": 0},
            {"nombre": "Catedral Metropolitana", "valor": 0},
            {"nombre": "Barrio San Telmo", "valor": 8}
        ],
        "habitaciones": ["R9", "R10"]
    }

]

db.hoteles.insert_many(hoteles_data)

# Insertar datos en la colección Habitaciones
habitaciones_data = [
    {
        "_id": "R1",
        "hotel_id": "H1",
        "tipo": "Suite Doble",
        "amenities": ["Wi-Fi gratuito", "Desayuno incluido", "Copa de vino de bienvenida"]
    },
    {
        "_id": "R2",
        "hotel_id": "H1",
        "tipo": "Habitación Ejecutiva",
        "amenities": ["Wi-Fi gratuito", "TV por cable", "Productos especiales de tocador"]
    },
    {
        "_id": "R3",
        "hotel_id": "H2",
        "tipo": "Habitación Doble Superior",
        "amenities": ["Wi-Fi gratuito", "Acceso al spa", "Chocolates de bienvenida"]
    },
    {
        "_id": "R4",
        "hotel_id": "H2",
        "tipo": "Suite",
        "amenities": ["Wi-Fi gratuito", "Desayuno incluido", "Copa de champán"]
    },
    {
        "_id": "R5",
        "hotel_id": "H3",
        "tipo": "Habitación Deluxe",
        "amenities": ["Wi-Fi gratuito", "Café de cortesía", "Minibar"]
    }
]

db.habitaciones.insert_many(habitaciones_data)

# Insertar datos en la colección Huéspedes
huespedes_data = [
    {
        "_id": "G1",
        "nombre": "Juan",
        "apellido": "Pérez",
        "teléfonos": ["011 1234-5678"],
        "emails": ["juan.perez@example.com"],
        "dirección": {
            "calle": "Calle Falsa",
            "número": "123",
            "código_postal": "C1000",
            "provincia": "Buenos Aires",
            "país": "Argentina"
        },
        "reservas": ["RS1"]
    },
    {
        "_id": "G2",
        "nombre": "Ana",
        "apellido": "García",
        "teléfonos": ["011 9876-5432"],
        "emails": ["ana.garcia@example.com"],
        "dirección": {
            "calle": "Avenida Siempre Viva",
            "número": "742",
            "código_postal": "C1400",
            "provincia": "Buenos Aires",
            "país": "Argentina"
        },
        "reservas": ["RS2"]
    },
    {
        "_id": "G3",
        "nombre": "Pedro",
        "apellido": "López",
        "teléfonos": ["011 2345-6789"],
        "emails": ["pedro.lopez@example.com"],
        "dirección": {
            "calle": "Calle 1",
            "número": "456",
            "código_postal": "C2000",
            "provincia": "Buenos Aires",
            "país": "Argentina"
        },
        "reservas": ["RS3"]
    },
    {
        "_id": "G4",
        "nombre": "María",
        "apellido": "Rodríguez",
        "teléfonos": ["011 3456-7890"],
        "emails": ["maria.rodriguez@example.com"],
        "dirección": {
            "calle": "Avenida Libertador",
            "número": "1010",
            "código_postal": "C1000",
            "provincia": "Buenos Aires",
            "país": "Argentina"
        },
        "reservas": ["RS4"]
    },
    {
        "_id": "G5",
        "nombre": "Lucía",
        "apellido": "Martínez",
        "teléfonos": ["011 4567-8901"],
        "emails": ["lucia.martinez@example.com"],
        "dirección": {
            "calle": "Calle 2",
            "número": "789",
            "código_postal": "C3000",
            "provincia": "Buenos Aires",
            "país": "Argentina"
        },
        "reservas": ["RS5"]
    }
]

db.huespedes.insert_many(huespedes_data)

# Insertar datos en la colección Reservas
reservas_data = [
    {
        "_id": "RS1",
        "huesped_id": ["G1"],
        "habitacion_id": "R1",
        "codigo_reserva": "C1",
        "fecha_inicio": "2024-11-01",
        "fecha_salida": "2024-11-05",
        "tarifa": "$200"
    },
    {
        "_id": "RS2",
        "huesped_id": ["G2"],
        "habitacion_id": "R3",
        "codigo_reserva": "C2",
        "fecha_inicio": "2024-11-10",
        "fecha_salida": "2024-11-12",
        "tarifa": "$150"
    },
    {
        "_id": "RS3",
        "huesped_id": ["G3"],
        "habitacion_id": "R5",
        "codigo_reserva": "C3",
        "fecha_inicio": "2024-11-15",
        "fecha_salida": "2024-11-20",
        "tarifa": "$180"
    },
    {
        "_id": "RS4",
        "huesped_id": ["G4"],
        "habitacion_id": "R2",
        "codigo_reserva": "C4",
        "fecha_inicio": "2024-11-25",
        "fecha_salida": "2024-11-30",
        "tarifa": "$220"
    },
    {
        "_id": "RS5",
        "huesped_id": ["G5"],
        "habitacion_id": "R4",
        "codigo_reserva": "C5",
        "fecha_inicio": "2024-11-28",
        "fecha_salida": "2024-12-01",
        "tarifa": "$250"
    }
]

db.reservas.insert_many(reservas_data)

# Verificar la inserción de datos
print("Datos insertados correctamente en las colecciones de MongoDB.")
