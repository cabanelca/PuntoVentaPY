caracter="abcdefghijklmnopqrstuvwxyz"

listB= list(caracter)
listR=listB.reverse()

clave=""
login=input("LOGIN: ")
listlogin=list(login)

i=0
while i < len(login):
    caracter=listlogin[i]
    j= listB.index(caracter)
    clave= clave+ listR
    i=i+1
print(clave)