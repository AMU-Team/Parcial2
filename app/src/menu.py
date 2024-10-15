def mostrar_menu(reino, reinos):
    print(f"\n--- Estado actual de {reino.nombre} ---")
    print(reino)
    print("\n--- Opciones para el reino ---")
    print("1. Expandir territorios")
    print("2. Comprar tierras")
    print("3. Construir infraestructuras")
    print("4. Invadir otro reino")
    print("5. No hacer nada este turno")
    
    opcion = input("Elige una opción (1-5): ")
    
    if opcion == "1":
        reino.expandir_territorio()
    elif opcion == "2":
        reino.comprar_tierras()
    elif opcion == "3":
        reino.construir_infraestructura()
    elif opcion == "4":
        reinos_invadibles = [otro_reino for otro_reino in reinos if otro_reino != reino and reino.estabilidad > otro_reino.estabilidad]
        if reinos_invadibles:
            for otro_reino in reinos_invadibles:
                decision_invadir = input(f"¿Deseas invadir a {otro_reino.nombre}? (s/n): ")
                if decision_invadir.lower() == "s":
                    reino.invadir(otro_reino)
        else:
            print("No hay reinos con menor estabilidad que puedas invadir.")
    elif opcion == "5":
        print(f"{reino.nombre} no hará nada en este turno.")
    else:
        print("Opción no válida, elige nuevamente.")
        mostrar_menu(reino, reinos)
