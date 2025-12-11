class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    def realizar_desplazamiento(self):
        print(f"{self.nombre} está realizando un desplazamiento.")

    def emitir_señales(self):
        print(f"{self.nombre} emite señales vocales.")

    def consumir_nutrientes(self):
        print(f"{self.nombre} está ingiriendo comida.")

    def entrar_en_reposo(self):
        print(f"{self.nombre} entra en estado de reposo.")
