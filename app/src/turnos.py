from menu import mostrar_menu

def jugar_turnos(reinos, turnos=5):
    for turno in range(turnos):
        print("\n" + "="*30)
        print(f"\n--- Turno {turno + 1} ---")
        print("="*30 + "\n")
        
        for reino in reinos:
            print(f"\nReino {reino.nombre} jugando su turno.")
            reino.recolectar_recursos()
            mostrar_menu(reino, reinos)
        
        # Eventos aleatorios ocurren entre turnos
        print("\n--- Eventos aleatorios al final del turno ---")
        for reino in reinos:
            reino.manejar_evento()

        # Mostrar el estado del reino al final del turno
        for reino in reinos:
            print(f"Estado actual del {reino.nombre}: {reino}")
    
    # Mostrar la puntuación final al final del juego
    print("\n--- Puntuaciones Finales ---")
    for reino in reinos:
        print(f"Puntuación final de {reino.nombre}: {reino.calcular_puntuacion()}")

def calcular_puntuacion(reino):
    puntuacion = (reino.oro + reino.madera) + (reino.territorios * 10) + (reino.estabilidad * 2) + (len(reino.infraestructura) * 20)
    return puntuacion
