"""
Clase de CheckIn
Pablo de la Iglesia
"""
import simpy

class CheckInStand:
    def __init__(self, env, name, num_stands, check_in_time):
        """
        Constructor
        """
        self.env = env
        self.name = name
        self.stands = simpy.Resource(env, capacity=num_stands)
        self.check_in_time = check_in_time

    def process_checkin(self, airplane_name):
        """
        Funcion Principal
        """
        print(f'{self.name}: {airplane_name} is requesting a stand at {self.env.now}')
        #Pedimos un puesto de checkin 
        with self.stands.request() as req:
            yield req
            print(f'{self.name}: {airplane_name} started check-in at {self.env.now}')
            yield self.env.timeout(self.check_in_time)
            print(f'{self.name}: {airplane_name} finished check-in at {self.env.now}')

