from behave import fixture, use_fixture
import requests

# Base URL de la API, adaptada para el entorno de contenedores de Docker Compose
BASE_URL = "http://localhost:8000"

# Fixture para resetear el estado del juego antes de cada escenario
@fixture
def reset_game(context):
    response = requests.post(f"{BASE_URL}/reset")
    assert response.status_code == 200, "Failed to reset the game."
    context.reset_done = True

# Hook que se ejecuta antes de cada escenario
def before_scenario(context, scenario):
    # Ejecuta la fixture para resetear el estado antes de cada escenario
    use_fixture(reset_game, context)

# Hook que se ejecuta después de cada escenario (opcional, solo si necesitas limpieza adicional)
def after_scenario(context, scenario):
    # Aquí puedes añadir lógica para limpiar recursos si fuera necesario
    use_fixture(reset_game, context)