from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import List, Optional

class ItemVenta(BaseModel):
    codigo: str = Field(..., description="Código del medicamento")
    nombre_medicamento: str = Field(..., description="Nombre del medicamento")
    fabricante: str = Field(..., description="Nombre del fabricante")
    fecha_vencimiento: date = Field(..., description="Fecha de vencimiento del medicamento")
    cantidad: int = Field(..., description="Cantidad vendida")
    lote: Optional[str] = Field(None, description="Número de lote del medicamento")
    stock: int = Field(..., description="Cantidad en stock")
    precio: float = Field(..., description="Precio del medicamento")
    total: float = Field(..., description="Total de la venta del medicamento")
    descuento: Optional[str] = Field(..., description="Descuento aplicado al medicamento")

    class Config:
        orm_mode = True

class DataVendedor(BaseModel):
    nombre_usuario: str = Field(..., description="Nombre del usuario vendedor")
    codigo_usuario: str = Field(..., description="Código del usuario vendedor")
    nombre_negocio: str = Field(..., description="Nombre del negocio")
    dirrecion_negocio: str = Field(..., description="Dirección del negocio")
    telefono_negocio: str = Field(..., description="Teléfono del negocio")

    class Config:
        orm_mode = True

class DataCliente(BaseModel):
    nombre_cliente: str = Field(..., description="Nombre del cliente")
    documento_cliente: str = Field(..., description="Documento de identificación del cliente")
    telefono_cliente: str = Field(..., description="Teléfono del cliente")
    correo_cliente: Optional[str] = Field(None, description="Correo electrónico del cliente")

    class Config:
        orm_mode = True

class VentaBase(BaseModel):
    dataVendedor: DataVendedor = Field(..., description="Datos del vendedor")
    dataCliente: DataCliente = Field(..., description="Datos del cliente")
    itemsVentas: List[ItemVenta] = Field(..., description="Lista de productos vendidos")

    class Config:
        orm_mode = True

class VentaCrear(VentaBase):
    pass

class VentaActualizar(VentaBase):
    pass

class VentaMostrar(VentaBase):
    id: str = Field(..., alias="_id", description="ID de la venta")
    fecha_venta: datetime = Field(..., description="Fecha en la que se realizó la venta")
