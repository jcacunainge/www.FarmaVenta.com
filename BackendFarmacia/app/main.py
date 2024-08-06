from fastapi import FastAPI
from app.routes import medicamento,usuario,cliente,ventas
from fastapi.middleware.cors import CORSMiddleware

from app.documentation.api_docs import (
    tags_metadata as medicamentos_tags_metadata,
)
combined_tags_metadata = []

combined_tags_metadata.extend(medicamentos_tags_metadata)
app_config = {
    "title": "BACKEND FARMACIA",
    "description": "Backend Farmacia 1.0 FastAPI (Python)",
    "version": "v1.0",
    "openapi_tags": combined_tags_metadata,
}

app = FastAPI(**app_config)


# Configura los orígenes permitidos
origins = [
    "https://www-farmaventa-com-1.onrender.com/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(    
    medicamento.router, 
    prefix="/api/v1/medicamentos", 
    tags=["MEDICAMENTOS"]
)
app.include_router(
    usuario.router, 
    prefix="/api/v1/usuario", 
    tags=["USUARIO"]
)
app.include_router(
    cliente.router, 
    prefix="/api/v1/clientes", 
    tags=["CLIENTES"]
)

app.include_router(
    ventas.router, 
    prefix="/api/v1/ventas", 
    tags=["VENTAS"]
)

@app.get("/")
def read_root():
    return {"Hello": "World"}
