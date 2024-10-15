from infraestructuras import infraestructuras
from eventos import manejar_evento_aleatorio
from turnos import calcular_puntuacion

class Reino:
    def __init__(self, nombre):
        self.nombre = nombre
        self.oro = 100
        self.madera = 100
        self.territorios = 5
        self.infraestructura = []
        self.producción = 20
        self.estabilidad = 100

    def __str__(self):
        return (f"Reino {self.nombre} - Oro: {self.oro}, Madera: {self.madera}, "
                f"Territorios: {self.territorios}, Infraestructuras: {len(self.infraestructura)}, "
                f"Producción: {self.producción}, Estabilidad: {self.estabilidad}")
    
    def recolectar_recursos(self):
        self.oro += self.producción
        self.madera += self.producción
        print(f"{self.nombre} ha recolectado {self.producción} de oro y {self.producción} de madera.")
    
    def calcular_estabilidad(self):
        self.estabilidad = 100  # Estabilidad base
        for infra in self.infraestructura:
            self.estabilidad += infraestructuras[infra]["aumento_estabilidad"]
        if self.oro < 50 or self.madera < 50:
            self.estabilidad -= 10  # Penalización por falta de recursos
        self.estabilidad = max(0, self.estabilidad)
    
    def expandir_territorio(self):
        costo_expansion_oro = 30
        costo_expansion_madera = 30
        if self.oro >= costo_expansion_oro and self.madera >= costo_expansion_madera:
            self.oro -= costo_expansion_oro
            self.madera -= costo_expansion_madera
            self.territorios += 2
            self.estabilidad += 10
            self.producción += 5
            print(f"{self.nombre} ha expandido su territorio.")
        else:
            print(f"{self.nombre} no tiene suficientes recursos para expandir el territorio.")
    
    def construir_infraestructura(self):
        print("\n--- Infraestructuras disponibles para construir ---")
        for infraestructura, costos in infraestructuras.items():
            print(f"{infraestructura}: Oro: {costos['oro']}, Madera: {costos['madera']}, "
                  f"Aumento producción: {costos['aumento_produccion']}, Aumento estabilidad: {costos['aumento_estabilidad']}")
        
        eleccion = input("¿Qué infraestructura deseas construir?: ")
        
        if eleccion in infraestructuras:
            costo_oro = infraestructuras[eleccion]["oro"]
            costo_madera = infraestructuras[eleccion]["madera"]
            
            if self.oro >= costo_oro and self.madera >= costo_madera:
                self.oro -= costo_oro
                self.madera -= costo_madera
                self.infraestructura.append(eleccion)
                self.producción += infraestructuras[eleccion]["aumento_produccion"]
                print(f"Has construido {eleccion}. Producción aumentada a {self.producción}.")
            else:
                print(f"No tienes suficientes recursos para construir {eleccion}.")
        else:
            print("Esa infraestructura no está disponible.")
        self.calcular_estabilidad()
        print(f"Estabilidad actual: {self.estabilidad}")
    
    def manejar_evento(self):
        manejar_evento_aleatorio(self)

    def calcular_puntuacion(self):
        return calcular_puntuacion(self)
    
    def invadir(self, otro_reino):
        if self.estabilidad > otro_reino.estabilidad:
            print(f"{self.nombre} ha invadido {otro_reino.nombre}!")
            self.oro += otro_reino.oro
            self.madera += otro_reino.madera
            otro_reino.oro = 0
            otro_reino.madera = 0
            self.estabilidad += otro_reino.estabilidad
            otro_reino.estabilidad = 0
        else:
            print(f"{self.nombre} no puede invadir a {otro_reino.nombre}.")
