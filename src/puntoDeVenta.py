import os

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def menuLogin():
    borrarPantalla()
    print("Bienvenido")
    print("Punto de Venta")
    print("\n")
    usuario=  input("Usuario: ")

    password= input("Contraseña: ")
def menuAdministrador():
    borrarPantalla()
    print ("Punto de Venta")
    print ("Modo Administrador")
    print ("\n")
    print ("1- Administrar Usuarios")
    print ("2- Adiministrar Stock")
    opcionAdministrador = input("Elige una opción valida: ")
def menuVendedores():
    borrarPantalla()
    print ("ELIJA UNA OPCIÓN DEL MENU ")
    print ("1-  VENDER ")
    print ("2- Buscar Producto")
    print ("3- Buscar Productos en falta")
    print ("4-  SALIR ")
    opciónVendedor = input(" Elije una Opción valida: ")

def menuAMEUsuarios():
    borrarPantalla()
    print ("1- MODIFICAR USUARIO ")
    print ("2- AGREGAR USUARIO ")
    print ("3- ELIMINAR USUARIO ")

    opcionAMEUsuario = input("Elija una opción correcta: ")

def menuModificarStock():
    borrarPantalla()
    print (" MODIFICAR STOCK ")
    print (" MODIFICAR PRECIO ")
    print (" AGREGAR ARTICULO ")

    opcionModificarStock= input(" Elija una opción valida: ")

#codigo principal (main)
#menuLogin()
#menuAdministrador()
#menuVendedores()
#menuAMEUsuarios()
#menuModificarStock()