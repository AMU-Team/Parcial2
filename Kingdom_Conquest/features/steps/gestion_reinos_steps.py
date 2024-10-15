# common_steps.py
from behave import given
import re
import requests

BASE_URL = "http://localhost:8000"

@given("El jugador está conectado al juego")
def step_impl(context):
    pass

@given("El reino {nombre} esta en la lista de reinos")
def step_impl(context, nombre):
    pass

@when("El jugador {accion_jugador} y confirma")
def step_impl(context, accion_jugador):
    pass

@then("El {nombre} debe {accion_reino}")
def step_impl(context, nombre, accion_reino):
    pass