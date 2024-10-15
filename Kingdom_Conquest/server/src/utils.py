def calcular_puntuacion(reino):
    puntuacion = (
        (reino.oro + reino.madera) +
        (reino.territorios * 10) +
        (reino.estabilidad * 2) +
        (len(reino.infraestructuras) * 20)
    )
    return puntuacion

def validar_recursos_suficientes(reino, costo_oro, costo_madera):
    return reino.oro >= costo_oro and reino.madera >= costo_madera
