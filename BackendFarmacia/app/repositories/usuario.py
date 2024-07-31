from app.database.mongoDB_conection import users_collection
from app.models.user import UsuarioModelo
from bson import ObjectId

async def crear_usuario(usuario: UsuarioModelo):
    resultado = await users_collection.insert_one(usuario.dict(by_alias=True))
    return str(resultado.inserted_id)

async def obtener_usuario_por_correo(correo: str):
    usuario = await users_collection.find_one({"correo": correo})
    if usuario:
        usuario['_id'] = str(usuario['_id'])  # Convertir ObjectId a str
        return UsuarioModelo(**usuario)
    return None

async def obtener_usuario_por_id(usuario_id: str):
    usuario = await users_collection.find_one({"_id": ObjectId(usuario_id)})
    if usuario:
        usuario['_id'] = str(usuario['_id'])  # Convertir ObjectId a str
        return UsuarioModelo(**usuario)
    return None
