from vehiculo import Vehiculo

class CarroDeportivo(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
        self.modalidad_alto_rendimiento = True 

    def modificar_velocidad(self): 
        return "Respuesta de aceleración inmediata y sistema de deceleración de alto rendimiento."

    def detalles_adicionales(self): 
        return f"Modalidad de alto rendimiento habilitada: {self.modalidad_alto_rendimiento}"

