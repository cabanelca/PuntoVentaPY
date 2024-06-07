
def grafico(listaY, listaX, cantidadLimite, titulo, detalleX, detalleY):
    import matplotlib.pyplot as plt  
    valorNSGF=[min(valor,cantidadLimite) for valor in listaY]
    valorSSGF=[max(0,valor-cantidadLimite)for valor in listaY]
    plt.bar(listaX,valorNSGF,color="grey",label="stock en falta")
    plt.bar(listaX,valorSSGF,bottom=valorNSGF,color= "blue", label="stock ok")
    plt.axhline(y=cantidadLimite,color="red",linestyle="--", label=f"limite({cantidadLimite})")
    plt.title(titulo)
    plt.xlabel(detalleX)
    plt.ylabel(detalleY)

    plt.show()

costof=300
dias=["L","M","X","J","V","S","D"]
ganancia=[100,200,300,400,500,600,700]
titulo_grafico="PRODUCTOS STOCK"
detalleX="PRODUCTOS"
detalleY="CANTIDAD EN STOCK"
grafico(ganancia, dias, costof, titulo_grafico, detalleX, detalleY)