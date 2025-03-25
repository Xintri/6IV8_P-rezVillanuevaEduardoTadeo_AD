import numpy as np
import matplotlib.pyplot as plt

#Crear semilla random para reproductibilidad
np.random.seed(0)

#Buscar paramtreos para una distribución
#Media
media = 0

#Desviaciones estandar
sigma1 = 1
sigma2 = 2
sigma3 = 3

#Numero de muestras para analizis
n_muestras = 1000

#Datos de las distribuciones normales
datos1 = np.random.normal(media, sigma1, n_muestras)
datos2 = np.random.normal(media, sigma2, n_muestras)
datos3 = np.random.normal(media, sigma3, n_muestras)

#Configurar gráfica
plt.figure(figsize=(10,6))

#Cargar las frecuencias a partir de una gráfica de histogramas
plt.hist(datos1, bins=30, color='blue', density=True, label='desviacion estandar = 1', alpha=0.5)
plt.hist(datos2, bins=30, color='red', density=True, label='desviacion estandar = 2', alpha=0.5)
plt.hist(datos3, bins=30, color='green', density=True, label='desviacion estandar = 3', alpha=0.5)

#a graficar
plt.title("Comparación de distribuciones normales con una semilla random")
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()
plt.grid()

plt.show()
