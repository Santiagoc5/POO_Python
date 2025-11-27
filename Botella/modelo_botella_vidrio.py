from modelo_botella import Botella
class Botella_vidrio(Botella):
    def __init__(self, marca, capacidad, tapa, forma, grabados):
        super().__init__(marca, capacidad, tapa)
        self.forma = forma
        self.grabados = grabados

    def cambiar_tapa(self):
      print(f"Tapa cambiada a: {self.tapa}")

    def imprimir_info(self):
       print(f"La forma es: {self.forma}")
       print(f"El grabado es: {self.grabados}")
       super().imprimir_info()
