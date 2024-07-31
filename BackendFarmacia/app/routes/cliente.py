# app/routes/cliente.py

from fastapi import APIRouter, HTTPException, status
from app.schemas.cliente import ClienteCrear, ClienteActualizar, ClienteLeer
from app.repositories.cliente import (
    crear_cliente,
    leer_cliente,
    leer_cliente_todo,
    actualizar_cliente,
    eliminar_cliente
)

router = APIRouter()

@router.post('/', response_model=ClienteLeer, status_code=status.HTTP_201_CREATED)
async def crear_cliente_ruta(cliente: ClienteCrear):
    return await crear_cliente(cliente)

@router.get('/{documento_cliente}', response_model=ClienteLeer, status_code=status.HTTP_200_OK)
async def leer_cliente_ruta(documento_cliente: str):
    cliente = await leer_cliente(documento_cliente)
    if not cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
    return cliente

@router.get('/', response_model=list[ClienteLeer], status_code=status.HTTP_200_OK)
async def leer_todos_clientes_ruta():
    return await leer_cliente_todo()

@router.put('/{documento_cliente}', response_model=ClienteLeer, status_code=status.HTTP_200_OK)
async def actualizar_cliente_ruta(documento_cliente: str, cliente: ClienteActualizar):
    cliente_actualizado = await actualizar_cliente(documento_cliente, cliente)
    if not cliente_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
    return cliente_actualizado

@router.delete('/{documento_cliente}', status_code=status.HTTP_200_OK)
async def eliminar_cliente_ruta(documento_cliente: str):
    result = await eliminar_cliente(documento_cliente)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
    return {"detail": "Cliente eliminado exitosamente"}
