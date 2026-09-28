from animal import Animal


class Delfin(Animal):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "oceano", "peces", tamano, color)

    def moverse(self):
        return f"{self.nombre} nada y salta sobre el agua"

    def adaptacion(self):
        return f"{self.nombre} respira aire por su espiraculo"
