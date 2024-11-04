from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['hotel_management']


puntos_de_interes = [
    {"_id": 0, "nombre": "Museo Nacional de Bellas Artes", "detalles": "Uno de los museos de arte más importantes de Argentina, alberga una gran colección de arte argentino e internacional."},
    {"_id": 1, "nombre": "Cementerio de la Recoleta", "detalles": "Lugar de descanso de muchas figuras históricas y culturales de Argentina, famoso por su arquitectura de mausoleos y esculturas."},
    {"_id": 2, "nombre": "Teatro Colón", "detalles": "Uno de los teatros de ópera más prestigiosos del mundo, reconocido por su acústica y su impresionante arquitectura."},
    {"_id": 3, "nombre": "Puente de la Mujer", "detalles": "Un icónico puente peatonal en Puerto Madero diseñado por Santiago Calatrava, simboliza la modernidad de la ciudad."},
    {"_id": 4, "nombre": "Reserva Ecológica Costanera Sur", "detalles": "Un pulmón verde a orillas del río, ideal para caminatas y observar la naturaleza en medio de la ciudad."},
    {"_id": 5, "nombre": "Centro Histórico", "detalles": "Área que incluye edificios y plazas históricas como Plaza de Mayo, que cuenta con una rica historia y arquitectura colonial."},
    {"_id": 6, "nombre": "Obelisco", "detalles": "Monumento icónico de Buenos Aires ubicado en la Avenida 9 de Julio, símbolo de la ciudad y punto de encuentro popular."},
    {"_id": 7, "nombre": "Plaza de Mayo", "detalles": "Centro político y cultural de Buenos Aires, rodeado de edificios emblemáticos como la Casa Rosada y la Catedral Metropolitana."},
    {"_id": 8, "nombre": "Museo de Arte Latinoamericano de Buenos Aires (MALBA)", "detalles": "Museo que alberga una destacada colección de arte latinoamericano contemporáneo y moderno."},
    {"_id": 9, "nombre": "Jardín Japonés", "detalles": "Un hermoso jardín de estilo japonés en el barrio de Palermo, ideal para relajarse y disfrutar de la cultura japonesa."},
    {"_id": 10, "nombre": "El Rosedal", "detalles": "Parque en Palermo con una gran variedad de rosas, senderos y un lago, es uno de los lugares más hermosos de la ciudad."},
    {"_id": 11, "nombre": "Casa Rosada", "detalles": "Sede del Poder Ejecutivo Nacional, destaca por su color rosado y su relevancia en la historia de Argentina."},
    {"_id": 12, "nombre": "Catedral Metropolitana", "detalles": "Principal iglesia católica de Buenos Aires, alberga los restos del General San Martín, uno de los héroes de la independencia."},
    {"_id": 13, "nombre": "Barrio San Telmo", "detalles": "Uno de los barrios más antiguos de la ciudad, conocido por su ambiente bohemio, ferias de antigüedades y tango."}
]


# Insertar datos en la colección Hotelescls
hoteles_data = [
    {
        "_id": "H1",
        "nombre": "Hotel Alvear",
        "dirección": "Avenida Alvear 1361, Recoleta",
        "teléfono": ["011 4808-2100"],
        "email": "info@alvear.com.ar",
        "puntos_de_interés": [0, 1, 2],  # Museo Nacional de Bellas Artes, Cementerio de la Recoleta, Teatro Colón
        "habitaciones": ["R1", "R2"]
    },
    {
        "_id": "H2",
        "nombre": "Hotel Faena",
        "dirección": "Martha Salotti 445, Puerto Madero",
        "teléfono": ["011 4010-9100"],
        "email": "reservas@faenahotels.com",
        "puntos_de_interés": [3, 4, 5],  # Puente de la Mujer, Reserva Ecológica Costanera Sur, Centro Histórico
        "habitaciones": ["R3", "R4"]
    },
    {
        "_id": "H3",
        "nombre": "Sheraton Buenos Aires",
        "dirección": "Avenida Leandro N. Alem 1200, Microcentro",
        "teléfono": ["011 4318-9000"],
        "email": "info.buenosaires@sheraton.com",
        "puntos_de_interés": [6, 2, 7],  # Obelisco, Teatro Colón, Plaza de Mayo
        "habitaciones": ["R5", "R6"]
    },
    {
        "_id": "H4",
        "nombre": "Palacio Duhau - Park Hyatt Buenos Aires",
        "dirección": "Av. Alvear 1661, Recoleta",
        "teléfono": ["011 5171-1234"],
        "email": "reservas.buenosaires@hyatt.com",
        "puntos_de_interés": [8, 9, 10],  # MALBA, Jardín Japonés, El Rosedal
        "habitaciones": ["R7", "R8"]
    },
    {
        "_id": "H5",
        "nombre": "Hotel Intercontinental",
        "dirección": "Moreno 809, Monserrat",
        "teléfono": ["011 5279-9200"],
        "email": "info.buenosaires@ihg.com",
        "puntos_de_interés": [11, 12, 13],  # Casa Rosada, Catedral Metropolitana, Barrio San Telmo
        "habitaciones": ["R9", "R10"]
    }
]

db.poi.insert_many(puntos_de_interes)

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
