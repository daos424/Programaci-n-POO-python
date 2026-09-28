from animal import Animal


class Mariposa(Animal):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "jardin", "nectar", tamano, color)

    def moverse(self):
        return f"{self.nombre} vuela entre las flores"

    def instintos(self):
        return f"{self.nombre} busca flores por instinto"
