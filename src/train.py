"""
Clase Tren
Pablo de la Iglesia Otero
"""
import simpy

class Train:
    def __init__(self, env, name, travel_time):
        """
        Constructor
        """
        self.env = env
        self.name = name
        self.travel_time = travel_time

    def transport_passengers(self, airplane_name):
        """
        Funcion principal
        """
        print(f'Train {self.name} transporting passengers for {airplane_name} at {self.env.now}')
        yield self.env.timeout(self.travel_time)
        print(f'Train {self.name} finished transporting passengers for {airplane_name} at {self.env.now}')

