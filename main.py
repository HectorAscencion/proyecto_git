from funciones import suma, resta, multiplicacion
import matplotlib.pyplot as plt
import os
print("Cambio en rama1")
print("Suma:", suma(10, 5))
print("Resta:", resta(10, 5))
print("Multiplicación:", multiplicacion(10, 5))

if not os.path.exists("resultados"):
    os.makedirs("resultados")

x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x, y)
plt.title("Gráfica de ejemplo")

plt.savefig("resultados/grafica1.png")
plt.savefig("resultados/grafica2.eps")

plt.close()

print("Archivos generados correctamente")