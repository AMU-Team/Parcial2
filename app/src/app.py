from reino import Reino
from turnos import jugar_turnos

def iniciar_juego():
    numero_reinos = int(input("¿Cuántos reinos participan en la partida?: "))
    reinos = []
    
    for i in range(numero_reinos):
        nombre_reino = input(f"Ingresa el nombre del reino {i + 1}: ")
        reinos.append(Reino(nombre_reino))
    
    print("¡Bienvenido a Conquista de Reinos!")
    turnos = int(input("¿Cuántos turnos deseas jugar?: "))
    
    jugar_turnos(reinos, turnos)

if __name__ == "__main__":
    iniciar_juego()
