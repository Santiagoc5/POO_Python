class Vehiculo:
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible

    def iniciar_marcha(self):                           
        return "El sistema de movimiento ha iniciado."

    def detener_marcha(self):                           
        return "El sistema de propulsión está detenido."

    def modificar_velocidad(self):                      
        return "Puede aumentar y reducir la velocidad de forma habitual."

    def mecanismo_direccion(self):                      
        return "Dispone de un mecanismo de guía estándar."

    def regulacion_temperatura(self):                   
        return "Módulo de gestión térmica de nivel elemental."

    def elementos_proteccion(self):                     
        return "Incorpora arneses de sujeción y bolsas de aire de serie."

    def dispositivos_luminosos(self):                   
        return "Puntos de luz frontales y posteriores operativos."

    def operatividad_ventanillas(self):                 
        return "Paneles transparentes de accionamiento manual o asistido según versión."

    def reglaje_retrovisores(self):                     
        return "Dispositivos de visión posterior ajustables según la configuración."

    def obtener_resumen(self):                         
        return f"Vehículo {self.modelo} color {self.color}, motor {self.motor}."

