from desarrollador import Desarrollador
from diseñador import Diseñador
from gerente import Gerente

def mostrar_info(empleado):
     print(f" El {empleado.cargo()} esta {empleado.trabajar()}")

desarrollador=Desarrollador()
diseñador=Diseñador()
gerente=Gerente()

mostrar_info(desarrollador)
mostrar_info(diseñador)
mostrar_info(gerente)
