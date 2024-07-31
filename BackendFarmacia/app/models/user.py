# app/models/user.py

from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, field):
        if isinstance(v, ObjectId):
            return v
        if isinstance(v, str) and ObjectId.is_valid(v):
            return ObjectId(v)
        raise ValueError('ObjectId inválido')

    @classmethod
    def __get_pydantic_json_schema__(cls, schema, field):
        schema.update(type='string')
        return schema

class UsuarioModelo(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
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
