from infraestructuras import infraestructuras  # Importa las infraestructuras disponibles
from eventos import manejar_evento_aleatorio  # Importa la función para manejar eventos aleatorios
from turnos import calcular_puntuacion  # Importa la función para calcular la puntuación final

# Definición de la clase Reino
class Reino:
    def __init__(self, nombre):
        # Inicializa los atributos del reino
        self.nombre = nombre  # Nombre del reino
        self.oro = 100  # Cantidad inicial de oro
        self.madera = 100  # Cantidad inicial de madera
        self.territorios = 20  # Cantidad inicial de territorios
        self.infraestructura = []  # Lista de infraestructuras construidas
        self.producción = 20  # Producción inicial de recursos por turno
        self.estabilidad = 100  # Estabilidad inicial del reino

    # Método que muestra el estado del reino como una cadena de texto
    def __str__(self):
        return (f"Reino {self.nombre} - Oro: {self.oro}, Madera: {self.madera}, "
                f"Territorios: {self.territorios}, Infraestructuras: {len(self.infraestructura)}, "
                f"Producción: {self.producción}, Estabilidad: {self.estabilidad}")

    # Método para recolectar recursos (oro y madera) al final del turno
    def recolectar_recursos(self):
        self.oro += self.producción  # Aumenta el oro basado en la producción del reino
        self.madera += self.producción  # Aumenta la madera en función de la producción
        print(f"{self.nombre} ha recolectado {self.producción} de oro y {self.producción} de madera.")

    # Método para calcular la estabilidad del reino basado en infraestructuras y recursos
    def calcular_estabilidad(self):
        self.estabilidad = 100  # Estabilidad base
        for infra in self.infraestructura:
            # Aumenta la estabilidad por cada infraestructura construida
            self.estabilidad += infraestructuras[infra]["aumento_estabilidad"]
        if self.oro < 50 or self.madera < 50:
            self.estabilidad -= 10  # Penaliza si los recursos son bajos
        self.estabilidad = max(0, self.estabilidad)  # La estabilidad no puede ser negativa

# Método para comprar tierras, que aumenta el número de territorios de uno en uno
    def comprar_tierras(self):
        costo_tierra_oro = 10  # Costo en oro para comprar una tierra
        costo_tierra_madera = 10  # Costo en madera para comprar una tierra

        # Verifica si el reino tiene suficientes recursos
        if self.oro >= costo_tierra_oro and self.madera >= costo_tierra_madera:
            self.oro -= costo_tierra_oro  # Resta el oro usado para comprar una tierra
            self.madera -= costo_tierra_madera  # Resta la madera usada
            self.territorios += 1  # Aumenta los territorios en 1
            self.estabilidad += 1  # Aumenta la estabilidad del reino ligeramente (opcional)
            print(f"{self.nombre} ha comprado 1 unidad de tierra. Nuevos territorios: {self.territorios}, Estabilidad: {self.estabilidad}")
        else:
            # Si no hay suficientes recursos, muestra un mensaje al jugador
            print(f"{self.nombre} no tiene suficientes recursos para comprar tierras.")  


    # Método para construir infraestructuras
    def construir_infraestructura(self):
        print("\n--- Infraestructuras disponibles para construir ---")
        # Muestra las infraestructuras disponibles y sus costos
        for infraestructura, costos in infraestructuras.items():
            print(f"{infraestructura}: Oro: {costos['oro']}, Madera: {costos['madera']}, "
                f"Aumento producción: {costos['aumento_produccion']}, Aumento estabilidad: {costos['aumento_estabilidad']}, "
                f"Aumento territorio: {costos['aumento_territorio']}")

        # Solicita al jugador que elija una infraestructura para construir
        eleccion = input("¿Qué infraestructura deseas construir?: ")

        # Verifica si la infraestructura elegida existe
        if eleccion in infraestructuras:
            costo_oro = infraestructuras[eleccion]["oro"]  # Costo en oro
            costo_madera = infraestructuras[eleccion]["madera"]  # Costo en madera
            aumento_territorio = infraestructuras[eleccion]["aumento_territorio"]  # Aumento del territorio

            # Verifica si el reino tiene suficientes recursos
            if self.oro >= costo_oro and self.madera >= costo_madera:
                # Si hay suficientes recursos, realiza la construcción
                self.oro -= costo_oro
                self.madera -= costo_madera
                self.territorios += aumento_territorio  # Aumenta los territorios
                self.infraestructura.append(eleccion)  # Añade la infraestructura a la lista
                self.producción += infraestructuras[eleccion]["aumento_produccion"]  # Aumenta la producción
                print(f"Has construido {eleccion}. Producción aumentada a {self.producción}, Territorios aumentados a {self.territorios}.")
            else:
                # Si no hay suficientes recursos, muestra un mensaje y regresa al menú
                print(f"No tienes suficientes recursos para construir {eleccion}.")
                return False  # Indica que la construcción no se realizó
        else:
            # Si la infraestructura no está disponible, muestra un mensaje de error
            print("Esa infraestructura no está disponible.")
            return False  # Indica que la construcción no se realizó
        
        # Calcula nuevamente la estabilidad del reino después de la construcción
        self.calcular_estabilidad()
        print(f"Estabilidad actual: {self.estabilidad}")
        return True  # Indica que la construcción se realizó correctamente

    # Método para manejar los eventos aleatorios
    def manejar_evento(self):
        manejar_evento_aleatorio(self)  # Llama a la función que maneja eventos aleatorios

    # Método para calcular la puntuación final del reino
    def calcular_puntuacion(self):
        return calcular_puntuacion(self)  # Calcula la puntuación final del reino

    # Método para invadir otro reino
    def invadir(self, otro_reino):
        # Verifica si el reino tiene más estabilidad que el otro reino
        if self.estabilidad > otro_reino.estabilidad:
            print(f"{self.nombre} ha invadido {otro_reino.nombre}!")  # Muestra el éxito de la invasión
            # Toma los recursos del otro reino
            self.oro += otro_reino.oro
            self.madera += otro_reino.madera
            otro_reino.oro = 0  # El otro reino pierde todos sus recursos
            otro_reino.madera = 0
            self.estabilidad += otro_reino.estabilidad  # Aumenta la estabilidad del invasor
            otro_reino.estabilidad = 0  # El otro reino pierde estabilidad
            otro_reino.infraestructura = []  # Lista de infraestructuras construidas
        else:
            print(f"{self.nombre} no puede invadir a {otro_reino.nombre}.")  # Si no es posible invadir
            return False  # Indica que la invasión no se realizó
        return True  # Indica que la invasión fue exitosa
