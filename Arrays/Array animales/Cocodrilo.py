from animal import Animal
class Cocodrilo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,
                 potencia_presion_mordida, entorno_acuoso, dimension_lineal):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        
        self.potencia_presion_mordida = potencia_presion_mordida
        self.entorno_acuoso = entorno_acuoso                     
        self.dimension_lineal = dimension_lineal                 

    def acechar_presa(self):
        print(f"{self.nombre} permanece inactivo antes de la emboscada.")

    def hundirse(self):
        print(f"{self.nombre} desciende bajo el agua sin hacer ruido.")

