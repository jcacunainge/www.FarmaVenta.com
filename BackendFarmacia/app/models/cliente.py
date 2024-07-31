# app/clientes/models.py

from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional

class ClienteBase(BaseModel):
    nombre_cliente: str = Field(..., description="Nombre del cliente")
    documento_cliente: str = Field(..., description="Documento del cliente")
    correo_cliente: EmailStr = Field(..., description="Correo electrónico del cliente")
    telefono_cliente: str = Field(..., description="Teléfono del cliente")

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(ClienteBase):
    pass

class ClienteDB(ClienteBase):
    id: Optional[ObjectId] = Field(None, alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
