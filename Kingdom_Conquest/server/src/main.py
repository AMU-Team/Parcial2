from fastapi import FastAPI, Response
from src.database_connection import init_db
from src.routes import router as reino_router  # Importa el router desde routes.py
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST  # Importar funciones para métricas de Prometheus

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

@app.get("/metrics")
def metrics():
    """
    Endpoint para obtener métricas de Prometheus.
    Retorna las métricas en el formato adecuado.
    """
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
