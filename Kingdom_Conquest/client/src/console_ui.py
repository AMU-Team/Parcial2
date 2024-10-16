from game_client import GameClient

def main():
    client = GameClient()

    # Crear dos reinos
    nombre1 = input("Ingresa el nombre del primer reino: ")
    reino1_id = client.join_game(nombre1)

    nombre2 = input("Ingresa el nombre del segundo reino: ")
    reino2_id = client.join_game(nombre2)

    if not reino1_id or not reino2_id:
        print("Error al crear los reinos. No se puede continuar.")
        return

    # Cada reino realiza 3 acciones
    for i in range(3):
        print(f"\n--- Turno {i+1} ---")
        print(f"{nombre1} - Realiza una acción")
        accion1 = input("Elige una acción (recolectar_recursos, expandir_territorio, construir_infraestructura): ")
        client.realizar_accion(reino1_id, accion1)

        print(f"{nombre2} - Realiza una acción")
        accion2 = input("Elige una acción (recolectar_recursos, expandir_territorio, construir_infraestructura): ")
        client.realizar_accion(reino2_id, accion2)

    # Aplicar 3 eventos aleatorios
    print("\n--- Eventos aleatorios ---")
    for i in range(3):
        client.aplicar_evento_aleatorio(reino1_id)
        client.aplicar_evento_aleatorio(reino2_id)

    # Obtener el estado final de los reinos
    reino1 = client.obtener_estado_reino(reino1_id)
    reino2 = client.obtener_estado_reino(reino2_id)

    if not reino1 or not reino2:
        print("Error al obtener el estado final de los reinos.")
        return

    # Calcular puntajes
    puntaje1 = client.obtener_puntaje(reino1)
    puntaje2 = client.obtener_puntaje(reino2)

    print(f"\nPuntaje final de {nombre1}: {puntaje1}")
    print(f"Puntaje final de {nombre2}: {puntaje2}")

    # Determinar el ganador
    if puntaje1 > puntaje2:
        print(f"¡{nombre1} es el ganador!")
    elif puntaje2 > puntaje1:
        print(f"¡{nombre2} es el ganador!")
    else:
        print("Es un empate.")

if __name__ == "__main__":
    main()
