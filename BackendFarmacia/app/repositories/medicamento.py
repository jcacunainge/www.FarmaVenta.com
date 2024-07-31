# app/repositories/medicamento.py

from pymongo.collection import Collection
from app.schemas.medicamento import MedicamentoCrear, MedicamentoActualizar
from app.database.mongoDB_conection import database
from datetime import datetime, date

def obtener_coleccion() -> Collection:
    return database.get_collection('medicamentos')

def convertir_fecha_a_iso(fecha: date) -> str:
    return fecha.isoformat()

def convertir_iso_a_fecha(fecha_iso: str) -> date:
    return datetime.fromisoformat(fecha_iso).date()

async def crear_medicamento(medicamento: MedicamentoCrear):
    coleccion = obtener_coleccion()
    medicamento_dict = medicamento.dict()
    
    # Convertir la fecha a formato ISO 8601
    if 'fecha_vencimiento' in medicamento_dict:
        medicamento_dict['fecha_vencimiento'] = convertir_fecha_a_iso(medicamento_dict['fecha_vencimiento'])
    
    resultado = await coleccion.insert_one(medicamento_dict)
    return await coleccion.find_one({"_id": resultado.inserted_id})

async def actualizar_medicamento(codigo: str, medicamento: MedicamentoActualizar):
    coleccion = obtener_coleccion()
    medicamento_dict = medicamento.dict(exclude_unset=True)
    
    # Convertir la fecha a formato ISO 8601
    if 'fecha_vencimiento' in medicamento_dict:
        medicamento_dict['fecha_vencimiento'] = convertir_fecha_a_iso(medicamento_dict['fecha_vencimiento'])
    
    resultado = await coleccion.update_one(
        {"codigo": codigo},
        {"$set": medicamento_dict}
    )
    if resultado.modified_count == 0:
        return None
    return await coleccion.find_one({"codigo": codigo})


async def leer_medicamento(codigo: str):
    coleccion = obtener_coleccion()
    medicamento = await coleccion.find_one({"codigo": codigo})
    if medicamento and 'fecha_vencimiento' in medicamento:
        medicamento['fecha_vencimiento'] = convertir_iso_a_fecha(medicamento['fecha_vencimiento'])
    
    return medicamento

async def leer_medicamento_todo():
    coleccion = obtener_coleccion()
    cursor = coleccion.find()
    medicamentos = []
    async for documento in cursor:
        if 'fecha_vencimiento' in documento:
            documento['fecha_vencimiento'] = convertir_iso_a_fecha(documento['fecha_vencimiento'])
        medicamentos.append(documento)
    return medicamentos


async def eliminar_medicamento(codigo: str):
    coleccion = obtener_coleccion()
    resultado = await coleccion.delete_one({"codigo": codigo})
    if resultado.deleted_count == 0:
        return None
    return resultado.deleted_count
