# gestion_reinos_steps.py
from behave import given, when, then
import requests

BASE_URL = "http://localhost:8000"

@given("El jugador está conectado al juego")
def step_impl(context):
    # Assuming there's an endpoint to check if the player is connected
    response = requests.get(f"{BASE_URL}/player/status")
    assert response.status_code == 200
    context.player_connected = response.json().get("connected", False)
    assert context.player_connected is True

@given("El reino {nombre} esta en la lista de reinos")
def step_impl(context, nombre):
    response = requests.get(f"{BASE_URL}/kingdoms")
    assert response.status_code == 200
    kingdoms = response.json()
    context.kingdom_exists = any(kingdom['name'] == nombre for kingdom in kingdoms)
    assert context.kingdom_exists is True

@when("El jugador {accion_jugador} y confirma")
def step_impl(context, accion_jugador):
    # Assuming accion_jugador is something like "crea el reino {nombre}"
    match = re.match(r"crea el reino (.+)", accion_jugador)
    if match:
        nombre = match.group(1)
        response = requests.post(f"{BASE_URL}/kingdoms", json={"name": nombre})
        assert response.status_code == 201
        context.created_kingdom = response.json()

@then("El {nombre} debe {accion_reino}")
def step_impl(context, nombre, accion_reino):
    # Assuming accion_reino is something like "existir en la lista de reinos"
    if accion_reino == "existir en la lista de reinos":
        response = requests.get(f"{BASE_URL}/kingdoms")
        assert response.status_code == 200
        kingdoms = response.json()
        kingdom_exists = any(kingdom['name'] == nombre for kingdom in kingdoms)
        assert kingdom_exists is True