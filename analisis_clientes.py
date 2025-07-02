import pandas as pd

#Leer los datos del archivo CSV

df = pd.read_csv("Clientes_telecom.csv")

#mostar estructura

print("Columnas")
print(df.columns)
print("Primeras filas:")
print(df.head())

#conteo por estado de servicio

print("Etsado del servicio")
print(df["Estado servico"].value_counts())
