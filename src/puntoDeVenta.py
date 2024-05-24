import os

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

borrarPantalla()


def menuLogin():
    print("Bienvenido")
    print("Punto de Venta")
    print("\n")
    usuario=  input("Usuario: ")

    password= input("Contraseña: ")

menuLogin()

