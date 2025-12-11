from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico
from modelo_botella_vidrio import Botella_vidrio
from base_de_datos import Base_de_datos 
from botella import botella

#Instancia del padre
objBotella = Botella("Coca cola", "1.5L", "Especial")
objBotella.imprimir_info()

#Instancia Hija
objBotella_plastica = Botella_plastico("Pepsi", "500ml", "Comun", "Redondo", "Plastico", "Sin tinte")
objBotella_plastica.imprimir_info()

objBotella_vidrio = Botella_vidrio("SevenUp", "2.0L", "Exlusiva", "Cilindrica", "Florales")
objBotella_vidrio.imprimir_info()

obj_base_de_datos = Base_de_datos()

codigo = input("Digite el codigo de la botella: ")
color = input("Digite el color de la botella: ")
obj_botella = botella(codigo, color)

obj_base_de_datos.guardar_un_objeto(obj_botella)
obj_base_de_datos.mostrar_información()