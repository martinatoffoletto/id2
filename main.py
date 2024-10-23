from pymongo import MongoClient

# Conexion
client = MongoClient('mongodb://localhost:27017/')
db = client['gestion_hoteles']



