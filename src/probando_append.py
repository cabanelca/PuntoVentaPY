def agregar_archivo(contenido, nombre_archivo):
    archivo=open(nombre_archivo,"a")
    archivo.write("#"+contenido) 
    archivo.close()
usuario="1111"
agregar_archivo(usuario, "prueba.txt")
usuario="ababa"
agregar_archivo(usuario,"prueba.txt")



lista="#1111#ababa".split("#")
print(len(lista))