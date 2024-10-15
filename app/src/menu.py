# Función que muestra el menú de opciones al jugador durante su turno
def mostrar_menu(reino, reinos):
    # Muestra el estado actual del reino
    print(f"\n--- Estado actual de {reino.nombre} ---")
    print(reino)  # Imprime el estado del reino
    
    # Muestra las opciones disponibles para el jugador
    print("\n--- Opciones para el reino ---")
    print("1. Comprar tierras")
    print("2. Construir infraestructuras")
    print("3. Invadir otro reino")
    print("4. Recolectar recursos")
    print("5. Ver estado de otros reinos")  # Opción adicional para ver el estado de otros reinos
    
    # Solicita al jugador que elija una opción
    opcion = input("Elige una opción (1-5): ")
    
    # Según la opción elegida, se ejecuta la acción correspondiente
    if opcion == "1":
        reino.comprar_tierras()  # Llama a la función para comprar tierras
    elif opcion == "2":
        # Intenta construir una infraestructura. Si no se puede, vuelve al menú sin perder el turno
        if not reino.construir_infraestructura():
            mostrar_menu(reino, reinos)
    elif opcion == "3":
        # Muestra los reinos invadibles y verifica si es posible invadir
        reinos_invadibles = [otro_reino for otro_reino in reinos if otro_reino != reino and reino.estabilidad > otro_reino.estabilidad]
        if reinos_invadibles:
            for otro_reino in reinos_invadibles:
                decision_invadir = input(f"¿Deseas invadir a {otro_reino.nombre}? (s/n): ")
                if decision_invadir.lower() == "s":
                    # Si no se puede invadir, vuelve al menú sin perder el turno
                    if not reino.invadir(otro_reino):
                        mostrar_menu(reino, reinos)
        else:
            print("No hay reinos con menor estabilidad que puedas invadir.")
            mostrar_menu(reino, reinos)  # Vuelve al menú si no hay reinos invadibles
    elif opcion == "4":
        reino.recolectar_recursos()  # Llama a la función para recolectar recursos
    elif opcion == "5":
        # Muestra el estado de los otros reinos y regresa al menú
        mostrar_estado_reinos(reino, reinos)
        mostrar_menu(reino, reinos)
    else:
        print("Opción no válida, elige nuevamente.")  # Si se elige una opción inválida, vuelve a mostrar el menú
        mostrar_menu(reino, reinos)

# Función que muestra el estado de los otros reinos
def mostrar_estado_reinos(reino_actual, reinos):
    print("\n--- Estado de los otros reinos ---")
    # Recorre los reinos para mostrar su estado, excepto el reino actual del jugador
    for otro_reino in reinos:
        if otro_reino != reino_actual:
            print(f"\nReino: {otro_reino.nombre}")
            print(otro_reino)  # Imprime el estado del reino usando su método __str__
