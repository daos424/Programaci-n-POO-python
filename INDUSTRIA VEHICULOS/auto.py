class Auto:
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible
        self.encendido = False
        self.velocidad = 0

    def arrancar(self):
        self.encendido = True
        return f"El {self.modelo} enciende su motor {self.motor}"

    def apagar(self):
        self.encendido = False
        self.velocidad = 0
        return f"El {self.modelo} queda apagado"

    def acelerar_y_frenar(self, accion, velocidad):
        cambios = {"acelerar": velocidad, "frenar": -velocidad}
        self.velocidad += cambios[accion]
        return f"El {self.modelo} realiza la accion {accion} y queda a {self.velocidad} km/h"

    def sistema_direccion(self, tipo):
        return f"El auto tiene direccion {tipo}"

    def climatizacion(self, estado):
        return f"El aire acondicionado esta {estado}"

    def tipo_seguridad(self):
        return "El auto cuenta con cinturon de seguridad y airbags"

    def luces(self, estado):
        return f"Las luces estan {estado}"

    def sistema_ventanas(self, estado):
        return f"Las ventanas estan {estado}"

    def sistema_espejo(self, estado):
        return f"Los espejos estan {estado}"
