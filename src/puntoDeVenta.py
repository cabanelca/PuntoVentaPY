import os

def borrarPantalla(): #borra pantalla de consola
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def menuLogin():# nos muestra el login
    borrarPantalla()
    print("Bienvenido")
    print("Punto de Venta")
    print("\n")
    usuario=  input("Usuario: ")

    password= input("Contraseña: ")
    return len(password)

def menuAdministrador():# nos muestra el menu de administrador 
    borrarPantalla()
    print ("Punto de Venta")
    print ("Modo Administrador")
    print ("\n")
    print ("1- Administrar Usuarios")
    print ("2- Adiministrar Stock")
    opcionAdministrador = input("Elige una opción valida: ")
    return (int(opcionAdministrador))

def menuVendedores():# nos muestra el menu de los vendedores
    borrarPantalla()
    print ("ELIJA UNA OPCIÓN DEL MENU ")
    print ("1-  VENDER ")
    print ("2- BUSCAR PRODUCTO")
    print ("3- BUSCAR PRODUCTOS EN FALTA")
    print ("4-  SALIR ")
    opciónVendedor = input(" Elije una Opción valida: ")

def menuAMEUsuarios(): # nos muestra el menu donde modificar los usuarios
    borrarPantalla()
    print ("1- MODIFICAR USUARIO ")
    print ("2- AGREGAR USUARIO ")
    print ("3- ELIMINAR USUARIO ")

    opcionAMEUsuario = input("Elija una opción correcta: ")

def menuModificarStock(): #nos muestra el menu donde poder modificar el Stock, consultarlo y agregar un articulo
    borrarPantalla()
    print ("1- MODIFICAR STOCK ")
    print ("2- MODIFICAR PRECIO ")
    print ("3- AGREGAR ARTICULO ")

    opcionModificarStock= input(" Elija una opción valida: ")




#codigo principal (main)
longPass=0
while longPass != 6 and longPass!= 8:
    longPass= menuLogin()


    if longPass == 6:
        menuVendedores()
    elif longPass == 8:
        modoAdmin=0
        while modoAdmin !=1 and modoAdmin !=2:
            modoAdmin=menuAdministrador()
            

            if modoAdmin == 1:
                menuAMEUsuarios()
            elif modoAdmin == 2:
                menuModificarStock()
            else:
                print ("Quieres modificar usuario elige 1 y si quieres modificar stock elige 2")
                input()       
             
        
    else :
        print (" Acceso Denegado ")
        input ()



        
     
#menuAdministrador()
#menuVendedores()
#menuAMEUsuarios()
#menuModificarStock()
