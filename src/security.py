"""
Clase de Seguridad del aeropuerto
Pablo de la Iglesia Otero
"""
import simpy

class SecurityCheck:
    def __init__(self, env, name, security_lines, inspection_time):
        """
        Constructor
        """
        self.env = env
        self.name = name
        self.security_lines = security_lines
        self.inspection_time = inspection_time

    def process_security(self, airplane_name):
        """
        Funcion principal
        """
        print(f'Security {self.name}: {airplane_name} is requesting security check at {self.env.now}')
        #Esperamos a que nos den una cola de seguridad
        with self.security_lines.request() as req:
            yield req
            print(f'Security {self.name}: {airplane_name} started security check at {self.env.now}')
            yield self.env.timeout(self.inspection_time)
            print(f'Security {self.name}: {airplane_name} finished security check at {self.env.now}')


