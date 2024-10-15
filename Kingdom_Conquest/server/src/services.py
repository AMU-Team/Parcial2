from sqlalchemy.orm import Session
from src.models import Reino, Infraestructura, Evento
from sqlalchemy.orm import joinedload

# Función para crear un nuevo reino
def crear_reino(db: Session, nombre: str) -> Reino:
    reino = Reino(nombre=nombre)
    db.add(reino)
    db.commit()
    db.refresh(reino)
    return reino

# Función para obtener la lista de todos los reinos
def obtener_reinos(db: Session) -> list:
    return db.query(Reino).options(joinedload(Reino.infraestructuras)).all()


# Función para actualizar los datos de un reino
def actualizar_reino(db: Session, reino_id: int, nombre: str) -> Reino:
    reino = db.query(Reino).filter(Reino.id == reino_id).first()
    if not reino:
        raise ValueError("Reino no encontrado")
    
    reino.nombre = nombre
    db.commit()
    db.refresh(reino)
    return reino

# Función para eliminar un reino
def eliminar_reino(db: Session, reino_id: int) -> None:
    reino = db.query(Reino).filter(Reino.id == reino_id).first()
    if not reino:
        raise ValueError("Reino no encontrado")
    
    db.delete(reino)
    db.commit()

# Función para ejecutar una acción sobre un reino
def ejecutar_accion_reino(db: Session, reino_id: int, accion: str, params: dict) -> Reino:
    reino = db.query(Reino).options(joinedload(Reino.infraestructuras)).filter(Reino.id == reino_id).first()
    if not reino:
        raise ValueError("Reino no encontrado")
    
    # Lógica para las acciones del reino
    if accion == "recolectar_recursos":
        recolectar_recursos(reino)
    elif accion == "expandir_territorio":
        expandir_territorio(reino, params.get("costo_oro", 30), params.get("costo_madera", 30))
    elif accion == "construir_infraestructura":
        construir_infraestructura(db, reino, params)
    
    db.commit()
    db.refresh(reino)
    return reino


# Funciones auxiliares de lógica de juego
def recolectar_recursos(reino: Reino) -> None:
    reino.oro += reino.produccion
    reino.madera += reino.produccion

def expandir_territorio(reino: Reino, costo_oro: int, costo_madera: int) -> None:
    if reino.oro >= costo_oro and reino.madera >= costo_madera:
        reino.territorios += 2
        reino.oro -= costo_oro
        reino.madera -= costo_madera

def construir_infraestructura(db: Session, reino: Reino, params: dict) -> None:
    infra = Infraestructura(
        nombre=params["nombre"],
        costo_oro=params["costo_oro"],
        costo_madera=params["costo_madera"],
        aumento_produccion=params["aumento_produccion"],
        aumento_estabilidad=params["aumento_estabilidad"],
        reino_id=reino.id
    )
    reino.oro -= infra.costo_oro
    reino.madera -= infra.costo_madera
    db.add(infra)
