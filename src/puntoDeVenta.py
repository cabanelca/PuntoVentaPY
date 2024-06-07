import os
import random
from io import open

def validacion_login(usuario, clave):
    usuario_txt=leer_archivo("usuario.txt")
    password_txt=leer_archivo("password.txt")
    lista_usuario=usuario_txt.split("#")
    lista_clave=password_txt.split("#")
    pos=0
    clave_cifrada=cifrado(clave)
    for usuario_exitente in lista_usuario:
        if usuario_exitente==usuario:
            if lista_clave[pos]==clave_cifrada:
                print(" ACCESO")
                input()
                return True
            else:
                
                return False
        else:
            pos = pos +1
   
    
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
    valor=validacion_login(usuario, password)
    if valor == True:
        return len(password)
    else:
        return 3
def menuAdministrador():# nos muestra el menu de administrador 
    borrarPantalla()
    print ("PUNTO DE VENTA")
    print ("MODO ADMINISTRADOR")
    print ("\n")
    print ("1- ADMINISTRAR USUARIOS")
    print ("2- ADMINISTRAR STOCK")
    print ("3- SALIR DEL PROGRAMA")
    opcionAdministrador = input("ELIGE UNA OPCION VALIDA: ")
    return (int(opcionAdministrador))

def menuVendedores():# nos muestra el menu de los vendedores
    borrarPantalla()
    print ("ELIJA UNA OPCIÓN DEL MENU ")
    print ("1-  VENDER ")
    print ("2- BUSCAR PRODUCTO")
    print ("3-  SALIR ")
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
    
    while True:
        borrarPantalla()
        print ("1- AGREGAR PRODUCTO")
        #print ("2- MODIFICAR PRECIO ")
        print ("2- MODIFICAR PRODUCTO")
        print ("3- ELIMINAR PRODUCTO")
        print ("4- VOLVER A LA PANTALLA ANTERIOR")
        opcionModificarStock= int(input(" ELIJA UNA OPCION VALIDA: "))
        if opcionModificarStock==1:
            menu_agregar_producto()
                
        elif opcionModificarStock==2:
            producto=input("INGRESE EL PRODUCTO A MODIFICAR: ")
            modificar_producto(producto)
            input()
        elif opcionModificarStock==3:
            producto=input("INGRESE EL PRODUCTO A ELIMINAR DE TU STOCK: ")
            eliminar_producto(producto)            
            input()
        elif opcionModificarStock==4:
            break
        else:
            print("ELIGE UNA OPCION ENTRE EL 1 Y EL 4")
            input()

def agregarUsuario():
    borrarPantalla()
    print  ("AGREGAR NUEVO USUARIO") 
    usuario= input("NOMBRE DEL NUEVO USUARIO: ")
    respuesta=input("¿TU USUARIO ES ADMIN? ")
    long=6
    if respuesta=="si":
        long=8
    password=generador_contrasena(long)
    print ("EL NUEVO USUARIO ES: " + usuario)
    input()
    print ("SU CONTRASEÑA ES: " + password)
    input()
    contrasena_cifrada= cifrado(password)
    agregar_archivo(usuario, "usuario.txt")
    agregar_archivo(contrasena_cifrada, "password.txt")
   
def menuModificarUsuario():
    borrarPantalla()
    print ("ESTAS POR MODIFICAR UN USUARIO")
    usuario= input( "INGRESE EL USUARIO QUE DESEA MODIFICAR: ")
    respuesta=input("¿TU USUARIO ES ADMIN? ")
    long=6
    if respuesta=="si":
        long=8
    password=generador_contrasena(long)
    contrasena_cifrada=cifrado(password)
    nuevo_usuario=input(" INGRESE NUEVO USUARIO: ")
    resultado=modificarUsuario(usuario,nuevo_usuario,contrasena_cifrada)
    if resultado==True:
        print ("TU NUEVO USUARIO ES: " + nuevo_usuario)
        input()
        print ("TU CONTRASENA ES : " + password)
        input()
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
def menuEliminarUsuario():
    borrarPantalla()
    print("ESTAS POR ELIMINAR UN USUARIO")
    usuario= input("INGRESA TU USUARIO A ELIMINAR: ")
    resultado =eliminarUsuario(usuario)
    if resultado==True:
        print("TU USUARIO FUE ELIMINADO")
        input()
    else:
        print ("EL USUARIO NO FUE ENCONTRADO")
        input()
    
def eliminarUsuario(usuario):
    borrarPantalla()
    usuario_txt=leer_archivo("usuario.txt")
    password_txt=leer_archivo("password.txt")
    lista_usuario= usuario_txt.split("#")
    lista_password=password_txt.split("#")
    i=0
    for us_existente in lista_usuario:
        if us_existente==usuario:
            lista_usuario[i]=usuario
            lista_password[i]=generador_contrasena(3)
            password_txt=("#").join(lista_password)
            sobrescribir_archivo(password_txt,"password.txt")
            return True
        else:
            i=i+1
    return False
    

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
    #return totalventa
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
def menu_buscar_productos():
    borrarPantalla()
    producto_buscado=input("INGRESE EL PRODUCTO QUE BUSCAS: ")
    buscar_producto(producto_buscado)
   

def buscar_producto(producto):
    productos_txt=leer_archivo("productos.txt")
    lista_productos=productos_txt.split("#")
    pos=0
    for prod in lista_productos:
        registro_producto=prod.split(",")
        if producto == registro_producto[1]:
            print("TU PRODUCTO: "+ registro_producto[1])
            input()

            print ("SU PRECIO ES: " + registro_producto[2])
            input()
            print("Y TE QUEDA EN STOCK: " + registro_producto[3])
            input()
        else:
            pos=pos+1
    if pos==len(lista_productos):
        print("TU PRODUCTO NO ESTA EN NUESTRO LOCAL")
        input()
def menu_agregar_producto():
    borrarPantalla()
    print("VAS A AGREGAR UN PRODUCTO ")
    producto=input("PRODUCTO A AGREGAR: ")
    precio=input("PRECIO A AGREGAR: ")
    cantidad=input("CUAL ES LA CANTIDAD DE TU STOCK: ")
    agregar_producto(producto,precio,cantidad)
    print("TU PRODUCTO FUE AGREGADO EN FORMA CORRECTA")
    input()
    
def agregar_producto(producto, precio, cantidad):
    contenido_anterior=""
    nuevo_id="1"
    if os.path.isfile("productos.txt"):
        contenido_anterior=leer_archivo("productos.txt")
        lista_producto=contenido_anterior.split("#")
        nuevo_id=len(lista_producto)+1
        contenido_anterior=contenido_anterior+"#"
    nuevo_prod=f"{nuevo_id},{producto},{precio},{cantidad}"
    contenido_nuevo=f"{contenido_anterior}{nuevo_prod}"
    sobrescribir_archivo(contenido_nuevo, "productos.txt")



    
def modificar_producto(producto):
    productos_txt=leer_archivo("productos.txt")
    lista_productos=productos_txt.split("#")
    pos =0
    producto_nuevo=input("INGRESA TU PRODUCTO: ")
    precio_nuevo=input("INGRESA EL PRECIO: ")
    stock_nuevo=input("INGRESA TU STOCK: ")
    for prod in lista_productos:
        registro_producto=prod.split(",")
        if producto == registro_producto[1]:
            registro_producto[1]=producto_nuevo
            registro_producto[2]=precio_nuevo
            registro_producto[3]=stock_nuevo
            prod=",".join(registro_producto)
            lista_productos[pos]=prod
        else:
            pos=pos+1
    productos_txt="#".join(lista_productos)
    sobrescribir_archivo(productos_txt, "productos.txt")
    if pos==len(lista_productos):
       print("TU PRODUCTO NO SE ENCUENTRA EN STOCK ")
    else:
        print("TU PRODUCTO SE MODIFICO CON EXITO")
def eliminar_producto(producto):
    productos_txt=leer_archivo("productos.txt")
    lista_productos=productos_txt.split("#")
    pos=0
    for prod in lista_productos:
        registro_producto=prod.split(",")
        if producto == registro_producto[1]:
            registro_producto[3]="0"
            prod= ",".join(registro_producto)
            lista_productos[pos]=prod
        else:
            pos= pos +1
    productos_txt="#".join(lista_productos)
    sobrescribir_archivo(productos_txt, "productos.txt")
    if pos==len(lista_productos):
        print("TU PRODUCTO NO SE ENCUENTRA EN STOCK")
    else:
        print("TU PRODUCTO SE ELIMINO CON EXITO")

#codigo principal (main)
longPass=0
while longPass != 6 and longPass!= 8:
    longPass= menuLogin()
    if longPass == 6:
        while True:
            modoVendedor= menuVendedores()
            if modoVendedor == 1:
               menu_ventas()
               
            elif modoVendedor ==2:
                menu_buscar_productos()     
            elif modoVendedor == 3:
                break
            else:
                print("ELIGE UN VALOR DEL 1 AL 3")
                input()
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
                        menuEliminarUsuario()
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



        
     

