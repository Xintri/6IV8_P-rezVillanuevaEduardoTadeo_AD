import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("ElementosBasicosEstadistica/docs/ejercicio01/housing.csv")

df_subset = df.iloc[10000:15001].copy()

columnas = ['median_house_value', 'total_bedrooms', 'population']
estadisticas = {}

for col in columnas:
    datos = df_subset[col].dropna()
    media_val = datos.mean()
    mediana_val = datos.median()
    moda_val = datos.mode()
    moda_val = moda_val.iloc[0] if not moda_val.empty else np.nan
    rango_val = datos.max() - datos.min()
    varianza_val = datos.var()
    desv_std_val = datos.std()
    estadisticas[col] = {
        "Media": media_val,
        "Mediana": mediana_val,
        "Moda": moda_val,
        "Rango": rango_val,
        "Varianza": varianza_val,
        "Desviacion Estandar": desv_std_val
    }

df_estadisticas = pd.DataFrame(estadisticas).transpose()

bins = 10
df_subset['mhv_bins'] = pd.cut(df_subset['median_house_value'], bins=bins)
tabla_frecuencias = df_subset['mhv_bins'].value_counts().sort_index()

print("Estadísticas Descriptivas:")
print(df_estadisticas)
print("\nTabla de Frecuencias para 'median_house_value':")
print(tabla_frecuencias)


plt.figure(figsize=(8,6))
plt.hist(df_subset['median_house_value'].dropna(), bins=20, edgecolor='black')
media_mhv = df_subset['median_house_value'].mean()
plt.axvline(media_mhv, color='red', linestyle='dashed', linewidth=1,
            label=f'Media: {media_mhv:.2f}')
plt.xlabel('median_house_value')
plt.ylabel('Frecuencia')
plt.title('Histograma de median_house_value (filas 10,000 a 15,000)')
plt.legend()
plt.show()

medias = [estadisticas[col]["Media"] for col in columnas]
plt.figure(figsize=(8,6))
plt.bar(columnas, medias, color=['blue', 'green', 'orange'])
plt.ylabel('Valor Medio')
plt.title('Comparación de Medias: median_house_value, total_bedrooms, population')
for i, valor in enumerate(medias):
    plt.text(i, valor, f'{valor:.2f}', ha='center', va='bottom')
plt.show()
