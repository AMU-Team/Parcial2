import pytest
from sqlalchemy import create_engine, text

SQLALCHEMY_DATABASE_URL = "postgresql://kingdom_user:password@localhost:5432/kingdom_db"

# Crear el motor de base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Test para verificar la conectividad a la base de datos con SELECT 1
def test_select_1():
    # Ejecutar un SELECT 1 en la base de datos
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1
