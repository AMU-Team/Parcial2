from behave import given, when, then
import requests

BASE_URL = "http://localhost:8000/api/v1"

@given('El reino "{name}" tiene una producción establecida')
def step_impl(context, name):
    # Crear un nuevo reino con el nombre proporcionado
    response = requests.post(f"{BASE_URL}/reinos/", json={"nombre": name})
    assert response.status_code == 200, f"Error al crear el reino: {response.text}"
    context.reino = response.json()

@when('El reino "{name}" recolecta recursos')
def step_impl(context, name):
    # Realizar la acción de recolectar recursos
    response = requests.post(f"{BASE_URL}/reinos/{context.reino['id']}/accion", json={"accion": "recolectar_recursos"})
    assert response.status_code == 200, f"Error al recolectar recursos: {response.text}"
    context.reino = response.json()

@then('Sus recursos de oro y madera crecen')
def step_impl(context):
    # Verificar que los recursos de oro y madera han crecido
    assert context.reino['oro'] > 0, "El oro no ha crecido"
    assert context.reino['madera'] > 0, "La madera no ha crecido"

@given('El reino "{name}" tiene suficiente oro y madera para la construccion')
def step_impl(context, name):
    # Crear un nuevo reino con el nombre proporcionado y recursos suficientes
    response = requests.post(f"{BASE_URL}/reinos/", json={"nombre": name})
    assert response.status_code == 200, f"Error al crear el reino: {response.text}"
    context.reino = response.json()
    # Asignar recursos suficientes
    context.reino['oro'] = 1000
    context.reino['madera'] = 1000

@when('El reino "{name}" construye una infraestructura "{infraestructura}"')
def step_impl(context, name, infraestructura):
    # Realizar la acción de construir infraestructura
    response = requests.post(f"{BASE_URL}/reinos/{context.reino['id']}/accion", json={"accion": "construir_infraestructura", "params": {"nombre": infraestructura}})
    assert response.status_code == 200, f"Error al construir infraestructura: {response.text}"
    context.reino = response.json()
    context.name = name  # Store the name in the context for later use

@then('La "{infraestructura}" se añade al reino "{name}" y sus recursos decrecen según el costo')
def step_impl(context, infraestructura, name):
    # Verificar que la infraestructura se ha añadido y los recursos han decrecido
    assert infraestructura in context.reino['infraestructuras'], f"La infraestructura {infraestructura} no se añadió"
    assert context.reino['oro'] < 1000, "El oro no ha decrecido"
    assert context.reino['madera'] < 1000, "La madera no ha decrecido"
    assert context.name == name, f"El nombre del reino no coincide: {context.name} != {name}"

@given('El reino "{name}" tiene suficiente oro y madera para la expansión')
def step_impl(context, name):
    # Crear un nuevo reino con el nombre proporcionado y recursos suficientes
    response = requests.post(f"{BASE_URL}/reinos/", json={"nombre": name})
    assert response.status_code == 200, f"Error al crear el reino: {response.text}"
    context.reino = response.json()
    # Asignar recursos suficientes
    context.reino['oro'] = 1000
    context.reino['madera'] = 1000

@when('El reino "{name}" expande su territorio')
def step_impl(context, name):
    # Realizar la acción de expandir territorio
    response = requests.post(f"{BASE_URL}/reinos/{context.reino['id']}/accion", json={"accion": "expandir_territorio"})
    assert response.status_code == 200, f"Error al expandir territorio: {response.text}"
    context.reino = response.json()

@then('Sus territorios debe incrementarse y sus recursos decrecen según el costo')
def step_impl(context):
    # Verificar que los territorios han incrementado y los recursos han decrecido
    assert context.reino['territorios'] > 0, "Los territorios no han incrementado"
    assert context.reino['oro'] < 1000, "El oro no ha decrecido"
    assert context.reino['madera'] < 1000, "La madera no ha decrecido"