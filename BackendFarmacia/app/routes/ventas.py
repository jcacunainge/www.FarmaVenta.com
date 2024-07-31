from fastapi import APIRouter, HTTPException, status
from datetime import datetime, date
from bson import ObjectId
from typing import Any, Dict, List

from app.repositories.ventas import (
    crear_venta,
    actualizar_venta,
    obtener_venta_por_id,
    obtener_ventas,
    eliminar_venta,
    obtener_ventas_por_fecha,
   
)

from app.schemas.ventas import VentaCrear, VentaActualizar, VentaMostrar

router = APIRouter()

@router.post("/", response_model=VentaMostrar)
async def crear_nueva_venta(venta: VentaCrear):
    nueva_venta = await crear_venta(venta)
    if nueva_venta:
        return nueva_venta
    raise HTTPException(status_code=400, detail="Error al crear la venta")

@router.put("/{id_venta}", response_model=VentaMostrar)
async def actualizar_venta_existente(id_venta: str, venta: VentaActualizar):
    venta_actualizada = await actualizar_venta(id_venta, venta)
    if venta_actualizada:
        return venta_actualizada
    raise HTTPException(status_code=404, detail="Venta no encontrada")

@router.get("/{id_venta}", response_model=VentaMostrar)
async def obtener_venta(id_venta: str):
    venta = await obtener_venta_por_id(id_venta)
    if venta:
        return venta
    raise HTTPException(status_code=404, detail="Venta no encontrada")

@router.get("/", response_model=list[VentaMostrar])
async def obtener_todas_las_ventas():
    ventas = await obtener_ventas()
    return ventas

@router.delete("/{id_venta}")
async def eliminar_venta_existente(id_venta: str):
    eliminacion = await eliminar_venta(id_venta)
    if eliminacion:
        return {"mensaje": "Venta eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Venta no encontrada")

@router.get("/ventas/fecha/{fecha_venta}", response_model=List[Any])
async def obtener_ventas_por_fecha_endpoint(fecha_venta: date):
    ventas = await obtener_ventas_por_fecha(fecha_venta)
    if not ventas:
        return []
    return ventas



