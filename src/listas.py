articulos= "1,galleta,2000,20#2,gaseosa,3000,20"
articulo_lista= articulos.split("#")
galleta= articulo_lista[1]
galleta_columna= galleta.split(",")
galleta_precio=galleta_columna[2]
galleta_precio="4000"
galleta_columna[2]= '5000'


print('variable string articulos = ' +articulos)
print('variable lista después del split: ', end='')
print(articulo_lista)

print('articulo [1] del anterior: ' + galleta)
print('galleta convertido a "lista": ', end= '')
print(galleta_columna)

print('galleta[2]:' + galleta_columna[2])
print('variable string galleta precio:' + galleta_precio)
galleta_modificada=",".join(galleta_columna)
print ("galleta modificada: " + galleta_modificada)
articulo_lista[1]=galleta_modificada   
print (articulo_lista)
nuevo_articulos= "#".join(articulo_lista)
print (nuevo_articulos)


lis_NombreProducto=["coca", "pepsi"]

lis_NombreProducto[0]= "coca cola"
lis_NombreProducto.insert(1, "Fanta")

print (lis_NombreProducto)