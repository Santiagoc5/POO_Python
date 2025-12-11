from animal import Animal
class PezTropical(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,
                 concentracion_sales, morfologia_apendice_natatorio, residente_arrecife):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        
        self.concentracion_sales = concentracion_sales             
        self.morfologia_apendice_natatorio = morfologia_apendice_natatorio 
        self.residente_arrecife = residente_arrecife          

    def desplazarse_liquido(self):
        print(f"{self.nombre} se mueve entre la barrera de coral con fluidez.")

    def modificar_tonalidad(self):
        print(f"{self.nombre} altera su pigmentación para mimetizarse.")

