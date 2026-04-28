import matplotlib.pyplot as plt

# Crear carpeta resultados si no existe
import os
if not os.path.exists("resultados"):
    os.makedirs("resultados")

# Gráfica simple
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x, y)
plt.title("Gráfica ejemplo")

plt.savefig("resultados/grafica1.png")
plt.savefig("resultados/grafica2.eps")

plt.close()