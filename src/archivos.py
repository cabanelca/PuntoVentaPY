f1=open("login.txt","w")
f1.close()

f2=open("password.txt","w")
f2.close()

f1=open("login.txt","r+")
usuario=input("escribi tu usuario")
f1.write(usuario)
f1.close()

f2=open("password.txt","r+")
clave=input("escribe tu clave")
clavecifrada=cifrado(clave)
f2.write(clavecifrada)
f2.close()



def validar(login,password):
  bandera=0
  f1=open("login.txt","r")
  f2=open("password.txt","r")
  listlog=f1.readlines()
  listpass=f2.readlines()
  f1.close()
  f2.close()

  i=listlog.index(login)
  if password==listpass[i]:
   bandera=1
  return bandera

def verificar(login,password):
  resultado=verificar(login)*verificar(password)
  if resultado!=0: #posible usuario
    if validar(login,password)!=0:
      if len(password)==8:
        menuAD()
      elif(password)==6:
        menuUS()
      else:
        print("no existe")

