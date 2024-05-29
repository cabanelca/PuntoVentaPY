from io import open


def crear_archivo(nombre):
    archivo= open(nombre,"w")
    archivo.close()
def escribir_archivo(contenido, nombre):
    archivo=open(nombre,"a")
    
    archivo.write(contenido + "\n")
   
    archivo.close()

def leer_archivo(nombre):
    archivo= open(nombre, "r")
    contenido = archivo.read()
    archivo.close()
    return contenido
nombre_archivo="Usuarios.txt"
crear_archivo(nombre=nombre_archivo)
nombre_archivo="Articulos.txt"
crear_archivo(nombre=nombre_archivo)
nombre_archivo="Ventas.txt"
crear_archivo(nombre=nombre_archivo)
nombre_archivo="Usuarios.txt"
crear_archivo(nombre=nombre_archivo)




variableFrase= input("Ingrese Frase: ")
escribir_archivo(cliente=variableFrase)
