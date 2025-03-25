import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_c = pd.read_excel("ElementosBasicosEstadistica/docs/ejercicio02/Catalogo_sucursal.xlsx")
df_p = pd.read_excel("ElementosBasicosEstadistica/docs/ejercicio02/proyecto1.xlsx")

#Conocer las ventas totales del comercio
print("Ventas totales: ",df_p["ventas_tot"].sum())

#Socios con y sin adeudos
print("Socios:")
print(df_p["B_adeudo"].value_counts())

#Porcentaje de socios con y sin adeudos

print(df_p["B_adeudo"].sum())
