print("#######################################################")
print("       BIENVENIDO AL PROGRAMA DE COMPRA ONLINE         ")
print("#######################################################")

import os
def menu():  #Función que limpia la pantalla y muestra nuevamente el menu
    os.system("cls")
    #print(" ELIJA UNA OPCION DEL MENU PRINCIPAL:\n 1- REGISTRO DE CLIENTE  \n 2- TIPO DE COMPRA \n 3- METODO DE PAGO \n 4- ENTREGA DE MERCADERIA \n 5- ADMINISTRADOR DE RED \n 6- SALIR DEL PROGRAMA ")

    
#print(" ELIJA UNA OPCION DEL MENU PRINCIPAL:\n 1- REGISTRO DE CLIENTE  \n 2- TIPO DE COMPRA \n 3- METODO DE PAGO \n 4- ENTREGA DE MERCADERIA \n 5- ADMINISTRADOR DE RED \n 6- SALIR DEL PROGRAMA ")

print("             REGISTRANDO AL CLIENTE             ")

class Persona:

    def __init__(self,nombre,apellido,edad,fecha_nacimiento,correo,ciudad,localidad,domicilio,dni,telefono): #CONSTRUCTOR
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.ciudad =  ciudad
        self.localidad = localidad
        self.domicilio = domicilio
        self.dni = dni
        self.telefono = telefono

    print("\nDATOS DEL CLIENTE") 

    def __str__(self): #METODO
        return "Nombre: {}\nApellido: {}\nEdad: {}\nFecha de Nacimiento: {}\nCorreo: {}\nCiudad: {}\nLocalidad: {}\nDomicilio: {}\nDNI: {}\nTeléfono: {}".format(self.nombre,self.apellido,self.edad,self.fecha_nacimiento,self.correo,self.ciudad,self.localidad,self.domicilio,self.dni,self.telefono)

        print("-------------------------------------------------------------------------------")    

print("Ingrese Nombre: ")
nombre1 = input()
nombre= nombre1

print("Ingrese Apellido: ")
apellido1 = input()
apellido = apellido1

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

persona1 = Persona(nombre,apellido,edad,fecha_nacimiento,correo,ciudad,localidad,domicilio,dni,telefono)
print(persona1)

print("-------------------------------------------------------------------------------") 


while True:
    print(" ELIJA UNA OPCION DEL MENU PRINCIPAL:\n 1- TIPO DE COMPRA \n 2- METODO DE PAGO \n 3- ENTREGA DE MERCADERIA \n 4- ADMINISTRADOR DE RED \n 5- SALIR DEL PROGRAMA ")
    opcion= int(input(f"OPCION: "))
    print("----------------------------------------------------------------------------")

    if (opcion ==1):
        print("         DETALLANDO EL TIPO DE COMPRA          ")

        class Cliente(Persona):  #Clase Cliente que hereda de Persona
            def __init__(self,nombre,apellido,edad,fecha_nacimiento,correo,ciudad,localidad,domicilio,dni,telefono,compra,usuario,contraseña):
                super().__init__(nombre,apellido,edad,fecha_nacimiento,correo,ciudad,localidad,domicilio,dni,telefono)
                self.compra = compra
                self.usuario = usuario
                self.contraseña = contraseña

            def __str__(self): #METODO
                return "Nombre: {}\nApellido: {}\nEdad: {} años\nFecha de Nacimiento: {}\nCorreo: {}\nCiudad: {}\nLocalidad: {}\nDomicilio: {}\nDNI: {}\nTeléfono: {}\nCompra: {}\nUsuario: {}\nContraseña: {}".format(self.nombre,self.apellido,self.edad,self.fecha_nacimiento,self.correo,self.ciudad,self.localidad,self.domicilio,self.dni,self.telefono,self.compra,self.usuario,self.contraseña)    


        print("-------------------------------------------------------------------------------") 
        print("DETALLANDO EL TIPO DE COMPRA: ")
        print("Ingrese Tipo Compra (Por Internet - vía WEB/Telefónica): ")
        compra1 = input()
        compra= compra1

        print("Ingrese Usuario: ")
        usuario1 = input()
        usuario= usuario1

        print("Ingrese Contraseña: ")
        contraseña1 = input()
        contraseña= contraseña1

        print("-------------------------------------------------------------------------------") 

        cliente1 = Cliente(nombre,apellido,edad,fecha_nacimiento,correo,ciudad,localidad,domicilio,dni,telefono,compra,usuario,contraseña)
        print(cliente1)
        print("-------------------------------------------------------------------------------")



    
    elif opcion ==2:
        print("     METODO DE PAGO      ")


        class Metodo_pago(Persona):

            def __init__(self,nombre,apellido,edad,fecha_nacimiento,correo,ciudad,localidad,domicilio,dni,telefono,medio_de_pago,banco,cuotas):
                super().__init__(nombre,apellido,edad,fecha_nacimiento,correo,ciudad,localidad,domicilio,dni,telefono)
                self.medio_de_pago= medio_de_pago
                self.banco = banco
                self.cuotas = cuotas

            print("     FORMA DE PAGO       ")     

            def __str__(self):
                return "Nombre: {}\nApellido: {}\nEdad: {}\nFecha de Nacimiento: {}\nCorreo: {}\nCiudad: {}\nLocalidad: {}\nDomicilio: {}\nDNI: {}\nTeléfono: {}\nMedio de Pago: {}\nBanco: {}\nCantidad de Cuotas: {}".format(self.nombre,self.apellido,self.edad,self.fecha_nacimiento,self.correo,self.ciudad,self.localidad,self.domicilio,self.dni,self.telefono,self.medio_de_pago,self.banco,self.cuotas)

                #self.nombre,self.apellido,self.edad,self.fecha_nacimiento,self.correo,self.ciudad,self.localidad,self.domicilio,self.dni,self.telefono,self.medio_de_pago,self.banco,self.cuotas

        print("##############################################################################") 
        print("Ingrese Medio de Pago (Débito/Tarjeta de Crédito): ")
        medio_de_pago1 = input()
        medio_de_pago= medio_de_pago1

        print("Ingrese BANCO: ")
        banco1 = input()
        banco= banco1

        print("Ingrese Cantidad de Cuotas (3/6/12/18): ")
        cuotas1 = input()
        cuotas= cuotas1

        print("##############################################################################") 
        print("     SELECCION DE METODO DE PAGO:        ")

        medio_de_pago1 = Metodo_pago(nombre,apellido,edad,fecha_nacimiento,correo,ciudad,localidad,domicilio,dni,telefono,medio_de_pago,banco,cuotas)
        print(medio_de_pago1)
        print("##############################################################################") 



    elif opcion == 3:
        print("      ENTREGA DE MERCADERIA       ")

        class Entrega_mercaderia(Persona):
            def __init__(self,nombre,apellido,edad,fecha_nacimiento,correo,ciudad,localidad,domicilio,dni,telefono,tipo_retiro_mercaderia,dia,horario):
                super().__init__(nombre,apellido,edad,fecha_nacimiento,correo,ciudad,localidad,domicilio,dni,telefono)
                self.tipo_retiro_mercaderia = tipo_retiro_mercaderia
                self.dia = dia
                self.horario = horario

            print("     ENTREGA DE MERCADERIA       ")

            def __str__(self):
                return "Nombre: {}\nApellido: {}\nEdad: {}\nFecha de Nacimiento: {}\nCorreo: {}\nCiudad: {}\nLocalidad: {}\nDomicilio: {}\nDNI: {}\nTeléfono: {}\nTipo de Entrega: {}\nDía: {}\nHorario: {}".format(self.nombre,self.apellido,self.edad,self.fecha_nacimiento,self.correo,self.ciudad,self.localidad,self.domicilio,self.dni,self.telefono,self.tipo_retiro_mercaderia,self.dia,self.horario)


        print("-------------------------------------------------------------------------------") 
        print("Ingrese Lugar de Entrega/Retiro de Mercadería (Entrega en su Domicilio/Picking Supermercado): ")
        tipo_retiro_mercaderia1 = input()
        tipo_retiro_mercaderia= tipo_retiro_mercaderia1

        print("Ingrese Día preferido para la entrega (Lunes a Viernes): ")
        dia1 = input()
        dia= dia1

        print("Ingrese Horario disponible (8 a 21 hs): ")
        horario1 = input()
        horario= horario1

        print("-------------------------------------------------------------------------------")
        print("      ENTREGA DE MERCADERIA       ")

        Entrega_mercaderia1 = Entrega_mercaderia(nombre,apellido,edad,fecha_nacimiento,correo,ciudad,localidad,domicilio,dni,telefono,tipo_retiro_mercaderia,dia,horario)
        print(Entrega_mercaderia1)
        print("-------------------------------------------------------------------------------")


    elif opcion ==4:
        print("     ADMINISTRAR REDES       ")
        class Administrador(Persona):  #Clase Administrador que hereda de Persona
            def __init__(self,nombre,apellido,edad,fecha_nacimiento,correo,ciudad,localidad,domicilio,dni,telefono,usuario,contraseña,telefono_admin):
                super().__init__(nombre,apellido,edad,fecha_nacimiento,correo,ciudad,localidad,domicilio,dni,telefono)
                
                self.telefono_admin = telefono_admin
                self.usuario = usuario
                self.contraseña = contraseña

            print("     DATOS DEL ADMINISTRADOR DE REDES        ") 

            def __str__(self): #METODO
                return "Nombre: {}\nApellido: {}\nEdad: {}\nFecha de Nacimiento: {}\nCorreo: {}\nCiudad: {}\nLocalidad: {}\nDomicilio: {}\nDNI: {}\nTeléfono: {}\nUsuario: {}\nContraseña: {}\nTeléfono Administrador de RED: {}".format(self.nombre,self.apellido,self.edad,self.fecha_nacimiento,self.correo,self.ciudad,self.localidad,self.domicilio,self.dni,self.telefono,self.usuario,self.contraseña,self.telefono_admin)     

                #self.nombre,self.apellido,self.edad,self.fecha_nacimiento,self.correo,self.ciudad,self.localidad,self.domicilio,self.dni,self.telefono,self.usuario,self.contraseña,self.telefono_admin
                
        print("-------------------------------------------------------------------------------")
        print("     ADMINISTRADOR DE REDES:     ")
        print("Ingrese Usuario Administrador de RED: ")
        usuario1 = input()
        usuaario= usuario1

        print("Ingrese Contraseña Administrador de RED: ")
        contraseña1 = input()
        contraseña= contraseña1   

        print("Ingrese Telefono Contacto Administrador de RED: ")
        telefono_admin1 = input()
        telefono_admin= telefono_admin1

        print("-------------------------------------------------------------------------------") 

        administrador1 = Administrador(nombre,apellido,edad,fecha_nacimiento,correo,ciudad,localidad,domicilio,dni,telefono,usuario,contraseña,telefono_admin)
        print(administrador1)
        print("-------------------------------------------------------------------------------")


    elif opcion ==5:
        print("[*] USTED SALIO DEL PROGRAMA [*]")
        break

    else:
        print("[*] INGRESASTE UNA OPCION INCORRECTA [*]")
        print("----------------------------------------------------------------------------") 
        print(" ELIJA UNA OPCION DEL MENU PRINCIPAL:\n 1- TIPO DE COMPRA \n 2- METODO DE PAGO \n 3- ENTREGA DE MERCADERIA \n 4- ADMINISTRADOR DE RED \n 5- SALIR DEL PROGRAMA ")
        opcion= int(input(f"OPCION: "))
