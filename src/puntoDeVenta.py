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
    opcionVendedor = input(" Elije una Opción valida: ")
    return (int(opcionVendedor))
def menuAMEUsuarios(): # nos muestra el menu donde modificar los usuarios
    borrarPantalla()
    print ("1- MODIFICAR USUARIO ")
    print ("2- AGREGAR USUARIO ")
    print ("3- ELIMINAR USUARIO ")

    opcionAMEUsuario = input("Elija una opción correcta: ")
    return (int(opcionAMEUsuario))

def menuModificarStock(): #nos muestra el menu donde poder modificar el Stock, consultarlo y agregar un articulo
    borrarPantalla()
    print ("1- MODIFICAR ARTICULO")
    #print ("2- MODIFICAR PRECIO ")
    print ("2- AGREGAR ARTICULO ")

    opcionModificarStock= input(" Elija una opción valida: ")

def agregarUsuario():
    borrarPantalla()
    print  ("AGREGAR NUEVO USUARIO") 
    usuario= input("Nombre del nuevo usuario: ")
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



#codigo principal (main)
longPass=0
while longPass != 6 and longPass!= 8:
    longPass= menuLogin()


    if longPass == 6:
        modoVendedor=0
        while modoVendedor != 1 and modoVendedor !=2 and modoVendedor != 3 and modoVendedor != 4:
            modoVendedor= menuVendedores()

        #    if modoVendedor == 1:
        
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
                print ("Quieres modificar usuario elige 1 y si quieres modificar stock elige 2")
                input()       
             
        
    else :
        print (" Acceso Denegado ")
        input ()



        
     
#menuAdministrador()
#menuVendedores()
#menuAMEUsuarios()
#menuModificarStock()
