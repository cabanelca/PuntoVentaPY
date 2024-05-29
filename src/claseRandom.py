import random
def generadorDePas(long):
    pas=""
    cont=0
   
    limite=0

    while cont < long:
        pas =pas +str(random.randint(0,9))
        cont= cont +1

    return pas
long=int(input("Ingrese la longitud de su contraseña: "))
contrasena=generadorDePas(long)
print(contrasena)