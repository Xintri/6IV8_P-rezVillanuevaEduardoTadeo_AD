import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./ElementosBasicosEstaduscutca/housing.csv')

##Mostrar las primeras 5 filas

print(df.head())

##Mostrar las ultimas 5 filas

print(df.tail())

##Fila en especifico

print(df.iloc[7])

##mostrar columna ocean_proximity
print(df["ocean_proximity"])

##Mostrar la media de la columna total_rooms
media_cuarto = df["total_rooms"].mean()
print("Media de cuartos: " + str(media_cuarto))

##Mediana
mediana_cuarto = df["median_house_value"].median()
print("La mediana de cuartos: " + str(mediana_cuarto))

##Suma de popular
salarioTotal = df["population"].sum()
print("El salario total es de: " + str(salarioTotal))

##Filtrar
vamoshacerfiltro = df[df["ocean_proximity"] == "ISLAND"]
print(vamoshacerfiltro)

##Hacer grafico de dispersion

plt.scatter(df["ocean_proximity"][:10], df["median_house_value"][:10])

##Nombramos los ejes
plt.xlabel("proximidad")
plt.ylabel("precio")
plt.title("Grafico de Dispersion de Proximidad al Oceano vs Precio")
plt.show()