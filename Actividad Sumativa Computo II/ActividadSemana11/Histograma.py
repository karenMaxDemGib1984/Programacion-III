import matplotlib.pyplot as plt

# Datos de la encuesta (minutos que tardan en llegar a la universidad)
tiempos = [90, 45, 15, 120, 30, 20, 30, 30, 75, 120]

# Crear el histograma
plt.hist(tiempos, bins=5, color='blue', edgecolor='black')

# Agregar título y etiquetas
plt.title('Tiempo que tardan en llegar a la Universidad (en minutos)')
plt.xlabel('Minutos')
plt.ylabel('Número de personas')

# Mostrar la gráfica
plt.show()
