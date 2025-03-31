import numpy as np
import pandas as pd
from scipy.spatial import distance

#Definir coordenadas de tienas (simulando q ahí están)
tiendas = {
    '3B':(1,1),
    'Juan':(1,5),
    'de Pk':(7,1),
    'JoseMaria':(3,3),
    'El Zorro':(4,8)
}

#Convertir coordenadas a un dataframe
df_tienas = pd.DataFrame(tiendas).T
df_tienas.columns = ['x', 'y']
print('coordenadas de las tiendas')
print(df_tienas)

#Inicializamos una distancia euclidiana

distancia_eu = pd.DataFrame(index=df_tienas.index, columns=df_tienas.index)
distancia_mh = pd.DataFrame(index=df_tienas.index, columns=df_tienas.index)
distancia_ch = pd.DataFrame(index=df_tienas.index, columns=df_tienas.index)

#Calcular las distancias
for i in df_tienas.index:
    for j in df_tienas.index:

        #distancias euclidianas
        distancia_eu.loc[i,j] = distance.euclidean(df_tienas.loc[i], df_tienas.loc[j])

        #distancias manhattan
        distancia_mh.loc[i,j] = distance.cityblock(df_tienas.loc[i], df_tienas.loc[j])

        #distancias chbyshev
        distancia_ch.loc[i,j] = distance.chebyshev(df_tienas.loc[i], df_tienas.loc[j])

#Mostrar resultados
print('\nDistancia Euclidianas entre tiendas')
print(distancia_eu)

print('\nDistancia Manhattan entre tiendas')
print(distancia_mh)

print('\nDistancia Chebyshev entre tiendas')
print(distancia_ch)