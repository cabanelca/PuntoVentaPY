import random
def generador_contrasena(longitud):
    minus="abcdefghijklmnopqrstuwxyz"

    

    muestra=random.sample(minus,longitud)
    password="".join(muestra)
    return password
    

contrasena=generador_contrasena(8)
print(contrasena)