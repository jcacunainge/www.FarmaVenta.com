from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.usuario import UsuarioCrear, UsuarioSalida
from app.models.user import UsuarioModelo
from app.repositories.usuario import crear_usuario, obtener_usuario_por_correo

router = APIRouter()

@router.post("/register", response_model=UsuarioModelo)
async def registrar(usuario: UsuarioCrear):
    usuario_existente = await obtener_usuario_por_correo(usuario.correo)
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Correo de usuario ya tomado")
    usuario_modelo = UsuarioModelo(**usuario.dict())
    await crear_usuario(usuario_modelo)
    return usuario_modelo

@router.post("/login", response_model=UsuarioCrear)
async def iniciar_sesion(usuario: UsuarioSalida):
    usuario_existente = await obtener_usuario_por_correo(usuario.correo)
    if not usuario_existente or usuario_existente.contraseña != usuario.contraseña:
        raise HTTPException(status_code=400, detail="Correo de usuario o contraseña inválidos")
    
    # Convertir ObjectId a string
    usuario_dict = usuario_existente.dict(by_alias=True)
    return JSONResponse(
        content={
            "mensaje": "Inicio de sesión exitoso",
            "usuario": usuario_dict
        },
        status_code=200
    )
