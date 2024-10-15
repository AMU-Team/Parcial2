from menu import mostrar_menu  # Importa la función para mostrar el menú

# Función que maneja los turnos del juego
def jugar_turnos(reinos, turnos=5):  # El número de turnos es 5 por defecto
    # Bucle que itera sobre el número de turnos
    for turno in range(turnos):
        print("\n" + "="*30)
        print(f"\n--- Turno {turno + 1} ---")  # Muestra el número de turno actual
        print("="*30 + "\n")
        
        # Cada reino juega su turno
        for reino in reinos:
            print(f"\nReino {reino.nombre} jugando su turno.")  # Muestra el nombre del reino que está jugando
            # Muestra el menú de acciones para que el jugador elija qué hacer
            mostrar_menu(reino, reinos)
        
        # Después de que todos los reinos juegan, ocurren eventos aleatorios
        print("\n--- Eventos aleatorios al final del turno ---")
        for reino in reinos:
            reino.manejar_evento()  # Cada reino experimenta un evento aleatorio

        # Muestra el estado de cada reino al final del turno
        for reino in reinos:
            print(f"Estado actual del {reino.nombre}: {reino}")  # Imprime el estado actual del reino
    
    # Al finalizar todos los turnos, muestra las puntuaciones finales
    print("\n--- Puntuaciones Finales ---")
    for reino in reinos:
        print(f"Puntuación final de {reino.nombre}: {reino.calcular_puntuacion()}")  # Calcula y muestra la puntuación final de cada reino

# Función que calcula la puntuación final del reino
def calcular_puntuacion(reino):
    # La puntuación se calcula sumando los recursos (oro y madera), territorios, estabilidad y cantidad de infraestructuras
    puntuacion = (reino.oro + reino.madera) + (reino.territorios * 10) + (reino.estabilidad * 2) + (len(reino.infraestructura) * 20)
    return puntuacion  # Devuelve la puntuación calculada
