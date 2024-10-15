from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database_connection import SessionLocal
from src.models import Reino, Infraestructura, Evento
from src.services import crear_reino, obtener_reinos, actualizar_reino, eliminar_reino, ejecutar_accion_reino
from pydantic import BaseModel

# Definición del router de FastAPI
router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelos para requests y responses

class ReinoCreateRequest(BaseModel):
    nombre: str

class ReinoResponse(BaseModel):
    id: int
    nombre: str
    oro: int
    madera: int
    territorios: int
    produccion: int
    estabilidad: int
    infraestructuras: List[str] = []
    eventos: List[str] = []

    class Config:
        orm_mode = True

class InfraestructuraRequest(BaseModel):
    nombre: str
    costo_oro: int
    costo_madera: int
    aumento_produccion: int
    aumento_estabilidad: int

class AccionReinoRequest(BaseModel):
    accion: str
    params: dict = {}

# Endpoints de la API

@router.post("/reinos/", response_model=ReinoResponse)
def crear_nuevo_reino(reino: ReinoCreateRequest, db: Session = Depends(get_db)):
    return crear_reino(db=db, nombre=reino.nombre)

@router.get("/reinos/", response_model=List[ReinoResponse])
def listar_reinos(db: Session = Depends(get_db)):
    return obtener_reinos(db)

@router.put("/reinos/{reino_id}", response_model=ReinoResponse)
def actualizar_datos_reino(reino_id: int, reino: ReinoCreateRequest, db: Session = Depends(get_db)):
    return actualizar_reino(db, reino_id, reino.nombre)

@router.delete("/reinos/{reino_id}")
def borrar_reino(reino_id: int, db: Session = Depends(get_db)):
    eliminar_reino(db, reino_id)
    return {"message": "Reino eliminado"}

@router.post("/reinos/{reino_id}/accion")
def realizar_accion_reino(reino_id: int, accion: AccionReinoRequest, db: Session = Depends(get_db)):
    return ejecutar_accion_reino(db, reino_id, accion.accion, accion.params)
