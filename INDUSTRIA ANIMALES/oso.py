from animal import Animal


class Oso(Animal):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "bosque", "frutas y peces", tamano, color)

    def moverse(self):
        return f"{self.nombre} camina y trepa por el bosque"

    def instintos(self):
        return f"{self.nombre} busca alimento guiado por su olfato"
