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
class ResetResponse(BaseModel):
    message: str

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
    try:
        nuevo_reino = crear_reino(db=db, nombre=reino.nombre)
        return ReinoResponse(
            id=nuevo_reino.id,
            nombre=nuevo_reino.nombre,
            oro=nuevo_reino.oro,
            madera=nuevo_reino.madera,
            territorios=nuevo_reino.territorios,
            produccion=nuevo_reino.produccion,
            estabilidad=nuevo_reino.estabilidad,
            infraestructuras=[infra.nombre for infra in nuevo_reino.infraestructuras],
            eventos=[evento.tipo_evento for evento in nuevo_reino.eventos]
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/reinos/", response_model=List[ReinoResponse])
def listar_reinos(db: Session = Depends(get_db)):
    reinos = obtener_reinos(db)
    return [
        ReinoResponse(
            id=r.id,
            nombre=r.nombre,
            oro=r.oro,
            madera=r.madera,
            territorios=r.territorios,
            produccion=r.produccion,
            estabilidad=r.estabilidad,
            infraestructuras=[infra.nombre for infra in r.infraestructuras],
            eventos=[evento.tipo_evento for evento in r.eventos]
        ) for r in reinos
    ]


@router.put("/reinos/{reino_id}", response_model=ReinoResponse)
def actualizar_datos_reino(reino_id: int, reino: ReinoCreateRequest, db: Session = Depends(get_db)):
    try:
        reino_actualizado = actualizar_reino(db, reino_id, reino.nombre)
        return ReinoResponse(
            id=reino_actualizado.id,
            nombre=reino_actualizado.nombre,
            oro=reino_actualizado.oro,
            madera=reino_actualizado.madera,
            territorios=reino_actualizado.territorios,
            produccion=reino_actualizado.produccion,
            estabilidad=reino_actualizado.estabilidad,
            infraestructuras=[infra.nombre for infra in reino_actualizado.infraestructuras],
            eventos=[evento.tipo_evento for evento in reino_actualizado.eventos]
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/reinos/{reino_id}")
def borrar_reino(reino_id: int, db: Session = Depends(get_db)):
    try:
        eliminar_reino(db, reino_id)
        return {"message": "Reino eliminado"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/reinos/{reino_id}/accion", response_model=ReinoResponse)
def realizar_accion_reino(reino_id: int, accion: AccionReinoRequest, db: Session = Depends(get_db)):
    try:
        reino_actualizado = ejecutar_accion_reino(db, reino_id, accion.accion, accion.params)
        return ReinoResponse(
            id=reino_actualizado.id,
            nombre=reino_actualizado.nombre,
            oro=reino_actualizado.oro,
            madera=reino_actualizado.madera,
            territorios=reino_actualizado.territorios,
            produccion=reino_actualizado.produccion,
            estabilidad=reino_actualizado.estabilidad,
            infraestructuras=[infra.nombre for infra in reino_actualizado.infraestructuras],
            eventos=[evento.tipo_evento for evento in reino_actualizado.eventos]
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/reset")
def reset_game(db: Session = Depends(get_db)):
    db.query(Evento).delete()
    db.query(Infraestructura).delete()
    db.query(Reino).delete()
    db.commit()
    return {"message": "Juego reiniciado"}
