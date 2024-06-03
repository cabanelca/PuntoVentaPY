def cifrado(login):
    caracter="abcdefghijklmnopqrstuvwxyz"

    listB= list(caracter)
    listR= list(caracter)
    listR.reverse()

    clave=""
   
    listlogin=list(login)

    i=0
    while i < len(login):
        caracter=listlogin[i]
        j= listB.index(caracter)
        clave= clave+ listR[j]
        i=i+1
    return(clave)

login=input("LOGIN: ")
login_cifrado=cifrado(login)
print(login_cifrado)