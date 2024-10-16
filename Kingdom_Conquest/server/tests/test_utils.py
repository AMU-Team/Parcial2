import pytest
from src.models import Reino, Infraestructura
from src.utils import calcular_puntuacion, validar_recursos_suficientes

# Test para la función calcular_puntuacion
def test_calcular_puntuacion():
    # Crear un reino ficticio
    reino = Reino(
        nombre="Reino A",
        oro=100,
        madera=50,
        territorios=3,
        estabilidad=80,
    )

    # Crear dos infraestructuras asociadas al reino
    infraestructura_1 = Infraestructura(nombre="Granero")
    infraestructura_2 = Infraestructura(nombre="Torre")

    # Asignar las infraestructuras al reino
    reino.infraestructuras = [infraestructura_1, infraestructura_2]

    # Calcular la puntuación del reino
    puntuacion = calcular_puntuacion(reino)

    # Verificar el cálculo de la puntuación
    # Fórmula: (oro + madera) + (territorios * 10) + (estabilidad * 2) + (infraestructuras * 20)
    # Puntuación esperada: (100 + 50) + (3 * 10) + (80 * 2) + (2 * 20) = 150 + 30 + 160 + 40 = 380
    assert puntuacion == 380

# Test para la función validar_recursos_suficientes
def test_validar_recursos_suficientes():
    # Crear un reino ficticio
    reino = Reino(
        nombre="Reino B",
        oro=100,
        madera=50,
    )

    # Caso 1: Recursos suficientes
    assert validar_recursos_suficientes(reino, costo_oro=50, costo_madera=20) == True

    # Caso 2: No tiene suficiente oro
    assert validar_recursos_suficientes(reino, costo_oro=120, costo_madera=20) == False

    # Caso 3: No tiene suficiente madera
    assert validar_recursos_suficientes(reino, costo_oro=50, costo_madera=60) == False

    # Caso 4: No tiene suficientes recursos en general
    assert validar_recursos_suficientes(reino, costo_oro=120, costo_madera=60) == False
