import random
import requests

class GameClient:
    def __init__(self, base_url="http://api:8000/api/v1"):
        # URL base del servidor API
        self.base_url = base_url

    def join_game(self, name):
        """Unirse a un juego creando un nuevo reino."""
        # Realiza una solicitud POST para crear un nuevo reino con el nombre proporcionado
        response = requests.post(f"{self.base_url}/reinos/", json={"nombre": name})
        if response.status_code == 200:
            data = response.json()  # Se guarda la respuesta JSON del servidor
            print(f"Reino '{name}' creado con éxito. ID: {data['id']}")
            return data['id']  # Devuelve el ID del reino recién creado
        else:
            print(f"Error al unirse al juego: {response.status_code} - {response.text}")
            return None

    def realizar_accion(self, reino_id, accion, params=None):
        """Realizar una acción sobre un reino."""
        # Si no hay parámetros adicionales, se inicializa con un diccionario vacío
        if params is None:
            params = {}
        # Realiza una solicitud POST para ejecutar una acción sobre el reino especificado
        response = requests.post(f"{self.base_url}/reinos/{reino_id}/accion", json={"accion": accion, "params": params})
        if response.status_code == 200:
            print(f"Acción '{accion}' realizada con éxito.")
            return response.json()  # Devuelve la respuesta JSON si la acción fue exitosa
        else:
            print(f"Error al realizar la acción: {response.status_code} - {response.text}")
            return None

    def aplicar_evento_aleatorio(self, reino_id):
        """Aplica un evento aleatorio que afecta los recursos o territorios."""
        # Selecciona un evento aleatorio de la lista proporcionada
        evento = random.choice(["perder_oro", "perder_territorios", "ganar_oro", "ganar_territorios"])
        print(f"Evento aleatorio para el reino {reino_id}: {evento}")

        # Según el evento seleccionado, se aplica la acción correspondiente al reino
        if evento == "perder_oro":
            self.realizar_accion(reino_id, "modificar_oro", {"cantidad": -20})
        elif evento == "perder_territorios":
            self.realizar_accion(reino_id, "modificar_territorios", {"cantidad": -1})
        elif evento == "ganar_oro":
            self.realizar_accion(reino_id, "modificar_oro", {"cantidad": 20})
        elif evento == "ganar_territorios":
            self.realizar_accion(reino_id, "modificar_territorios", {"cantidad": 1})

    def obtener_puntaje(self, reino):
        """Calcula el puntaje de un reino basado en oro, madera, territorios y estabilidad."""
        # El puntaje del reino se calcula sumando los valores de oro, madera, territorios y estabilidad
        return reino['oro'] + reino['madera'] + (reino['territorios'] * 10) + (reino['estabilidad'] * 2)

    def obtener_estado_reino(self, reino_id):
        """Obtiene el estado de un reino por su ID."""
        # Realiza una solicitud GET para obtener el estado de todos los reinos
        response = requests.get(f"{self.base_url}/reinos/")
        if response.status_code == 200:
            reinos = response.json()  # Obtiene la lista de reinos del servidor
            # Busca el reino por su ID en la lista de reinos y devuelve su estado
            for reino in reinos:
                if reino['id'] == reino_id:
                    return reino
        print(f"Error al obtener el estado del reino: {response.status_code} - {response.text}")
        return None
