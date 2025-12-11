class Base_de_datos:

    def __init__(self):
        self.lista_animales = []
    
    def guardar_un_objeto(self, nuevo_objeto):
        self.lista_animales.append(nuevo_objeto)

    def insertar_varios_objetos(self):
        self.lista_animales.extend(self.lista_nueva)
    
    def mostrar_información(self):
        for objeto in self.lista_animales:
            print(objeto.get_nombre)
            print(objeto.get_edad)
            print(objeto.get_habitat)
            print(objeto.get_dieta)
            print(objeto.get_tamaño)
            print(objeto.get_color)