from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Dict, Optional

class VentaItem(BaseModel):
    codigo: str = Field(..., description="Código del medicamento")
    nombre_medicamento: str = Field(..., description="Nombre del medicamento")
    fabricante: Optional[str] = Field(None, description="Nombre del fabricante")
    fecha_vencimiento: datetime = Field(..., description="Fecha de vencimiento del medicamento")
    cantidad: int = Field(..., description="Cantidad disponible")
    lote: Optional[str] = Field(None, description="Número de lote del medicamento")
    stock: int = Field(..., description="Cantidad en stock")
    precio: float = Field(..., description="Precio del medicamento")
    total: float = Field(..., description="Total de la venta")
    descuento: Optional[float] = Field(None, description="Descuento aplicado")

class Venta(BaseModel):
    id: Optional[str] = Field(None, description="ID de la venta")
    dataVendedor: Dict = Field(..., description="Información del vendedor")
    dataCliente: Dict = Field(..., description="Información del cliente")
    itemsVentas: List[VentaItem] = Field(..., description="Lista de artículos vendidos")
    fecha_venta: Optional[datetime] = Field(None, description="Fecha de la venta")

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat() if isinstance(v, datetime) else None
        }
