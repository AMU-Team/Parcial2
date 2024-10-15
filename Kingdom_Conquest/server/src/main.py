from fastapi import FastAPI
from src.database_connection import init_db
from src.routes import router as reino_router  # Importa el router desde routes.py

app = FastAPI()

# Inicializa la base de datos y crea las tablas
@app.on_event("startup")
def startup_event():
    init_db()

# Registrar el router para las rutas del reino
app.include_router(reino_router, prefix="/api/v1")  # Prefijo opcional para las rutas

# Ruta raíz
@app.get("/")
def read_root():
    return {"message": "Bienvenido a Kingdom Conquest API"}
