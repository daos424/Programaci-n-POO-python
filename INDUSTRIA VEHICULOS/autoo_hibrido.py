from auto import Auto


class CarroHibrido(Auto):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "gasolina y electricidad")

    def sistema_espejo(self, estado):
        return f"Espejos {estado} con ajuste automatico"

    def climatizacion(self, estado):
        return f"Climatizacion {estado} con ahorro de energia"
