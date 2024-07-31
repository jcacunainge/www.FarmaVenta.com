# app/repositories/cliente.py

from pymongo.collection import Collection
from app.schemas.cliente import ClienteCrear, ClienteActualizar
from app.database.mongoDB_conection import database
from datetime import datetime

def obtener_coleccion() -> Collection:
    return database.get_collection('clientes')

def convertir_id(documento):
    documento["id"] = str(documento.pop("_id"))
    return documento

async def crear_cliente(cliente: ClienteCrear):
    coleccion = obtener_coleccion()
    cliente_dict = cliente.dict()
    resultado = await coleccion.insert_one(cliente_dict)
    cliente_creado = await coleccion.find_one({"_id": resultado.inserted_id})
    return convertir_id(cliente_creado)

async def actualizar_cliente(documento_cliente: str, cliente: ClienteActualizar):
    coleccion = obtener_coleccion()
    cliente_dict = cliente.dict(exclude_unset=True)
    resultado = await coleccion.update_one(
        {"documento_cliente": documento_cliente},
        {"$set": cliente_dict}
    )
    if resultado.matched_count == 0:
        return None
    cliente_actualizado = await coleccion.find_one({"documento_cliente": documento_cliente})
    return convertir_id(cliente_actualizado)

async def leer_cliente(documento_cliente: str):
    coleccion = obtener_coleccion()
    cliente = await coleccion.find_one({"documento_cliente": documento_cliente})
    if cliente:
        return convertir_id(cliente)
    return None

async def leer_cliente_todo():
    coleccion = obtener_coleccion()
    cursor = coleccion.find()
    clientes = []
    async for documento in cursor:
        clientes.append(convertir_id(documento))
    return clientes

async def eliminar_cliente(documento_cliente: str):
    coleccion = obtener_coleccion()
    resultado = await coleccion.delete_one({"documento_cliente": documento_cliente})
    return resultado.deleted_count > 0
