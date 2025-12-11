from carro_deportivo import CarroDeportivo
from camioneta_carga import CamionetaCarga

def main(): 
    
    vehiculo_rapido = CarroDeportivo("Porsche 911", "Rojo Fuego", "4.0 Atmosférico", 2, 2, "Premium")
    unidad_utilitaria = CamionetaCarga("Ford Transit", "Gris Plomo", "2.0 Turbo Diesel", 3, 2, "Diesel", 2200)

    print(vehiculo_rapido.obtener_resumen())        
    print(vehiculo_rapido.modificar_velocidad())         
    print(vehiculo_rapido.detalles_adicionales())       

    print(unidad_utilitaria.obtener_resumen())          
    print(unidad_utilitaria.regulacion_temperatura())    
    print(unidad_utilitaria.detalles_adicionales())      

