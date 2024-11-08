import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base
from src.main import app  
from src.routes import get_db

# Definir la URL de la base de datos de pruebas 
SQLALCHEMY_DATABASE_URL = "postgresql://kingdom_user:password@localhost:5432/kingdom_db"

# Crear una base de datos de pruebas
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture para la base de datos de prueba
@pytest.fixture(scope="module")
def test_db():
    """
    Fixture para inicializar y limpiar la base de datos en cada módulo de prueba.
    Crea las tablas antes de cada prueba y las elimina después.
    """
    # Crear las tablas antes de que comience la prueba
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Eliminar las tablas al finalizar la prueba
        Base.metadata.drop_all(bind=engine)

# Fixture para sobrescribir la dependencia get_db
@pytest.fixture(scope="module")
def client(test_db):
    """
    Fixture para configurar el cliente de pruebas FastAPI y sobrescribir la dependencia de la base de datos (get_db).
    Esto asegura que las pruebas usen la base de datos de prueba en lugar de la base de datos real.
    """
    def override_get_db():
        try:
            yield test_db
        finally:
            test_db.close()

    # Sobrescribir la dependencia get_db por el test_db
    app.dependency_overrides[get_db] = override_get_db

    # Crear el cliente de pruebas
    client = TestClient(app)
    
    # Reiniciar la base de datos antes de cada prueba
    client.post("/api/v1/reset")
    
    yield client

# Tests de las rutas
def test_crear_reino(client):
    """
    Test para crear un nuevo reino usando el endpoint de creación de reinos.
    Se verifica que el reino se crea correctamente con los valores por defecto para oro, madera, territorios, etc.
    """
    # Enviar solicitud POST para crear un nuevo reino
    response = client.post("/api/v1/reinos/", json={"nombre": "Reino A"})
    
    # Verificar la respuesta
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Reino A"
    assert data["oro"] == 100
    assert data["madera"] == 100
    assert data["territorios"] == 5
    assert data["produccion"] == 20
    assert data["estabilidad"] == 100

def test_listar_reinos(client):
    """
    Test para listar todos los reinos. Se crean dos reinos y luego se verifica que la lista los contiene correctamente.
    """
    # Crear dos reinos
    client.post("/api/v1/reinos/", json={"nombre": "Reino A"})
    client.post("/api/v1/reinos/", json={"nombre": "Reino B"})
    
    # Enviar solicitud GET para listar todos los reinos
    response = client.get("/api/v1/reinos/")
    
    # Verificar la respuesta
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["nombre"] == "Reino A"
    assert data[1]["nombre"] == "Reino B"

def test_actualizar_reino(client):
    """
    Test para actualizar el nombre de un reino. Se crea un reino y luego se actualiza su nombre.
    """
    # Reiniciar la base de datos
    client.post("/api/v1/reset")
    
    # Crear un reino
    response = client.post("/api/v1/reinos/", json={"nombre": "Reino A"})
    reino_id = response.json()["id"]
    
    # Enviar solicitud PUT para actualizar el nombre del reino
    response = client.put(f"/api/v1/reinos/{reino_id}", json={"nombre": "Nuevo Reino A"})
    
    # Verificar la respuesta
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Nuevo Reino A"

def test_borrar_reino(client):
    """
    Test para eliminar un reino. Se crea un reino y luego se elimina, verificando que la eliminación sea exitosa.
    """
    # Reiniciar la base de datos
    client.post("/api/v1/reset")
    
    # Crear un reino
    response = client.post("/api/v1/reinos/", json={"nombre": "Reino A"})
    reino_id = response.json()["id"]
    
    # Enviar solicitud DELETE para eliminar el reino
    response = client.delete(f"/api/v1/reinos/{reino_id}")
    
    # Verificar la respuesta
    assert response.status_code == 200
    assert response.json() == {"message": "Reino eliminado"}

def test_realizar_accion_reino(client):
    """
    Test para realizar una acción en un reino. En este caso, se verifica que la acción de 'recolectar recursos' 
    incremente los valores de oro y madera.
    """
    # Reiniciar la base de datos
    client.post("/api/v1/reset")
    
    # Crear un reino
    response = client.post("/api/v1/reinos/", json={"nombre": "Reino A"})
    reino_id = response.json()["id"]
    
    # Verificar que el reino se haya creado correctamente
    assert response.status_code == 200
    data = response.json()
    assert data["oro"] == 100
    assert data["madera"] == 100
    
    # Enviar solicitud POST para recolectar recursos
    response = client.post(f"/api/v1/reinos/{reino_id}/accion", json={"accion": "recolectar_recursos", "params": {}})
    
    # Verificar la respuesta
    assert response.status_code == 200
    data = response.json()
    
    # Verificar los cambios en los recursos
    assert data["oro"] == 120  # Oro incrementado por la acción
    assert data["madera"] == 120  # Madera también debe incrementarse por la acción

    # Verificar que los demás valores del reino permanecen inalterados
    assert data["territorios"] == 5
    assert data["produccion"] == 20
    assert data["estabilidad"] == 100

def test_reset_game(client):
    """
    Test para reiniciar el juego. Se crea un reino y luego se llama al endpoint de reiniciar,
    verificando que todos los reinos sean eliminados.
    """
    # Crear un reino
    client.post("/api/v1/reinos/", json={"nombre": "Reino A"})
    
    # Enviar solicitud POST para reiniciar el juego
    response = client.post("/api/v1/reset")
    
    # Verificar la respuesta
    assert response.status_code == 200
    assert response.json() == {"message": "Juego reiniciado"}
