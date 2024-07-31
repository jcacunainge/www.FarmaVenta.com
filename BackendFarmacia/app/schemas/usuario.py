from pydantic import BaseModel, EmailStr

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
