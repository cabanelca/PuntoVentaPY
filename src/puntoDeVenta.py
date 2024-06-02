import os
from io import open


def crear_archivo(nombre):
    archivo= open(nombre,"w")
    archivo.close()
def sobreescribir_archivo(contenido, nombre_archivo):
    archivo=open(nombre_archivo,"w")
    
    archivo.write(contenido)
   
    archivo.close()

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
    opcionAdministrador = input("ELIGE UNA OPCION VALIDA")
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
    print ("1- MODIFICAR USUARIO ")
    print ("2- AGREGAR USUARIO ")
    print ("3- ELIMINAR USUARIO ")

    opcionAMEUsuario = input("ELIJA UNA OPCION VALIDA")
    return (int(opcionAMEUsuario))

def menuModificarStock(): #nos muestra el menu donde poder modificar el Stock, consultarlo y agregar un articulo
    borrarPantalla()
    print ("1- MODIFICAR PRODUCTO")
    #print ("2- MODIFICAR PRECIO ")
    print ("2- AGREGAR PRODUCTO")

    opcionModificarStock= input(" ELIJA UNA OPCION VALIDA ")

def agregarUsuario():
    borrarPantalla()
    print  ("AGREGAR NUEVO USUARIO") 
    usuario= input("NOMDE DEL NUEVO USUARIO: ")
    password="12345678"# aca iria generador de contraseña.
    #agregar a archivo correspondiente de usuario y de contraseña.
    print ("EL NUEVO USUARIO ES:" + usuario)
    print ("SU CONTRASEÑA ES:" + password)

def modificarUsuario():
    borrarPantalla()
    print( "INGRESE EL USUARIO QUE DESEA MODIFICAR")


def eliminarUsuario():
    borrarPantalla()
    print (" ELIJA EL USUARIO A ELIMINAR: ")
def modificar_articulo():
    borrarPantalla()
    print("ELIJA EL ARTICULO A MODIFICAR")
def agregar_articulo():
    borrarPantalla()
    print("INGRESE EL ARTICULO A AGREGAR")
def menu_ventas():
    productos=leer_archivo("productos.txt")
    totalventa=0
    while True:
        borrarPantalla()
        print("VENTAS DE PRODUCTOS")
        pro_vendido= input("INGRESE EL PRODUCTO A AGREGAR: ")
        cantidad=input("INGRESE LA CANTIDAD QUE VA A COMPRAR: ")
        productos= registrar_ventas(productos,pro_vendido,cantidad)
        fin=input("DESEAS SEGUIR COMPRANDO: ")
        if fin == "no":
            break
    sobreescribir_archivo(productos,"productos.txt")
   
    print(" TU SALDO A PAGAR ES= "+ str(totalventa))
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
   
    return productos




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
        modoAdmin=0
        while modoAdmin !=1 and modoAdmin !=2:

            modoAdmin=menuAdministrador()
            if modoAdmin == 1:
                opcion_admin=0
                while opcion_admin!=1 and opcion_admin !=2 and opcion_admin !=3:
                    opcion_admin=menuAMEUsuarios()
                    if opcion_admin==1:
                        agregarUsuario()
                    elif opcion_admin==2:
                        modificarUsuario()
                    elif opcion_admin==3:
                        eliminarUsuario()
                    else : 
                        "INGRESE UN VALOR CORRECTO"

            elif modoAdmin == 2:
                menuModificarStock()
            else:
                print ("QUIERES MODIFICAR USUARIO ELIGE 1 Y SI QUIERES MODIFICAR STOCK ELIGE 2")
                input()       
             
        
    else :
        print (" ACCESO DENEGADO")
        input ()



        
     
#menuAdministrador()
#menuVendedores()
#menuAMEUsuarios()
#menuModificarStock()
