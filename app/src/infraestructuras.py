# Definición de las infraestructuras disponibles en el juego
# Cada infraestructura tiene un costo en oro y madera, y ofrece ciertos beneficios
infraestructuras = {
    "Granero": {
        "oro": 20,  # Costo en oro para construir el granero
        "madera": 30,  # Costo en madera para construir el granero
        "aumento_produccion": 10,  # Aumenta la producción del reino en 10 unidades
        "aumento_estabilidad": 5,  # Aumenta la estabilidad del reino en 5 puntos
        "aumento_territorio": 2  # Aumenta el número de territorios del reino en 2
    },
    "Muralla": {
        "oro": 50,  # Costo en oro para construir la muralla
        "madera": 50,  # Costo en madera para construir la muralla
        "aumento_produccion": 0,  # No afecta la producción del reino
        "aumento_estabilidad": 15,  # Aumenta la estabilidad del reino en 15 puntos
        "aumento_territorio": 5  # Aumenta el número de territorios del reino en 5
    },
    "Torre de vigilancia": {
        "oro": 30,  # Costo en oro para construir la torre de vigilancia
        "madera": 40,  # Costo en madera para construir la torre de vigilancia
        "aumento_produccion": 0,  # No afecta la producción del reino
        "aumento_estabilidad": 10,  # Aumenta la estabilidad del reino en 10 puntos
        "aumento_territorio": 3  # Aumenta el número de territorios del reino en 3
    }
}
