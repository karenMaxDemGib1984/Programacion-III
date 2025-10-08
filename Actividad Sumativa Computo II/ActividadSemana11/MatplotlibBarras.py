#Cuantas tazas de café tomas al día.

import matplotlib.pyplot as plt

# Datos
categorias = ["O tazas","1 taza", "2 tazas", "4 tazas"]
valores = [5, 1, 2, 2]

# Crear gráfico de barras
plt.bar(categorias, valores, color="Crimson")

# Personalización
plt.title("¿Cuántas tazas de cafe tomas al día?")
plt.xlabel("Tazas de cafe")
plt.ylabel("Personas")
plt.yticks(range(0, 8, 1))


# Mostrar
plt.show() 