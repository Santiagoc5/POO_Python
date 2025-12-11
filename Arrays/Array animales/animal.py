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

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_habitat(self):
        return self.habitat

    def get_dieta(self):
        return self.dieta

    def get_tamaño(self):
        return self.tamaño

    def get_color(self):
        return self.color

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def set_habitat(self, habitat):
        self.habitat = habitat

    def set_dieta(self, dieta):
        self.dieta = dieta

    def set_tamaño(self, tamaño):
        self.tamaño = tamaño

    def set_color(self, color):
        self.color = color