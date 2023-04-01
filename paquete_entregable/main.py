
#2°Entrega: script.py -->
from paquete_entregable.codigo_fuente_cliente import *


# 1°Entrega: script1.py -->
#from paquete_entregable.paquete_super_mejorado.py import*


persona= Persona(nombre)

print("Ingrese Nombre: ")
nombre1 = input()
nombre= nombre1

print("Ingrese Apellido: ")
apellido1 = input()
apellido = apellido1

print("Ingrese Usuario: ")
usuario1 = input()
usuario= usuario1

print("Ingrese Contraseña: ")
contraseña1 = input()
contraseña= contraseña1

print("Ingrese Edad: ")
edad1 = int(input())
edad = edad1

print("Ingrese Fecha de Nacimiento(día/mes/año): ")
fecha_nacimiento1 = input()
fecha_nacimiento = fecha_nacimiento1

print("Ingrese Correo: ")
correo1 = input()
correo = correo1

print("Ingrese Ciudad: ")
ciudad1 = str(input())
ciudad = ciudad1

print("Ingrese Localidad: ")
localidad1 = str(input())
localidad = localidad1

print("Ingrese Domicilio: ")
domicilio1 = input()
domicilio = domicilio1

print("Ingrese DNI: ")
dni1 = input()
dni = dni1

print("Ingrese Teléfono: ")
telefono1 = input()
telefono = telefono1


print("-------------------------------------------------------------------------------") 
print("LOS DATOS DEL CLIENTE SON: ")

persona1 = Persona(nombre,apellido,usuario,contraseña,edad,fecha_nacimiento,correo,ciudad,localidad,domicilio,dni,telefono)
print(persona1)

print("-------------------------------------------------------------------------------") 

persona.saludar()



