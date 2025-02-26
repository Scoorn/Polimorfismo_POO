from empleado import Empleado

class Desarrollador(Empleado):
    def trabajar (self):
        return "Escribiendo codigo"
    
    def cargo(self):
        return "Desarrollador"