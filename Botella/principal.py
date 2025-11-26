from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico

#Instancia del padre
objBotella = Botella("Coca cola", "1.5L", "Especial")
objBotella.imprimir_info()

#Instancia Hija
objBotella_plastica = Botella_plastico("Pepsi", "500ml", "Comun", "Redondo", "Plastico", "Sin tinte")
dato_out = objBotella_plastica.imprimir_info()
print(dato_out)