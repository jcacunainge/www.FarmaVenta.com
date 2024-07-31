# app/routes/medicamento_rutas.py

from fastapi import APIRouter, HTTPException, status
from app.schemas.medicamento import MedicamentoCrear, MedicamentoActualizar, MedicamentoTodo
from app.repositories.medicamento import (
    crear_medicamento,
    leer_medicamento,
    leer_medicamento_todo,
    actualizar_medicamento,
    eliminar_medicamento
)

router = APIRouter()

@router.post('/', response_model=MedicamentoTodo, status_code=status.HTTP_201_CREATED)
async def crear_medicamento_ruta(medicamento: MedicamentoCrear):
    return await crear_medicamento(medicamento)

@router.get('/{codigo}', response_model=MedicamentoTodo, status_code=status.HTTP_200_OK)
async def leer_medicamento_ruta(codigo: str):
    item_db = await leer_medicamento(codigo)
    if item_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Medicamento no encontrado')
    return item_db

@router.get('/', response_model=list[MedicamentoTodo], status_code=status.HTTP_200_OK)
async def leer_todos_medicamentos_ruta():
    return await leer_medicamento_todo()

@router.put('/{codigo}', response_model=MedicamentoTodo, status_code=status.HTTP_200_OK)
async def actualizar_medicamento_ruta(codigo: str, medicamento: MedicamentoActualizar):
    item_db = await actualizar_medicamento(codigo, medicamento)
    if item_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Medicamento no encontrado')
    return item_db

@router.delete('/{codigo}', status_code=status.HTTP_200_OK)
async def eliminar_medicamento_ruta(codigo: str):
    resultado = await eliminar_medicamento(codigo)
    if resultado is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Medicamento no encontrado')
    return {"detalle": "Medicamento eliminado exitosamente"}
