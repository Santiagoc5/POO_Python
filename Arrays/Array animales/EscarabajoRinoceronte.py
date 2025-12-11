from animal import Animal
class EscarabajoRinoceronte(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,
                 potencia_comparativa, cubierta_rigida, extension_apendice_frontal):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.potencia_comparativa = potencia_comparativa
        self.cubierta_rigida = cubierta_rigida
        self.extension_apendice_frontal = extension_apendice_frontal

    def perforar_tierra(self):
        print(f"{self.nombre} perfora la tierra con resolución.")

    def ejecutar_fuerza(self):
        print(f"{self.nombre} demuestra su potencia formidable.")
