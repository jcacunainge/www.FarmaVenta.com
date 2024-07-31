from datetime import datetime, date
from bson import ObjectId
from pymongo.collection import Collection
from app.database.mongoDB_conection import ventas_collection
from app.schemas.ventas import VentaCrear, VentaActualizar
from typing import Any, Dict, List

def obtener_coleccion() -> Collection:
    return ventas_collection

def convertir_fecha_a_datetime(fecha: date) -> datetime:
    return datetime.combine(fecha, datetime.min.time())


def convertir_fecha_a_iso(fecha: date) -> str:
    return fecha.isoformat()

def convertir_iso_a_fecha(fecha_iso: str) -> date:
    return datetime.fromisoformat(fecha_iso).date()

async def crear_venta(venta: VentaCrear) -> Dict[str, Any]:
    coleccion = obtener_coleccion()
    venta_dict = venta.dict()

    # Convertir fechas a formato ISO 8601
    for item in venta_dict.get('itemsVentas', []):
        if 'fecha_vencimiento' in item:
            item['fecha_vencimiento'] = convertir_fecha_a_iso(item['fecha_vencimiento'])
    venta_dict['fecha_venta'] = datetime.now()  # Agregar la fecha de venta
    resultado = await coleccion.insert_one(venta_dict)
    # Convertir _id a string
    venta_dict['_id'] = str(resultado.inserted_id)
    
    return venta_dict


async def actualizar_venta(id_venta: str, venta: VentaActualizar):
    coleccion = obtener_coleccion()
    venta_dict = venta.dict(exclude_unset=True)

    # Convertir fecha_vencimiento en itemsVentas a datetime
    for item in venta_dict.get('itemsVentas', []):
        if 'fecha_vencimiento' in item and isinstance(item['fecha_vencimiento'], date):
            item['fecha_vencimiento'] = convertir_fecha_a_datetime(item['fecha_vencimiento'])

    resultado = await coleccion.update_one(
        {"_id": ObjectId(id_venta)},
        {"$set": venta_dict}
    )
    if resultado.modified_count == 0:
        return None
    return await coleccion.find_one({"_id": ObjectId(id_venta)})



async def obtener_venta_por_id(id_venta: str):
    coleccion = obtener_coleccion()
    venta = await coleccion.find_one({"_id": ObjectId(id_venta)})
    return venta

async def obtener_ventas() -> List[Dict[str, Any]]:
    coleccion = obtener_coleccion()
    cursor = coleccion.find()
    ventas = []
    async for documento in cursor:
        documento['_id'] = str(documento['_id'])
        ventas.append(documento)
    return ventas


async def eliminar_venta(id_venta: str):
    coleccion = obtener_coleccion()
    resultado = await coleccion.delete_one({"_id": ObjectId(id_venta)})
    if resultado.deleted_count == 0:
        return None
    return resultado.deleted_count



async def obtener_ventas_por_fecha(fecha_venta: date) -> List[Dict[str, Any]]:
    coleccion = obtener_coleccion()
    fecha_inicio = datetime.combine(fecha_venta, datetime.min.time())
    fecha_fin = datetime.combine(fecha_venta, datetime.max.time())

    cursor = coleccion.find({"fecha_venta": {"$gte": fecha_inicio, "$lte": fecha_fin}})
    ventas = []
    async for documento in cursor:
        documento['_id'] = str(documento['_id'])
        ventas.append(documento)
    return ventas



