# Polimorfismo 
## Descripcion general 🚀
 Para entender este ejercicio debemos saber que es el polimorfismo este permite que objetos de diferentes  clases respondan al mismo método de manera diferente. En otras palabras, el polimorfismo permite que un objeto tome muchas formas aqui veremos su uso con un ejemplo de cargos de empleados
## Explicacion 
Aqui creamos una clase base "Empleado" con dos metodos que no retornan valores como tal, servira como molde para nuestras demas clases:
```
class Empleado:
    def trabajar (self):
        return ""
    def cargo (self):
        return""
```
Para utilizar nuestra clase "Empleado" en las demas clases debemos importarla (solamente si estan en diferentes archivos) asi:
```
from empleado import Empleado
```
Tenemos nuestra clase Desarrollador que utiliza los metodos trabajar y cargo pero esta vez retornara la funcion de ese empleado y su cargo en pocas palabras:
El metodo trabajar() retorna esto:
```
return "Escribiendo codigo"
```
El metodo cargo() retorna:
```
 return "Desarrollador"
```
 Asi como este ejemplo esta las demas clases Diseñador y Gerente. Lo que hacemos aqui es utilizar la clase base "Empleado" como un patron que nos permite sacar diferentes diseños a partir de él
## Ejecutando las pruebas ⚙️
En archivo "main.py" importamos nuestras tres clases Desarrollador, Diseñador, Gerente para hacer uso de ellas y ver como se ejecutan:
```
from desarrollador import Desarrollador
from diseñador import Diseñador
from gerente import Gerente
```
Posteriormente definimos una funcion mostrar_info() para valga la redundancia para mostrar la informacion de esos empleados como cargo y funcion:
```
print(f" El {empleado.cargo()} esta {empleado.trabajar()}")
```
Ahora instanciamos y creamos objetos para las clases:
```
desarrollador=Desarrollador()
diseñador=Diseñador()
gerente=Gerente()
```
Finalmente asignamos esos objetos a nuestro metodo mostrar_info() y podriamos ver resultados asi en la terminal:
```
 El Desarrollador esta Escribiendo codigo
 El Diseñador esta Creando diseño gráfico 
 El Gerente esta Gestionando el equipo
```
## Autora✒️
Norkys Peña

## Gratitud 🎁
Si deseas apoyar siguenos y comenta por alguna duda. Aceptamos donaciones $$ 🤑
 
 
