from vehiculo import Vehiculo

class CamionetaCarga(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible, aforo_kilogramos_util):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
        self.aforo_kilogramos_util = aforo_kilogramos_util

    def regulacion_temperatura(self):
        return "Sistema térmico elemental diseñado para ambiente de trabajo."

    def detalles_adicionales(self):
        return f"Volumen máximo de transporte: {self.aforo_kilogramos_util} kg"
