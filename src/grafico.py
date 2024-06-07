import matplotlib.pyplot as plt

dias=["L","M","X","J","V","S","D"]
ganancia=[100,200,300,400,500,600,700]
costof=300
valorNSGF=[min(valor,costof) for valor in ganancia]
valorSSGF=[max(0,valor-costof)for valor in ganancia]

plt.bar(dias,valorNSGF,color="black",label="por debajo del gasto fijo")
plt.bar(dias,valorSSGF,bottom=valorNSGF,color= "grey", label="ganancia")


plt.axhline(y=costof,color="red",linestyle="--", label=f"costf({costof})")
plt.title("grafico de ganacias")
plt.xlabel("dias")
plt.ylabel("$")

plt.show()