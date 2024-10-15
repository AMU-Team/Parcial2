from reino import Reino  # Importa la clase Reino
from turnos import jugar_turnos  # Importa la función que maneja los turnos del juego

# Función que inicializa el juego
def iniciar_juego():
    numero_reinos = int(input("¿Cuántos reinos participan en la partida?: "))  # Solicita el número de reinos
    reinos = []  # Inicializa una lista vacía para almacenar los reinos
    
    # Bucle para crear cada reino según el número de reinos especificado
    for i in range(numero_reinos):
        nombre_reino = input(f"Ingresa el nombre del reino {i + 1}: ")  # Solicita el nombre del reino
        reinos.append(Reino(nombre_reino))  # Añade el reino creado a la lista de reinos
    
    print("¡Bienvenido a Conquista de Reinos!")  # Mensaje de bienvenida
    
    # Llama a la función que maneja el juego, usando el valor predeterminado de 5 turnos
    jugar_turnos(reinos)

# Punto de entrada del script
if __name__ == "__main__":
    iniciar_juego()  # Inicia el juego si se ejecuta el script directamente
