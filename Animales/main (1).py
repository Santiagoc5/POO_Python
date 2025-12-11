from Caballo import Caballo
from Cocodrilo import Cocodrilo
from PezTropical import PezTropical
from EscarabajoRinoceronte import EscarabajoRinoceronte
from Pato import Pato

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
