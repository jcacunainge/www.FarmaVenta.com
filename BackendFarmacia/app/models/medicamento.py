from sqlalchemy import Column, String, text, Integer, Date, Float # noqa: F401
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class MedicamentoModel(Base):
    codigo = Column(String, primary_key=True, nullable=False, comment="Código del medicamento")
    nombre_medicamento = Column(String, nullable=False, comment="Nombre del medicamento")
    fabricante = Column(String, nullable=True, comment="Nombre del fabricante")
    fecha_vencimiento = Column(Date, nullable=False, comment="Fecha de vencimiento del medicamento")
    cantidad = Column(Integer, nullable=False, comment="Cantidad disponible")
    lote = Column(String, nullable=True, comment="Número de lote del medicamento")
    stock = Column(Integer, nullable=False, comment="Cantidad en stock")
    precio = Column(Float, nullable=False, comment="Precio del medicamento")

