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

    def get_modelo(self):
        return self.modelo

    def get_color(self):
        return self.color

    def get_motor(self):
        return self.motor

    def get_numero_puertas(self):
        return self.numero_puertas

    def get_capacidad_pasajeros(self):
        return self.capacidad_pasajeros

    def get_tipo_combustible(self):
        return self.tipo_combustible

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_color(self, color):
        self.color = color

    def set_motor(self, motor):
        self.motor = motor

    def set_numero_puertas(self, numero_puertas):
        self.numero_puertas = numero_puertas

    def set_capacidad_pasajeros(self, capacidad_pasajeros):
        self.capacidad_pasajeros = capacidad_pasajeros

    def set_tipo_combustible(self, tipo_combustible):
        self.tipo_combustible = tipo_combustible