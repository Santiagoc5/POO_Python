from animal import Animal
class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,
                 cifra_velocidad_punta, clase_cobertura_pelo, bajo_cuidado_humano):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        
        self.cifra_velocidad_punta = cifra_velocidad_punta       
        self.clase_cobertura_pelo = clase_cobertura_pelo         
        self.bajo_cuidado_humano = bajo_cuidado_humano          

    def ejecutar_carrera(self):
        print(f"{self.nombre} ejecuta la carrera a {self.cifra_velocidad_punta} km/h.")

    def consumir_hierba(self):
        print(f"{self.nombre} está consumiendo hierba en el prado.")
