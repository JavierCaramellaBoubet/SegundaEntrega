##########################################################################################################################################################################

#from google.colab import drive #Importo una biblioteca de funciones que es de google drive
#drive.mount('/drive/')  #Monto mi drive en mi Colabs
#ruta= "/drive/MyDrive/CURSO PYTHON 2023/PRIMERA PRE-ENTREGA PYTHON" #Dirección de la carpeta en el Drive

#from google.colab import drive #Importo una biblioteca de funciones que es de google drive
#drive.mount('/drive/')  #Monto mi drive en mi Colabs

ruta= "C:/Users/cti7860/Desktop/ARCHIVOS PERSONALES/Capacitación/CURSO PYTHON - CODERHOUSE/SEGUNDA PRE-ENTREGA PYTHON/paquete/" #Dirección de la carpeta donde esta ubicado el archivo

##########################################################################################################################################################################

print("#######################################################")
print("              BIENVENIDO AL PROGRAMA")
print("#######################################################")

##########################################################################################################################################################################
import os

def menu():  #Función que limpia la pantalla y muestra nuevamente el menu
  os.system("cls")
  print(" ELIJA UNA OPCION DEL MENU PRINCIPAL:\n 1- REGISTRO DE USUARIO/CONTRASEÑA  \n 2- LOGGIN EN PLATAFORMA \n 3- MOSTRAR BASE DE USUARIOS \n 4- SALIR DEL PROGRAMA ")

##########################################################################################################################################################################

diccionario={} #Diccionario vacío

def usuario_contrasena():
  print("#################################################")
  base_usuario= diccionario.update({"USUARIO":diccionario["USUARIO"], "CONTRASEÑA":diccionario["CONTRASEÑA"]})
  #return diccionario
  return base_usuario
  print("#################################################")

def pedir_datos_usuario():
  diccionario={}
  user= diccionario["USUARIO"]
  password= diccionario["CONTRASEÑA"]
  return diccionario

def mostrar_datos_de_usuario(pedir_datos_usuario):
  print("---------------------------\n")
  print(f"    NOMBRE: {'USUARIO'}")
  print(f"    APELLIDO: {'CONTRASEÑA'}")
  print("\n---------------------------\n")

def verificar_datos(user,password):
  user= diccionario["USUARIO"]
  password= diccionario["CONTRASEÑA"]

  for usuario in diccionario:
    if diccionario["USUARIO"] == "USUARIO" and diccionario["CONTRASEÑA"] == "CONTRASEÑA":
      return print("Bienvenido", diccionario["USUARIO"])
      break
    else:
      print("El usuario o contraseña son incorrectas, Intente nuevamente")  

def confirmar_user(user,diccionario):
  while (user not in diccionario):
    print("USUARIO INCORRECTO")
    user= input("Ingrese Usuario: ")
  return user

def confirmar_password(password,diccionario,intentos):
  while (password not in diccionario.values() and intentos >1 ):
    print(f"CONTRASEÑA INCORRECTA, QUEDAN {intentos} INTENTOS")
    password= input("Ingrese Contraseña: ")
  return password  


###################################################################################################################################################################

while True:
  menu()
  opcion= int(input(f"OPCION: "))
  print("----------------------------------------------------------------------------")

  if opcion == 1:
    print("Usted selecciono REGISTRO DE USUARIO/CONTRASEÑA")

    print("//////////////////////////////////////////////////////////////////////////// ")
    print("               NOMBRE DE USUARIO ")
    print("NOTA: El nombre de usuario debe ser en minúsculas.")
    print("      Debe contener entre 6 y 12 caracteres.")
    print("      Puede contener solo letras y números.")
    print("      No se permiten espacios en blanco")
    print("//////////////////////////////////////////////////////////////////////////// ")
    diccionario["USUARIO"]= str(input("Por favor ingrese su USUARIO: ")).lower()

    print("//////////////////////////////////////////////////////////////////////////// ")
    print("               CONTRASEÑA ")
    print("La contraseña debe contener 8 caracteres")
    print("La contraseña debe tener como minimo un caracter no alfanumerico")
    print("La contraseña debe tener como minimo un caracter numerico")
    print("La contraseña debe tener como minimo un caracter en mayuscula")
    print("La contraseña debe tener como minimo un caracter en minuscula")
    print("Nota: Evita los espacios en blanco")
    print("//////////////////////////////////////////////////////////////////////////// ")
    diccionario["CONTRASEÑA"]= input("Por favor ingrese su CONTRASEÑA: ")


    with open(ruta+"/base_de_usuarios.txt","a") as f:  ### Apendeamos Usuario y Contraseña en un txt del Drive
      f.write(str(diccionario["USUARIO"]+ " , " + diccionario["CONTRASEÑA"] + "\n"))
    
  
  
  elif opcion == 2:   ### REALICE EL MODO PRUEBA DE FALLOS YA QUE NO LOGRE COMPARAR EL USUARIO Y PASSWORD

    
    print("ESTAS EN OPCION 2:  EN MANTENIMIENTO")
    print("MODO PRUEBA DE FALLO")
    print("Favor de usar la URUARIO: '123456'")
    print("Favor de usar la CONTRASEÑA: '123456'")

          ## TIPICO EJEMPLIO DE PASSWORD (3 INTENTOS)

    usuario="123456"
    contraseña="123456"

    usuario_ingresado= (input("Ingrese Usuario: ")).lower()
    contraseña_ingresada= (input("Ingrese Password: "))
    cantidad_ingresos=1 # se pone (+1) porque se pide fuera del While ingresar por primera vez la contraseña

    while ((contraseña_ingresada != contraseña) and (usuario_ingresado != usuario) and(cantidad_ingresos <3)):
      usuario_ingresado= input(f"Usuario INCORRECTO, Ingrese nuevamente su USUARIO (Quedan {3-cantidad_ingresos} intentos): ")
      contrseña_ingresada= input(f"Contraseña INCORRECTA, Ingrese nuevamente su CONTRASEÑA (Quedan {3-cantidad_ingresos} intentos): ")
      cantidad_ingresos+=1
    # Termina el WHILE

    print("-------------------------------------------------------------------------------------------------------------------------------")

    if ((usuario_ingresado == usuario) and (contraseña_ingresada == contraseña)):
      print(f"BIENVENIDO USUARIO {usuario}, SE ESTA EJECUTANDO EL MODO PRUEBA DE FALLO")
    else:
      print("USTED NO ESTA AUTORIZADO, CONTACTE AL ADMINISTRADOR")   

    print("-------------------------------------------------------------------------------------------------------------------------------")








    mostrar_datos_de_usuario
    print(mostrar_datos_de_usuario)

    with open(ruta+"/base_de_usuarios.txt","r") as f:
      print(f)

      verificar_datos


    
    
  elif opcion == 3:
    try:    # Usamos el try/except para solucionar el error de consultar sin cuando no hay usuarios cargados.
      print("Usted selecciono MOSTRAR BASE DE USUARIOS")
      mostrar_base_usuarios()
      print(mostrar_base_usuarios)
    except:
      print("[*] NO HAY USUARIO CARGADOS INICIALMENTE [*]")
      print("  [*]-REALICE UN REGISTRO DE USUARIO-[*]")
      print("----------------------------------------------------------------------------")


  elif opcion == 4:
    print("[*] USTED SALIO DEL PROGRAMA [*]")
    break  

  else:
    print("[*] INGRESASTE UNA OPCION INCORRECTA [*]")
    print("----------------------------------------------------------------------------")    
    print("ELIJA UNA OPCION DEL MENU PRINCIPAL:\n 1- REGISTRO DE USUARIO/CONTRASEÑA  \n 2- LOGGIN EN PLATAFORMA \n 3- MOSTRAR BASE DE USUARIOS \n 4- SALIR DEL PROGRAMA ")
    opcion= int(input(f"OPCION: "))

##########################################################################################################################################################################

  def mostrar_base_usuarios():
    with open(ruta+"/dictionary.txt","r") as f:
      contenido=f.read()
    print("*******************************")
    print("{:<11} {:<11}".format('USUARIO','CONTRASEÑA'))
    print(contenido)

    print("*******************************\n")  

