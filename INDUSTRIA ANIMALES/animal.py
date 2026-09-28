class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color

    def moverse(self):
        return f"{self.nombre} se mueve por su habitat"

    def comunicacion(self):
        return f"{self.nombre} se comunica con otros animales"

    def reproduccion(self):
        return f"{self.nombre} se reproduce y tiene crias"

    def alimentarse(self):
        return f"{self.nombre} se alimenta de {self.dieta}"

    def adaptacion(self):
        return f"{self.nombre} esta adaptado a vivir en {self.habitat}"

    def instintos(self):
        return f"{self.nombre} usa sus instintos para sobrevivir"

    def descanso(self):
        return f"{self.nombre} busca un lugar seguro para descansar"

    def sueno(self):
        return f"{self.nombre} duerme para recuperar energia"

    def interaccion_social(self):
        return f"{self.nombre} se relaciona con otros de su especie"
