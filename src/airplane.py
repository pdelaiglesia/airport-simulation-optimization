"""
Clase de Avion
Pablo de la Iglesia
"""
import simpy

from train import Train
from checkinstand import CheckInStand
from security import SecurityCheck

class Airplane:
    def __init__(self, env, name, land_bcs, boarding_bcs, train, security, checkin, passenger_load):
        """
        Constructor
        """
        self.env = env
        self.name = name
        self.land_bcs = land_bcs
        self.boarding_bcs = boarding_bcs
        self.train = train
        self.security = security
        self.checkin = checkin
        self.passenger_load = passenger_load
        self.action = env.process(self.run())
        self.total_wait_time = 0  # Tiempo total de espera

    def run(self):
        """
        Funcion principal del avion
        """
        #Guardamos momento de inicio de la simulacion
        start_time = self.env.now 
        #Esperamos y pedimos por pista de aterrizaje
        yield self.env.timeout(5)
        print(f'{self.name} requesting landing at {self.env.now}')
        
        # Tiempo de espera para aterrizar
        with self.land_bcs.request() as req:
            yield req
            #Guardamos el tiempo en que aterriza
            landing_time = self.env.now
            print(f'{self.name} landed at {landing_time}')
            self.total_wait_time += landing_time - start_time
        
        # Proceso de check-in
        checkin_start = self.env.now
        #Ejecutamos el proceso de checkin para los pasajeros del avion
        yield self.env.process(self.checkin.process_checkin(self.name))
        checkin_end = self.env.now
        self.total_wait_time += checkin_end - checkin_start
        
        # Proceso de seguridad
        security_start = self.env.now
        #Ejecutamos el proceso de seguridad para los pasajeros del avion
        yield self.env.process(self.security.process_security(self.name))
        security_end = self.env.now
        self.total_wait_time += security_end - security_start
        
        # Transporte en tren
        train_start = self.env.now
        #Ejecutamos el proceso de llevar a los pasajeros en el tren
        yield self.env.process(self.train.transport_passengers(self.name))
        train_end = self.env.now
        self.total_wait_time += train_end - train_start
        
        # Tiempo de espera para despegar
        with self.land_bcs.request() as req2:
            yield req2
            takeoff_time = self.env.now
            print(f'{self.name} taking off at {takeoff_time}')
            self.total_wait_time += takeoff_time - train_end



