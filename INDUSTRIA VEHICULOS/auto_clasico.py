from auto import Auto


class AutoClasico(Auto):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "gasolina")

    def sistema_direccion(self, tipo):
        return f"Direccion {tipo} con volante de estilo antiguo"

    def tipo_seguridad(self):
        return "Cinturones y frenos reforzados"
