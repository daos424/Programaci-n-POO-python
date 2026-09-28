from animal import Animal


class Gato(Animal):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "hogar", "pescado", tamano, color)

    def moverse(self):
        return f"{self.nombre} camina con cuidado y salta"

    def comunicacion(self):
        return f"{self.nombre} se comunica con maullidos"
