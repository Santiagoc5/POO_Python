from animal import Animal
class Pato(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,
                 amplitud_alar, requiere_migracion, clase_cubierta_plumas):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.amplitud_alar = amplitud_alar
        self.requiere_migracion = requiere_migracion
        self.clase_cubierta_plumas = clase_cubierta_plumas

    def flotar_en_agua(self):
        print(f"{self.nombre} se desliza sobre la superficie liquida.")

    def iniciar_vuelo(self):
        print(f"{self.nombre} alza el vuelo con gracia.")
