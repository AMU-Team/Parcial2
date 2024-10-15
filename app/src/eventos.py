import random  # Importa la librería para manejar eventos aleatorios

# Lista de posibles eventos que pueden ocurrir
eventos = ["Invasión", "Desastre Natural", "Descubrimiento"]

# Función que maneja los eventos aleatorios para un reino
def manejar_evento_aleatorio(reino):
    evento = random.choice(eventos)  # Selecciona un evento aleatorio
    print(f"Evento aleatorio: {evento}")

    # Si ocurre una invasión
    if evento == "Invasión":
        reino.oro -= 10  # Pierde 10 de oro
        reino.madera -= 10  # Pierde 10 de madera
        print("Invasión! El reino pierde 10 de oro y 10 de madera.")
    
    # Si ocurre un desastre natural
    elif evento == "Desastre Natural":
        reino.territorios -= 1  # Pierde un territorio
        # Elimina una infraestructura si hay alguna construida
        reino.infraestructura = reino.infraestructura[:-1] if reino.infraestructura else []
        print("Desastre Natural! El reino pierde 1 territorio y 1 infraestructura.")
    
    # Si ocurre un descubrimiento de recursos
    elif evento == "Descubrimiento":
        reino.oro += 15  # Gana 15 de oro
        reino.madera += 15  # Gana 15 de madera
        print("Descubrimiento! El reino obtiene 15 de oro y 15 de madera.")

    # Asegura que los recursos y los territorios no sean negativos
    reino.oro = max(0, reino.oro)
    reino.madera = max(0, reino.madera)
    reino.territorios = max(0, reino.territorios)
    reino.producción = max(0, reino.producción)
    reino.estabilidad = max(0, reino.estabilidad)
