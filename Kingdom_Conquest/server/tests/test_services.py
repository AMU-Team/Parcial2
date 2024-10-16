import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session 
from src.models import Base, Reino, Infraestructura, Evento
from src.services import crear_reino, obtener_reinos, actualizar_reino, eliminar_reino, ejecutar_accion_reino, construir_infraestructura
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Configuración de base de datos para pruebas (SQLite en memoria)
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture para la sesión de base de datos
@pytest.fixture(scope="function")
def db_session():
    # Crear las tablas en la base de datos
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    # Cerrar sesión y eliminar las tablas después de la prueba
    session.close()
    Base.metadata.drop_all(bind=engine)

# Pruebas unitarias para los servicios

def test_crear_reino(db_session):
    # Crear un nuevo reino
    reino = crear_reino(db=db_session, nombre="Reino A")
    
    # Verificar que el reino fue creado correctamente
    assert reino.nombre == "Reino A"
    assert reino.oro == 100
    assert reino.madera == 100
    assert reino.territorios == 5
    assert reino.produccion == 20
    assert reino.estabilidad == 100

def test_obtener_reinos(db_session):
    # Crear dos reinos para probar la obtención de todos los reinos
    crear_reino(db=db_session, nombre="Reino A")
    crear_reino(db=db_session, nombre="Reino B")
    
    reinos = obtener_reinos(db=db_session)
    
    # Verificar que se obtuvieron ambos reinos
    assert len(reinos) == 2
    assert reinos[0].nombre == "Reino A"
    assert reinos[1].nombre == "Reino B"

def test_actualizar_reino(db_session):
    # Crear un reino y luego actualizar su nombre
    reino = crear_reino(db=db_session, nombre="Reino A")
    reino_actualizado = actualizar_reino(db=db_session, reino_id=reino.id, nombre="Nuevo Reino A")
    
    # Verificar que el nombre se actualizó correctamente
    assert reino_actualizado.nombre == "Nuevo Reino A"

def test_eliminar_reino(db_session):
    # Crear un reino y luego eliminarlo
    reino = crear_reino(db=db_session, nombre="Reino A")
    eliminar_reino(db=db_session, reino_id=reino.id)
    
    # Verificar que el reino fue eliminado correctamente
    reinos = obtener_reinos(db=db_session)
    assert len(reinos) == 0

def test_ejecutar_accion_reino_recolectar_recursos(db_session):
    # Crear un reino y recolectar recursos
    reino = crear_reino(db=db_session, nombre="Reino A")
    ejecutar_accion_reino(db=db_session, reino_id=reino.id, accion="recolectar_recursos", params={})
    
    # Verificar que los recursos fueron recolectados correctamente
    assert reino.oro == 120  # Producción inicial es 20
    assert reino.madera == 120

def test_ejecutar_accion_reino_expandir_territorio(db_session):
    # Crear un reino y expandir su territorio
    reino = crear_reino(db=db_session, nombre="Reino A")
    ejecutar_accion_reino(db=db_session, reino_id=reino.id, accion="expandir_territorio", params={"costo_oro": 30, "costo_madera": 30})
    
    # Verificar que el territorio se expandió y los recursos se descontaron
    assert reino.territorios == 7  # Aumentó en 2 territorios
    assert reino.oro == 70  # Descontó 30 de oro
    assert reino.madera == 70  # Descontó 30 de madera

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
    db.commit()  # Este commit guarda los cambios en la base de datos
    db.refresh(reino)  # Actualiza el objeto 'reino' en la sesión para reflejar los cambios en la base de datos
