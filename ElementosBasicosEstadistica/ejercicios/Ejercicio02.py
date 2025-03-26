import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_proyecto = pd.read_excel('ElementosBasicosEstadistica/docs/ejercicio02/proyecto1.xlsx')
df_sucursal = pd.read_excel('ElementosBasicosEstadistica/docs/ejercicio02/Catalogo_sucursal.xlsx')

# Si no existe 'MargenUtilidad', asignar valor por defecto
if 'MargenUtilidad' not in df_sucursal.columns:
    df_sucursal['MargenUtilidad'] = 15

# Ventas totales
vt = df_proyecto['ventas_tot'].sum()
print("Ventas totales:", vt)

# Socios con y sin adeudo
total = len(df_proyecto)
con_adeudo = len(df_proyecto[df_proyecto['B_adeudo'] == 'Con adeudo'])
sin_adeudo = len(df_proyecto[df_proyecto['B_adeudo'] == 'Sin adeudo'])
porc_con = (con_adeudo / total) * 100
porc_sin = (sin_adeudo / total) * 100
print(f"Con adeudo: {con_adeudo} ({porc_con:.2f}%)")
print(f"Sin adeudo: {sin_adeudo} ({porc_sin:.2f}%)")

# Gráfica de ventas totales vs. tiempo
df_vt = df_proyecto.groupby('B_mes')['ventas_tot'].sum().reset_index()
# Convertir a formato fecha sin la parte de la hora
df_vt['B_mes'] = pd.to_datetime(df_vt['B_mes']).dt.strftime('%Y-%m-%d')
x = range(len(df_vt))
plt.bar(x, df_vt['ventas_tot'], color='#AEC6CF', width=0.6, edgecolor='black', linewidth=2)
plt.xticks(x, df_vt['B_mes'], rotation=45)
plt.title("Ventas totales por mes")
plt.tight_layout()
plt.show()

# Gráfica de desviación estándar de pagos vs. tiempo
df_std = df_proyecto.groupby('B_mes')['pagos_tot'].std().reset_index()
df_std['B_mes'] = pd.to_datetime(df_std['B_mes']).dt.strftime('%Y-%m-%d')
x2 = range(len(df_std))
plt.bar(x2, df_std['pagos_tot'], color='#854aa1', width=0.6, edgecolor='black', linewidth=2)
plt.xticks(x2, df_std['B_mes'], rotation=45)
plt.title("Desviación estándar de pagos")
plt.tight_layout()
plt.show()

# Deuda total
deuda_total = df_proyecto['adeudo_actual'].sum()
print("Deuda total:", deuda_total)

# Porcentaje de utilidad
utilidad = vt - deuda_total
porc_util = (utilidad / vt * 100) if vt != 0 else 0
print(f"Porc. utilidad: {porc_util:.2f}%")

# Gráfico circular de ventas por sucursal
df_merged = pd.merge(df_proyecto, df_sucursal, on='id_sucursal', how='left')
df_suc = df_merged.groupby('suc')['ventas_tot'].sum().reset_index()
n = len(df_suc)
cmap = plt.get_cmap('Pastel1', lut=n)
colors = [cmap(i) for i in range(n)]
plt.pie(df_suc['ventas_tot'], labels=df_suc['suc'], colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Ventas por sucursal")
plt.show()

# Gráfico de barras: Deudas Totales vs. Margen de Utilidad por sucursal
df_merged = pd.merge(df_proyecto, df_sucursal, on='id_sucursal', how='left')
df_deuda = df_merged.groupby('suc')['adeudo_actual'].sum().reset_index()
df_margen = df_sucursal[['suc', 'MargenUtilidad']].drop_duplicates()
df_final = pd.merge(df_deuda, df_margen, on='suc', how='left')

ind = np.arange(len(df_final))
bar_width = 0.4

fig, ax1 = plt.subplots(figsize=(10,6))
ax2 = ax1.twinx()

# Barras para Deuda Total (eje izquierdo)
bar1 = ax1.bar(ind, df_final['adeudo_actual'],
                width=bar_width,
                color='#77DD77',
                edgecolor='black',
                linewidth=2,
                label='Deuda')

# Barras para Margen de Utilidad (eje derecho)
bar2 = ax2.bar(ind, df_final['MargenUtilidad'],
                width=bar_width,
                color='#CBAACB',
                edgecolor='black',
                linewidth=2,
                label='Margen Utilidad',
                alpha=0.7)

ax1.set_ylabel("Deuda Total", color='#77DD77')
ax2.set_ylabel("Margen de Utilidad", color='#CBAACB')
ax1.tick_params(axis='y', labelcolor='#77DD77')
ax2.tick_params(axis='y', labelcolor='#CBAACB')

plt.xticks(ind, df_final['suc'], rotation=45)
plt.title("Deudas Totales vs. Margen de Utilidad (Dos Ejes Y)")
fig.tight_layout()
plt.show()