# Calcular la distancia entre todos los pares de puntos y determinar
# cuáles están más alejados y más cercanos entre sí, utilizando
# las distancias Euclidiana, Manhattan y Chebyshev

# Importar librerías
import pandas as pd
import numpy as np
from scipy.spatial import distance

# Definir las coordenadas de los puntos
puntos = {
    "Punto A": (2, 3),
    "Punto B": (5, 4),
    "Punto C": (1, 1),
    "Punto D": (6, 7),
    "Punto E": (3, 5),
    "Punto F": (8, 2),
    "Punto G": (4, 6),
    "Punto H": (2, 1)
}

# Convertir puntos a un DataFrame
df_puntos = pd.DataFrame.from_dict(puntos, orient='index', columns=["X", "Y"])
print("Coordenadas de los puntos:")
print(df_puntos)

def calcular_distancias(df_puntos):
    # Crear DataFrames vacíos para almacenar las distancias
    distancia_eu = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
    distancia_mh = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
    distancia_ch = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)

    # Calcular distancias
    for i in df_puntos.index:
        for j in df_puntos.index:
            # Calcular todas las distancias (incluyendo cuando i == j)
            distancia_eu.loc[i, j] = distance.euclidean(df_puntos.loc[i], df_puntos.loc[j])
            distancia_mh.loc[i, j] = distance.cityblock(df_puntos.loc[i], df_puntos.loc[j])
            distancia_ch.loc[i, j] = distance.chebyshev(df_puntos.loc[i], df_puntos.loc[j])

    return distancia_eu, distancia_mh, distancia_ch

# Calcular distancias
distancia_eu, distancia_mh, distancia_ch = calcular_distancias(df_puntos)

# Mostrar tabla de distancias Euclidianas
print("\nTabla de distancias Euclidianas:")
print(distancia_eu)

# Encontrar la distancia máxima y los puntos correspondientes (Euclidiana)
valor_maximo = distancia_eu.astype(float).values.max()
(punto1, punto2) = distancia_eu.stack().astype(float).idxmax()

print("\nDistancia máxima (Euclidiana):", valor_maximo)
print("Entre los puntos:", punto1, "y", punto2)

# Otra manera de obtener la misma información
max_value = distancia_eu.max().max()
col_max = distancia_eu.max().idxmax()
id_max = distancia_eu[col_max].idxmax()

print("\nMétodo alternativo:")
print(f"Valor máximo: {max_value}")
print(f"Columna: {col_max}")
print(f"Índice: {id_max}")

# Mostrar tabla de distancias Manhattan
print("\nTabla de distancias Manhattan:")
print(distancia_mh)

# Encontrar la distancia máxima y los puntos correspondientes (Manhattan)
valor_maximo = distancia_mh.astype(float).values.max()
(punto1, punto2) = distancia_mh.stack().astype(float).idxmax()

print("\nDistancia máxima (Manhattan):", valor_maximo)
print("Entre los puntos:", punto1, "y", punto2)

# Otra manera de obtener la misma información
max_value = distancia_mh.max().max()
col_max = distancia_mh.max().idxmax()
id_max = distancia_mh[col_max].idxmax()

print("\nMétodo alternativo:")
print(f"Valor máximo: {max_value}")
print(f"Columna: {col_max}")
print(f"Índice: {id_max}")

# Mostrar tabla de distancias Chebysev
print("\nTabla de distancias Chebysev:")
print(distancia_ch)

# Encontrar la distancia máxima y los puntos correspondientes (Chebysev)
valor_maximo = distancia_ch.astype(float).values.max()
(punto1, punto2) = distancia_ch.stack().astype(float).idxmax()

print("\nDistancia máxima (Chebysev):", valor_maximo)
print("Entre los puntos:", punto1, "y", punto2)

# Otra manera de obtener la misma información
max_value = distancia_ch.max().max()
col_max = distancia_ch.max().idxmax()
id_max = distancia_ch[col_max].idxmax()

print("\nMétodo alternativo:")
print(f"Valor máximo: {max_value}")
print(f"Columna: {col_max}")
print(f"Índice: {id_max}")
