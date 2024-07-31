from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://jcacunainge:n01TQymZHBHFL276@cluster0.2e2ovc3.mongodb.net/?retryWrites=true&w=majority"

client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("¡Se realizó el ping a tu implementación. Te has conectado exitosamente a MongoDB!")
except Exception as e:
    print(e)

database = client.get_database("farmacia")
users_collection = database.get_collection("users")
ventas_collection = database.get_collection("ventas")