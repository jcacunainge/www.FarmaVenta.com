from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class MedicamentoCrear(BaseModel):
    codigo: str = Field(..., description="Código del medicamento")
    nombre_medicamento: str = Field(..., description="Nombre del medicamento")
    fabricante: Optional[str] = Field(None, description="Nombre del fabricante")
    fecha_vencimiento: date = Field(..., description="Fecha de vencimiento del medicamento")
    cantidad: int = Field(..., description="Cantidad disponible")
    lote: Optional[str] = Field(None, description="Número de lote del medicamento")
    stock: int = Field(..., description="Cantidad en stock")
    precio: float = Field(..., description="Precio del medicamento")

    class Config:
        orm_mode = True

class MedicamentoActualizar(BaseModel):
    nombre_medicamento: Optional[str] = Field(None, description="Nombre del medicamento")
    fabricante: Optional[str] = Field(None, description="Nombre del fabricante")
    fecha_vencimiento: Optional[date] = Field(None, description="Fecha de vencimiento del medicamento")
    cantidad: Optional[int] = Field(None, description="Cantidad disponible")
    lote: Optional[str] = Field(None, description="Número de lote del medicamento")
    stock: Optional[int] = Field(None, description="Cantidad en stock")
    precio: Optional[float] = Field(None, description="Precio del medicamento")

    class Config:
        orm_mode = True

class MedicamentoTodo(MedicamentoCrear):
    pass
