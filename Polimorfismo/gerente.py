from empleado import Empleado

class Gerente(Empleado):
    def trabajar (self):
        return "Gestionando el equipo"
    def cargo(self):
        return "Gerente"