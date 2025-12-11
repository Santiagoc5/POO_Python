from carro_deportivo import CarroDeportivo
from camioneta_carga import CamionetaCarga
from base_de_datos import Base_de_datos
from vehiculo import Vehiculo

def main(): 
    
    vehiculo_rapido = CarroDeportivo("Porsche 911", "Rojo Fuego", "4.0 Atmosférico", 2, 2, "Premium")
    unidad_utilitaria = CamionetaCarga("Ford Transit", "Gris Plomo", "2.0 Turbo Diesel", 3, 2, "Diesel", 2200)

    print(vehiculo_rapido.obtener_resumen())        
    print(vehiculo_rapido.modificar_velocidad())         
    print(vehiculo_rapido.detalles_adicionales())       

    print(unidad_utilitaria.obtener_resumen())          
    print(unidad_utilitaria.regulacion_temperatura())    
    print(unidad_utilitaria.detalles_adicionales())      

obj_base_de_datos = Base_de_datos()

modelo = input("Digite el modelo del vehículo: ")
color = input("Digite el color del vehículo: ")
motor = input("Digite el tipo de motor: ")
numero_puertas = int(input("Digite el número de puertas: "))
capacidad_pasajeros = int(input("Digite la capacidad de pasajeros: "))
tipo_combustible = input("Digite el tipo de combustible: ")
obj_vehiculo = Vehiculo(modelo,color,motor,numero_puertas,capacidad_pasajeros,tipo_combustible)

obj_base_de_datos.guardar_un_objeto(obj_vehiculo)

obj_base_de_datos.mostrar_información()