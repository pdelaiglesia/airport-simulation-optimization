"""
Programa principal
Pablo de la Iglesia
"""
import simpy
import numpy as np
import pandas as pd
from pyswarm import pso
from itertools import product

from airplane import Airplane
from train import Train
from security import SecurityCheck
from checkinstand import CheckInStand


def run_simulation(num_fingers, num_security, num_runways, num_checkin):
    #Creamos el environment
    env = simpy.Environment()
    #Creamos los recursos compartidos
    land_bcs = simpy.Resource(env, capacity=num_runways)  
    boarding_bcs = simpy.Resource(env, capacity=num_fingers)  
    station_bcs = simpy.Resource(env, capacity=2)  
    security_lines = simpy.Resource(env, capacity=num_security)  
    check_in_stands = simpy.Resource(env, capacity=num_checkin)  
    #Creamos el tren, la seguridad y el checkin
    train = Train(env, 'Train 1', travel_time=10)  
    security = SecurityCheck(env, 'Security Checkpoint', security_lines, inspection_time=8)  
    check_in = CheckInStand(env, 'Check-In Area', num_stands=num_checkin, check_in_time=15)  
    total_wait_time = 0
    plane_count = 0
    #Funcion que genera aviones
    def generate_planes(env, land_bcs, boarding_bcs, train, security, check_in, interval):
        nonlocal total_wait_time, plane_count
        i = 0
        while True:
            #Damos datos random a l
            passenger_load = np.random.randint(50, 101)
            
            # Crear avión y esperar a que su proceso termine
            plane = Airplane(env, f'Plane {i}', land_bcs, boarding_bcs, train, security, check_in, passenger_load)
            yield plane.action
            
            # Actualizar numero de aviones y tiempo de espera
            total_wait_time += plane.total_wait_time
            plane_count += 1
            i += 1
            #Esperar intervalo de tiempo para crear nuevo
            yield env.timeout(interval)
    #Corremos el programa con proceso principal de generar aviones
    env.process(generate_planes(env, land_bcs, boarding_bcs, train, security, check_in, 10))
    env.run(until=500)
    #Calculamos tiempo de espera medio y lo devolvemos
    avg_wait_time = total_wait_time / plane_count if plane_count > 0 else float('inf')
    return avg_wait_time
#Funcion que encuentra la función objetivo
def objective_function(params):
    #Extrae paramentros
    num_fingers, num_security, num_runways, num_checkin = map(int, params)
    #Corremos simulacion y guardamos tiempo de espera medio
    avg_wait_time = run_simulation(num_fingers, num_security, num_runways, num_checkin)
    return avg_wait_time

# Función para realizar el Producto Cartesiano
def cartesian_product():
    #Definimos rangos de parametros
    num_fingers = [1, 2, 3, 5, 7, 10]
    num_security = [1, 2, 3, 4, 5, 10]
    num_runways = [1, 2, 3, 4, 5]
    num_checkin = [1, 2, 3, 5, 10]
    #Calculamos todas las combinaciones posibles
    param_combinations = list(product(num_fingers, num_security, num_runways, num_checkin))
    
    results = []
    
    # Ejecutar la simulación para cada combinación
    for params in param_combinations:
        num_fingers, num_security, num_runways, num_checkin = params
        avg_wait_time = run_simulation(num_fingers, num_security, num_runways, num_checkin)
        results.append({
            'Fingers': num_fingers,
            'Security': num_security,
            'Runways': num_runways,
            'Check-ins': num_checkin,
            'Avg Wait Time': avg_wait_time
        })

    # Crear un DataFrame con los resultados
    df_cartesian_results = pd.DataFrame(results)
    df_cartesian_results.to_csv('cartesian_results.csv', index=False)
    print(df_cartesian_results)
    
    return df_cartesian_results
#Funncion para optimizar mediante PSO
def run_pso_optimization():
    #Definimos limites de busqueda
    lb = [1, 1, 1, 1]  
    ub = [10, 10, 5, 10]  
    #Minimizamos la funcion objetivo mediante PSO
    xopt, fopt = pso(objective_function, lb, ub, swarmsize=50, omega=0.5, phip=1.5, phig=1.5, maxiter=100)
    #Mostramos la mejor solucion
    print(f"Mejor solución encontrada: Fingers: {int(xopt[0])}, Seguridad: {int(xopt[1])}, Pistas: {int(xopt[2])}, Check-ins: {int(xopt[3])}")
    print(f"Valor objetivo mínimo: {fopt}")
    return xopt, fopt


if __name__ == "__main__":
    
    print("Ejecutando Producto Cartesiano:")
    df_cartesian = cartesian_product()
    
    print("\nEjecutando PSO para optimización:")
    run_pso_optimization()









