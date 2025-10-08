import matplotlib.pyplot as plt

# Datos
x = [2, 4, 5, 6,7,8 ]    # Eje X
y = [1, 1, 1, 1, 5, 1] # Eje Y

# Crear gráfico de líneas
plt.plot(x, y)


plt.plot(x, y, color='blue', linestyle='--', marker='o', label='Horas de sueño')

plt.title("Horas de sueño")
plt.xlabel("Horas de sueño")
plt.ylabel("Personas")

# Mostrar valores del eje Y de 0 a 6 en incrementos de 1
plt.yticks(range(0, 8, 1))

plt.legend()  # Muestra la leyenda
plt.grid(True)  # Muestra una cuadrícula
plt.show()


# Mostrar en pantalla
plt.show()
