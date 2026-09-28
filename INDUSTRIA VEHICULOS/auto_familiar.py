from auto import Auto


class AutoFamiliar(Auto):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "gasolina")

    def sistema_ventanas(self, estado):
        return f"Ventanas {estado} para todos los pasajeros"

    def tipo_seguridad(self):
        return "Airbags, seguros infantiles y sensores"
