import random

eventos = ["Invasión", "Desastre Natural", "Descubrimiento"]

def manejar_evento_aleatorio(reino):
    evento = random.choice(eventos)
    print(f"Evento aleatorio: {evento}")
    
    if evento == "Invasión":
        reino.oro -= 10
        reino.madera -= 10
        print("Invasión! El reino pierde 10 de oro y 10 de madera.")
    
    elif evento == "Desastre Natural":
        reino.territorios -= 1
        reino.infraestructura = reino.infraestructura[:-1] if reino.infraestructura else []
        print("Desastre Natural! El reino pierde 1 territorio y 1 infraestructura.")
    
    elif evento == "Descubrimiento":
        reino.oro += 15
        reino.madera += 15
        print("Descubrimiento! El reino obtiene 15 de oro y 15 de madera.")
    
    # Control de valores negativos
    reino.oro = max(0, reino.oro)
    reino.madera = max(0, reino.madera)
    reino.territorios = max(0, reino.territorios)
    reino.producción = max(0, reino.producción)
    reino.estabilidad = max(0, reino.estabilidad)
