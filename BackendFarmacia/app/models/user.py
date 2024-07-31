from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId

class UsuarioModelo(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias='_id')
    nombre_usuario: str
    codigo_usuario: str
    nombre_negocio: str
    dirrecion_negocio: str
    telefono_negocio: str
    correo: EmailStr
    contraseña: str
    es_admin: bool = Field(default=False)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UsuarioCrear(BaseModel):
    nombre_usuario: str
    codigo_usuario: str
    nombre_negocio: str
    dirrecion_negocio: str
    telefono_negocio: str
    contraseña: str
    correo: EmailStr

class UsuarioSalida(BaseModel):
    correo: EmailStr
    contraseña: str
