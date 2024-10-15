from sqlalchemy.orm import Session
from src.models import Reino, Infraestructura, Evento

# Función para crear un nuevo reino
def crear_reino(db: Session, nombre: str):
    reino = Reino(nombre=nombre)
    db.add(reino)
    db.commit()
    db.refresh(reino)
    return reino

# Función para obtener la lista de todos los reinos
def obtener_reinos(db: Session):
    reinos = db.query(Reino).all()
    for reino in reinos:
        # Convertir los objetos de infraestructuras en una lista de nombres de infraestructuras
        reino.infraestructuras = [infra.nombre for infra in reino.infraestructuras]
    return reinos

# Función para actualizar los datos de un reino
def actualizar_reino(db: Session, reino_id: int, nombre: str):
    reino = db.query(Reino).filter(Reino.id == reino_id).first()
    if not reino:
        raise HTTPException(status_code=404, detail="Reino no encontrado")
    
    reino.nombre = nombre
    db.commit()
    db.refresh(reino)
    return reino

# Función para eliminar un reino
def eliminar_reino(db: Session, reino_id: int):
    reino = db.query(Reino).filter(Reino.id == reino_id).first()
    if not reino:
        raise HTTPException(status_code=404, detail="Reino no encontrado")
    
    db.delete(reino)
    db.commit()

# Función para ejecutar una acción sobre un reino
def ejecutar_accion_reino(db: Session, reino_id: int, accion: str, params: dict):
    reino = db.query(Reino).filter(Reino.id == reino_id).first()
    if not reino:
        raise HTTPException(status_code=404, detail="Reino no encontrado")
    
    # Lógica para las acciones del reino
    if accion == "recolectar_recursos":
        reino.oro += reino.produccion
        reino.madera += reino.produccion
    elif accion == "expandir_territorio":
        if reino.oro >= params.get("costo_oro", 30) and reino.madera >= params.get("costo_madera", 30):
            reino.territorios += 2
            reino.oro -= params["costo_oro"]
            reino.madera -= params["costo_madera"]
    elif accion == "construir_infraestructura":
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
    
    # Otras acciones pueden agregarse aquí

    db.commit()
    db.refresh(reino)
    return reino
