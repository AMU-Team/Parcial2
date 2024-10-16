import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from src.models import Base, Reino, Infraestructura, Evento, Tierra
from src.routes import get_db

# Configurar la base de datos en memoria para pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"  # Utilizando SQLite en memoria
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture para la base de datos de prueba con transacciones
@pytest.fixture(scope="function")
def test_db():
    Base.metadata.create_all(bind=engine)  # Crear las tablas antes de la prueba
    db = TestingSessionLocal()
    try:
        yield db  # Proporciona la base de datos para las pruebas
    finally:
        db.rollback()  # Hacer rollback después de cada prueba
        Base.metadata.drop_all(bind=engine)  # Limpiar las tablas después de cada prueba
        db.close()

# Test para verificar que las tablas se crearon correctamente
def test_create_tables(test_db):
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    # Verificar que las tablas se crearon correctamente
    assert "reinos" in tables
    assert "infraestructuras" in tables
    assert "eventos" in tables
    assert "tierras" in tables

# Test para verificar la relación entre reino e infraestructura
def test_reino_infraestructura_relationship(test_db):
    # Crear un nuevo reino
    reino = Reino(nombre="Reino A", oro=200, madera=150)
    test_db.add(reino)
    test_db.commit()

    # Crear una infraestructura y asignarla al reino
    infraestructura = Infraestructura(nombre="Granero", costo_oro=50, reino=reino)
    test_db.add(infraestructura)
    test_db.commit()

    # Verificar que la infraestructura está asociada correctamente al reino
    assert infraestructura.reino_id == reino.id
    assert infraestructura.nombre == "Granero"

    # Verificar que el reino tiene la infraestructura asociada
    assert len(reino.infraestructuras) == 1
    assert reino.infraestructuras[0].nombre == "Granero"

# Test para verificar la relación entre reino y tierras
def test_reino_tierra_relationship(test_db):
    # Crear un nuevo reino
    reino = Reino(nombre="Reino B", oro=150, madera=100)
    test_db.add(reino)
    test_db.commit()

    # Crear una tierra y asignarla al reino
    tierra = Tierra(nombre="Valle", costo_oro=30, costo_madera=20, reino=reino)
    test_db.add(tierra)
    test_db.commit()

    # Verificar que la tierra está asociada correctamente al reino
    assert tierra.reino_id == reino.id
    assert tierra.nombre == "Valle"

    # Verificar que el reino tiene la tierra asociada
    assert len(reino.tierras) == 1
    assert reino.tierras[0].nombre == "Valle"

# Test para verificar la relación entre reino y eventos
def test_reino_evento_relationship(test_db):
    # Crear un nuevo reino
    reino = Reino(nombre="Reino C", oro=300, madera=200)
    test_db.add(reino)
    test_db.commit()

    # Crear un evento y asignarlo al reino
    evento = Evento(tipo_evento="Batalla", descripcion="Batalla ganada", reino=reino)
    test_db.add(evento)
    test_db.commit()

    # Verificar que el evento está asociado correctamente al reino
    assert evento.reino_id == reino.id
    assert evento.tipo_evento == "Batalla"

    # Verificar que el reino tiene el evento asociado
    assert len(reino.eventos) == 1
    assert reino.eventos[0].tipo_evento == "Batalla"
