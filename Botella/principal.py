from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico
from modelo_botella_vidrio import Botella_vidrio

#Instancia del padre
objBotella = Botella("Coca cola", "1.5L", "Especial")
objBotella.imprimir_info()

#Instancia Hija
objBotella_plastica = Botella_plastico("Pepsi", "500ml", "Comun", "Redondo", "Plastico", "Sin tinte")
objBotella_plastica.imprimir_info()

objBotella_vidrio = Botella_vidrio("SevenUp", "2.0L", "Exlusiva", "Cilindrica", "Florales")
objBotella_vidrio.imprimir_info()