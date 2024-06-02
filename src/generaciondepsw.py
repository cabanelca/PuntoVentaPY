import random

minus="abcdefghijklmnopqrstuwxyz"
mayus="ABCDEFGHIJKLMNOPQRSTUWXYZ"
numeros="0123456789"
simb=".,:;_-¨´@·#~$%&/=?¿"

base=minus
longitud=6

muestra=random.sample(base,longitud)
password="".join(muestra)
print(password)

