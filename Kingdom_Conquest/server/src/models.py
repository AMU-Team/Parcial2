from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from src.database_connection import Base

# Modelo de Reino
class Reino(Base):
    __tablename__ = "reinos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    oro = Column(Integer, default=100)
    madera = Column(Integer, default=100)
    territorios = Column(Integer, default=5)
    produccion = Column(Integer, default=20)
    estabilidad = Column(Integer, default=100)

    # Relación con Infraestructuras
    infraestructuras = relationship("Infraestructura", back_populates="reino", lazy='joined')

    # Relación con Eventos (historial de eventos del reino)
    eventos = relationship("Evento", back_populates="reino")

    # Relación con Tierras (agregar la relación)
    tierras = relationship("Tierra", back_populates="reino")

# Modelo de Infraestructura
class Infraestructura(Base):
    __tablename__ = "infraestructuras"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    costo_oro = Column(Integer, default=0)
    costo_madera = Column(Integer, default=0)
    aumento_produccion = Column(Integer, default=0)
    aumento_estabilidad = Column(Integer, default=0)

    # Foreign key para asociar infraestructuras con un reino
    reino_id = Column(Integer, ForeignKey('reinos.id'))
    reino = relationship("Reino", back_populates="infraestructuras")


# Modelo de Evento
class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    tipo_evento = Column(String, index=True)
    descripcion = Column(String)

    # Impacto del evento en los recursos y estabilidad
    impacto_oro = Column(Integer, default=0)
    impacto_madera = Column(Integer, default=0)
    impacto_territorios = Column(Integer, default=0)
    impacto_estabilidad = Column(Integer, default=0)

    # Foreign key para asociar eventos con un reino
    reino_id = Column(Integer, ForeignKey('reinos.id'))
    reino = relationship("Reino", back_populates="eventos")


# Modelo de Tierras (relación agregada correctamente)
class Tierra(Base):
    __tablename__ = "tierras"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    costo_oro = Column(Integer, default=0)
    costo_madera = Column(Integer, default=0)

    # Foreign key para asociar tierras con un reino
    reino_id = Column(Integer, ForeignKey('reinos.id'))
    reino = relationship("Reino", back_populates="tierras")
