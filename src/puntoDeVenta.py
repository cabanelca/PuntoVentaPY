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
    opcion = input("Elige una opción valida: ")

#codigo principal (main)
#menuLogin()
#menuAdministrador()

