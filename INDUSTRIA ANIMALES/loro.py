from animal import Animal


class Loro(Animal):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "selva", "frutas", tamano, color)

    def moverse(self):
        return f"{self.nombre} vuela entre los arboles"

    def comunicacion(self):
        return f"{self.nombre} imita sonidos para comunicarse"
