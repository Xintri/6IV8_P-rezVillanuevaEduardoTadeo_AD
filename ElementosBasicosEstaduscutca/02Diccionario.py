import pandas as pd

##Escribir una funcion que reciva un diccionario con las notas de los estudiantes del curso y devuelve una serie con minimo, maximo, media, desviacion critica

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticas = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index = ['Minimo', 'Maximo', 'Media', 'Desviacion estandar'])

    return estadisticas

def  aprobados(notas):
    notas = pd.Series(notas)

    return notas[notas >= 6].sort_values(ascending=False)


notas = {"Jaun": 0, "Juana": 10, "Pepe":9 , "Roman":1, "Maximiliano": 8, "Envi":7, "Icarus":6}

print(estadistica_notas(notas))
print(aprobados(notas))