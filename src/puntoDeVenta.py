import os
import random
from io import open


def generador_contrasena(longitud):
    minus="abcdefghijklmnopqrstuvwxyz"
    muestra=random.sample(minus,longitud)
    password="".join(muestra)
    return password
   
def cifrado(cadena):
    caracter="abcdefghijklmnopqrstuvwxyz"
    listB= list(caracter)
    listR= list(caracter)
    listR.reverse()
    clave=""
    listlogin=list(cadena)
    i=0
    while i < len(cadena):
        caracter=listlogin[i]
        j= listB.index(caracter)
        clave= clave+ listR[j]
        i=i+1
    return(clave)
def crear_archivo(nombre):
    archivo= open(nombre,"w")
    archivo.close()

def sobrescribir_archivo(contenido, nombre_archivo):
    archivo=open(nombre_archivo,"w")
    archivo.write(contenido)
    archivo.close()

def agregar_archivo(contenido, nombre_archivo):
    if os.path.isfile(nombre_archivo):
        contenido_anterior=leer_archivo(nombre_archivo)
        
        if len(contenido_anterior)>0:
            contenido= "#"+ contenido
        archivo=open(nombre_archivo,"a")

        archivo.write(contenido)
        archivo.close()
    else:
        sobrescribir_archivo(contenido, nombre_archivo)
def leer_archivo(nombre):
    archivo= open(nombre, "r")
    contenido = archivo.read()
    archivo.close()
    return contenido

def borrarPantalla(): #borra pantalla de consola
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def menuLogin():# nos muestra el login
    borrarPantalla()
    print("BINVENIDO")
    print("PUNTO DE VENTA")
    print("\n")
    usuario=  input("USUARIO: ")

    password= input("CONTRASEÑA: ")
    return len(password)

def menuAdministrador():# nos muestra el menu de administrador 
    borrarPantalla()
    print ("PUNTO DE VENTA")
    print ("MODO ADMINISTRADOR")
    print ("\n")
    print ("1- ADMINISTRAR USUARIOS")
    print ("2- ADMINISTRAR VENDEDOR")
    print ("3- SALIR DEL PROGRAMA")
    opcionAdministrador = input("ELIGE UNA OPCION VALIDA: ")
    return (int(opcionAdministrador))

def menuVendedores():# nos muestra el menu de los vendedores
    borrarPantalla()
    print ("ELIJA UNA OPCIÓN DEL MENU ")
    print ("1-  VENDER ")
    print ("2- BUSCAR PRODUCTO")
    print ("3- LISTA DE PRODUCTOS EN FALTA")
    print ("4-  SALIR ")
    opcionVendedor = input("ELIJA UNA OPCION VALIDA: ")
    return (int(opcionVendedor))
def menuAMEUsuarios(): # nos muestra el menu donde modificar los usuarios
    borrarPantalla()
    print ("1- AGREGAR USUARIO ")
    print ("2- MODIFICAR USUARIO ")
    print ("3- ELIMINAR USUARIO ")
    print ("4- QUIERES VOLVER AL MENU ANTERIOR ")

    opcionAMEUsuario = input("ELIJA UNA OPCION VALIDA: ")
    return (int(opcionAMEUsuario))

def menuModificarStock(): #nos muestra el menu donde poder modificar el Stock, consultarlo y agregar un articulo
    borrarPantalla()
    print ("1- MODIFICAR PRODUCTO")
    #print ("2- MODIFICAR PRECIO ")
    print ("2- AGREGAR PRODUCTO")
    print ("3- ELIMINAR PRODUCTO")
    opcionModificarStock= input(" ELIJA UNA OPCION VALIDA: ")

def agregarUsuario():
    borrarPantalla()
    print  ("AGREGAR NUEVO USUARIO") 
    usuario= input("NOMBRE DEL NUEVO USUARIO: ")
    password=generador_contrasena(6)
    print ("EL NUEVO USUARIO ES: " + usuario)
    print ("SU CONTRASEÑA ES: " + password)
    contrasena_cifrada= cifrado(password)
    agregar_archivo(usuario, "usuario.txt")
    agregar_archivo(contrasena_cifrada, "password.txt")
   
def menuModificarUsuario():
    borrarPantalla()
    print ("ESTAS POR MODIFICAR UN USUARIO")
    usuario= input( "INGRESE EL USUARIO QUE DESEA MODIFICAR: ")
    password=generador_contrasena(6)
    contrasena_cifrada=cifrado(password)
    nuevo_usuario=input(" INGRESE NUEVO USUARIO: ")
    resultado=modificarUsuario(usuario,nuevo_usuario,contrasena_cifrada)
    if resultado==True:
        print ("TU NUEVO USUARIO ES: " + nuevo_usuario)
        print ("TU CONTRASENA ES : " + password)
    else:
        print("EL USUARIO NO FUE ENCONTRADO")
def modificarUsuario(usuario_viejo, usuario_nuevo, password):
    usuario_txt=leer_archivo("usuario.txt")
    password_txt=leer_archivo("password.txt")
    lista_usuario= usuario_txt.split("#")
    lista_password=password_txt.split("#")
    i=0
    #while len(lista_usuario) >i and lista_usuario[i]!= usuario_viejo:
     #   i = i +1
    for us_existente in lista_usuario:
        if us_existente==usuario_viejo:
            lista_usuario[i]=usuario_nuevo
            lista_password[i]=password
            usuario_txt=("#").join(lista_usuario)
            password_txt=("#").join(lista_password)
            sobrescribir_archivo(usuario_txt, "usuario.txt")
            sobrescribir_archivo(password_txt, "password.txt")
            return True
        else:
            i=i+1

    return False
   
      
    
def eliminarUsuario():
    borrarPantalla()
    usuario=print(input (" ELIJA EL USUARIO A ELIMINAR: "))
    password= inhabilitada
    sobrescribir_archivo(usuario, "usuario.txt")
    sobrescribir_archivo(password, "password.txt")
    print ("EL SIGUIENTE USUARIO ESTA INHABILITADO")
    
def modificar_articulo():
    borrarPantalla()
    print("ELIJA EL ARTICULO A MODIFICAR: ")
def agregar_articulo():
    borrarPantalla()
    print("INGRESE EL ARTICULO A AGREGAR: ")
def menu_ventas():
    productos=leer_archivo("productos.txt")
    totalventa=0
    while True:
        borrarPantalla()
        print("VENTAS DE PRODUCTOS")
        pro_vendido= input("INGRESE EL PRODUCTO A VENDER: ")
        cantidad=input("INGRESE LA CANTIDAD QUE VA A COMPRAR: ")
        registro_venta= registrar_ventas(productos,pro_vendido,cantidad)
        productos=registro_venta[0]
        totalventa=registro_venta[1]+totalventa
        fin=input("DESEAS SEGUIR COMPRANDO: ")
        if fin == "no":
            break
    
    sobrescribir_archivo(productos,"productos.txt")
    print(" TU SALDO A PAGAR ES= "+ str(totalventa))
    input()
   
def registrar_ventas(productos,pro_vendido,cantidad):
    subtotal=0
    pos=0
    lista_productos=productos.split("#")
    for prod in lista_productos:
        registro_producto = prod.split(",")
        if pro_vendido == registro_producto[1]:
            if int(cantidad) > int(registro_producto[3]):
                print ("NO TIENES SUFICIENTE STOCK DEL PRODUCTO")
            else:
                resultado_resta=(int(registro_producto[3])- int(cantidad))
                registro_producto[3]=str(resultado_resta)
                subtotal= (int(registro_producto[2])*int(cantidad))+subtotal
                prod=(",").join(registro_producto)
                lista_productos[pos]=prod
        else:
            pos =pos +1
    if len(lista_productos) == pos:
        print (" EL PRODUCTO NO SE ENCUENTRA EN STOCK")

    productos=("#").join(lista_productos)
   
    return productos, subtotal




#codigo principal (main)
longPass=0
while longPass != 6 and longPass!= 8:
    longPass= menuLogin()


    if longPass == 6:
        modoVendedor=0
        while modoVendedor != 4:
            modoVendedor= menuVendedores()

            if modoVendedor == 1:
                menu_ventas()
         #   elif modoVendedor ==2:

           # elif modoVendedor ==3:
                
         #   elif modoVendedor ==4:

          #  else:
               # print("elige una opcion entre el 1 y el 4")
                #input()
    elif longPass == 8:
        
        while True:

            modoAdmin=menuAdministrador()
            if modoAdmin == 1:
                
                while True:
                    opcion_admin=menuAMEUsuarios()
                    if opcion_admin==1:
                        agregarUsuario()
                    elif opcion_admin==2:
                        menuModificarUsuario()
                    elif opcion_admin==3:
                        eliminarUsuario()
                    elif opcion_admin==4:
                        break
                    else : 
                       print( "INGRESE UN VALOR CORRECTO")
                       input()

            elif modoAdmin == 2:
                menuModificarStock()
            elif modoAdmin ==3:
                break
            else:
                print ("QUIERES MODIFICAR USUARIO ELIGE 1 Y SI QUIERES MODIFICAR STOCK ELIGE 2")
                input()       
             
        
    else :
        print (" ACCESO DENEGADO")
        input ()



        
     

