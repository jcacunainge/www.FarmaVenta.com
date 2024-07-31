# app/schemas/cliente.py

from pydantic import BaseModel, Field, EmailStr

class ClienteBase(BaseModel):
    nombre_cliente: str = Field(..., description="Nombre del cliente")
    documento_cliente: str = Field(..., description="Documento del cliente")
    correo_cliente: EmailStr = Field(..., description="Correo electrónico del cliente")
    telefono_cliente: str = Field(..., description="Teléfono del cliente")

class ClienteCrear(ClienteBase):
    pass

class ClienteActualizar(ClienteBase):
    pass

class ClienteLeer(ClienteBase):
    id: str = Field(..., description="ID del cliente")

    class Config:
        orm_mode = True
