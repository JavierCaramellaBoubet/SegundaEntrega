#########################################################################################################################################################################

#from google.colab import drive #Importo una biblioteca de funciones que es de google drive
#drive.mount('/drive/')  #Monto mi drive en mi Colabs
#ruta= "/drive/MyDrive/CURSO PYTHON 2023/PRIMERA PRE-ENTREGA PYTHON" #Dirección de la carpeta en el Drive

import sys

ruta= "C:/Users/cti7860/Desktop/ARCHIVOS PERSONALES/Capacitación/CURSO PYTHON - CODERHOUSE/SEGUNDA PRE-ENTREGA PYTHON/paquete/" #Dirección de la carpeta donde esta ubicado el archivo

##########################################################################################################################################################################

print("#######################################################")
print("              BIENVENIDO AL PROGRAMA")
print("#######################################################")

##########################################################################################################################################################################
import os


def menu():  #Función que limpia la pantalla y muestra nuevamente el menu
  #os.system("cls")
  print(" ELIJA UNA OPCION DEL MENU PRINCIPAL:\n 1- REGISTRO DE USUARIO/CONTRASEÑA  \n 2- LOGGIN EN PLATAFORMA \n 3- MOSTRAR BASE DE USUARIOS \n 4- SALIR DEL PROGRAMA ")

##########################################################################################################################################################################
diccionario=set() #Diccionario vacío

##########################################################################################################################################################################


import ast
import os

FILE_NAME="dictionary.txt"

def file_exist():
    #Con esta funcion la utilizo para la simple funcionalidad de la libreria SO
    #que entre muchas cosas me permite validar la existencia del archivo
    #La funcion "exists" me devuelve un buleano
    return os.path.exists(FILE_NAME)

def load_file():
    #Open una funcion que no permite abrir archivos
    #Se indica la ruta del mismo como parametro
    #y el archivo estara representado por la variable "f"
    with open(FILE_NAME) as f:
        #Se obtiene la data de la variable "f" invocando la funcion read()
        data = f.read()
        #ast es una libreria que permite cargar el contenido del archivo
        #representado bajo la variable "data" en el diccionario directamente
        return ast.literal_eval(data)

def save_file(data_user):
    #Se abre el archivo para escribir se parece a la funcion load file
    #con la diferencia que la funcion open se le adiciona el parametro "W"
    #para indicar que se abre el archivo para escritura
    with open(FILE_NAME, 'w') as f:
        f.write(str(data_user))

def load_data():
    #Si el archivo existe se carga lo datos del archivo
    #de lo contrario devuelve un diccionario vacio
    if file_exist():
        return load_file()
    else:
        return {}

def password(key):
    # Declara las variables
    letters = len(key)
    lower_case = 0
    upper_case = 0
    numeric = 0
    no_alpha = 0
    space = 0

    # Comprueba que la contraseña es correcta
    if letters < 8:
        print('La contraseña debe contener 8 caracteres')
    else:
        for content in key:
            if content.islower():
                lower_case += 1
            elif content.isupper():
                upper_case += 1
            elif content.isdigit():
                numeric += 1
            else:
                if content.isspace():
                    space += 1
                elif not content.isalnum():
                    no_alpha += 1

        # Comprueba si la contraseña cumple con los parametros
        if lower_case >= 1:
            if upper_case >= 1:
                if numeric >= 1:
                    if no_alpha >= 1:
                        if space >= 1:
                            print('La contraseña no puede contener espacio en blancos')
                        else:
                            return True
                    else:
                        print('La contraseña debe tener como minimo un caracter no alfanumerico')
                else:
                    print('La contraseña debe tener como minimo un caracter numerico')
            else:
                print('La contraseña debe tener como minimo un caracter en mayuscula')
        else:
            print('La contraseña debe tener como minimo un caracter en minuscula')

# Funcion para el nombre de usuario
def user(name):
    # Cuenta la cantidad de letras
    letters = len(name)
    answer = name.isalnum()

    if user_exist(name):
        print("EL USUARIO YA EXISTE!!!")
    # Comprueba que el nombre cumple lo especificado
    # Cuando arme el if para la creacion del usuario no considere mayusculas!!!Por eso no me estaba funcionando bien el verify_user 
    elif letters < 6:
        print('El nombre de usuario debe contener al menos 6 caracteres')
    elif letters > 12:
        print('El nombre de usuario no puede contener mas de 12 caracteres')
    elif not answer:
        print('El nombre de usuario puede contener solo letras y numeros')
        print('Nota: Evita los espacios en blanco')
    else:
        return True

# Funcion para simular el registro
def register():
    #print("File Data")
    #print(user_dic)
    print("Usted selecciono 1- REGISTRO DE USUARIO/CONTRASEÑA")
    print("//////////////////////////////////////////////////////////////////////////// ")
    print("               NOMBRE DE USUARIO ")
    print("NOTA: El nombre de usuario debe ser en minúsculas.")
    print("      Debe contener entre 6 y 12 caracteres.")
    print("      Puede contener solo letras y números.")
    print("      No se permiten espacios en blanco")
    print("//////////////////////////////////////////////////////////////////////////// ")

    name = input("Ingrese un nombre de usuario: ").lower()

    while 1:
        answer01 = user(name)
        if answer01 == True:
            break
        else:
            name = input("Ingrese un nombre de usuario: ")

    print("//////////////////////////////////////////////////////////////////////////// ")
    print("               CONTRASEÑA ")           
    print("NOTA: La contraseña debe contener 8 caracteres.")
    print("      Debe tener como mínimo un caracter no alfanumérico.")
    print("      Debe tener como mínimo un caracter numérico.")
    print("      Debe tener como mínimo un caracter en mayúscula")
    print("      Debe tener como mínimo un caracter en minúscula.")
    print("      No se permiten espacios en blanco.")

    key = input("Ingrese una contraseña: ")
    while 1:
        answer02 = password(key)
        if answer02:
            break
        else:
            key = input("Ingrese una contraseña: ")

    add_user(name,key)
    print('Registro Exitoso')
    print('Su usuario es:', name)
    print('Su contraseña es:', key)
    save_file(user_dic)





def add_user(login,password):
    # la funcion update en diccionario me permite agregar
    # en este caso el registro a adicionar en el diccionario
    # esta  compuesto dos elementos login password
    # que a su vez son dos string
    user_dic.update({login:password})

    # el print de diccionario
    #encontras un par registro separados por la ","
    # y cada elemento esta compuesto un par de string
    #print(user_dic)

def user_exist(user_name):
    # busca en el dic el login
    # en caso de econtrarlo devuelve true false
     return user_name.lower() in user_dic

def verify_user(user_name,passw):
    # verifica usuario y password
    user_name_temp = user_name.lower()
    if user_exist(user_name_temp):
        return user_dic.get(user_name_temp) == passw
    return False

# NUEVO la variable user_dic es una variable global y es incializada por la funcion load_data()
user_dic=load_data()

# register()

def mostrar_base_usuarios():
  with open(ruta+"/dictionary.txt","r") as f:
    contenido=f.read()
    print("*******************************")
    print("{:<11} {:<11}".format('USUARIO','CONTRASEÑA'))
    print(contenido)

    print("*******************************\n")  

def append_usuario_password():

  with open(ruta+"/dictionary.txt","a") as f:  ### Apendeamos Usuario y Contraseña en un txt del Drive
    f.write("{:<11} {:<11}".format('USUARIO','CONTRASEÑA'))
    f.write(str(diccionario['USUARIO']+ " , " + diccionario['CONTRASEÑA'] + "\n"))



def salir():
  print("[*] USTED SALIO DEL PROGRAMA [*]")

while True:
  menu()
  opcion= int(input(f"OPCION: "))
  print("----------------------------------------------------------------------------")

  if opcion ==1:
      register()
      append_usuario_password()
      mostrar_base_usuarios()



  elif opcion ==2:
      print("Usted selecciono 2- LOGGIN EN PLATAFORMA")

      user = input("Ingrese un nombre de usuario: ")
      passw = input("Ingrese un contraseña: ")

      if verify_user(user,passw):
        print("\033[1m" +'Se ha Logueado Correctamente.' + "\033[0m")
        print("\033[1m" +'Usuario y contrasena correctas.' + "\033[0m")

      else:
        print("\033[1m" +'Los datos ingresados son incorrectos.'+ "\033[0m")
        print("\033[1m" +'Verifique Usuario y Contraseña'+ "\033[0m")
      

  elif opcion ==3:
    try:
      print("Usted selecciono MOSTRAR BASE DE USUARIOS")
      
      print(diccionario)

      print("{:<11} {:<11}".format('# -USUARIO- #','# -CONTRASEÑA- #'))
      mostrar_base_usuarios
      
      for key, value in user_dic.items():
        print("{:<15} {:<15}".format(key, value))

      mostrar_base_usuarios()
      print(mostrar_base_usuarios)



      # Usamos el try/except para solucionar el error de consultar sin cuando no hay usuarios cargados.

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