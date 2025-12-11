from Caballo import Caballo
from Cocodrilo import Cocodrilo
from PezTropical import PezTropical
from EscarabajoRinoceronte import EscarabajoRinoceronte
from Pato import Pato
from base_de_datos import Base_de_datos
from animal import Animal

def principal():
    
    equino = Caballo("Trueno", 8, "pastizal", "heno", "medio", "blanco", 75, "rizado", False)
    equino.ejecutar_carrera() 

    reptil = Cocodrilo("Mordisco", 25, "manglar", "pez y ave", "gigante", "gris oscuro", 3500, False, 5.8)
    reptil.hundirse() 

    pececillo = PezTropical("Espectro", 2, "cueva marina", "algas", "minúsculo", "amarillo", 42, "triangular", False)
    pececillo.desplazarse_liquido()

    coleoptero = EscarabajoRinoceronte("Atlas", 1, "bosque seco", "fruta", "estándar", "marrón claro", 500, "semiblando", 1.5)
    coleoptero.perforar_tierra() 
    
    ave_acuatica = Pato("Quakie", 6, "pantano", "vegetación", "grande", "marrón/negro", 1.2, False, "brillante")
    ave_acuatica.flotar_en_agua()

obj_base_de_datos = Base_de_datos()

nombre = input("Digite el nombre del animal: ")
edad = input("Digite la edad del animal: ")
habitat = input("Digite su habita: ")
dieta = input("Digite la dieta del animal: ")
tamaño = input("Digite el tamaño del animal: ")
color = input("Digite el color del animal: ")
obj_animal = Animal(nombre, edad, habitat, dieta, tamaño, color)

obj_base_de_datos.guardar_un_objeto(obj_animal)
obj_base_de_datos.mostrar_información()