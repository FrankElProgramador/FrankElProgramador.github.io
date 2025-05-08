import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template
#python.exe -m pip install --upgrade pip
df = pd.read_csv("Proyecto3/csv/Dispositivos_conectados_en_las_zonas_wifi_del_distrito_de_Cartagena_20250508.csv")
#[330 rows x 8 columns]
# AÑO, MES, CORREGIMIENTO/BARRIO, ZONA WIFI, OTRO, SMARTPHONE, TABLET, PC
#print(df.info())    # Información general
"""
#   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   AÑO                   330 non-null    int64
 1   MES                   330 non-null    object
 2   CORREGIMIENTO/BARRIO  330 non-null    object
 3   ZONA WIFI             330 non-null    object
 4   OTRO                  330 non-null    int64
 5   SMARTPHONE            330 non-null    int64
 6   TABLET                330 non-null    int64
 7   PC                    330 non-null    int64
"""
#print(df.describe())   # Estadísticas descriptivas

# Selección de columna por variables
ColumnaAÑO = df["AÑO"]
ColumnaMES = df["MES"]
ColumnaCORREGIMIENTOBARRIO = df["CORREGIMIENTO/BARRIO"]
ColumnaZONAWIFI = df["ZONA WIFI"]
ColumnaOTRO = df["OTRO"]
ColumnaSMARTPHONE = df["SMARTPHONE"]
ColumnaTABLET = df["TABLET"]
ColumnaPC = df["PC"]


# Selección de varias columnas
columna2 = df[["AÑO"]]

# Filtrado de datos
columna3 = df[df["AÑO"] == 2024]


"""
# Crear gráfico de barras
plt.bar(ColumnaAÑO, ColumnaPC, color="skyblue")
plt.title("PC conectados a wifi por Año")
plt.xlabel("Año")
plt.ylabel("Personas")
plt.show()

# Crear gráfico de líneas
plt.plot(ColumnaAÑO, ColumnaPC, marker="o", color="green", linestyle="--")
plt.title("PC conectados a wifi por Año")
plt.xlabel("Año")
plt.ylabel("Personas")
plt.show()

# Crear gráfico de dispersión
plt.scatter(ColumnaAÑO, ColumnaPC, color="purple")
plt.title("PC conectados a wifi por Año")
plt.xlabel("Año")
plt.ylabel("Personas")
plt.show()
"""
# Crear gráfico de dispersión
plt.scatter(ColumnaAÑO,ColumnaZONAWIFI,color="orange")
plt.title("PERSONAS CONECTADAS POR AÑO A LA WIFI")
plt.xlabel("Año")
plt.ylabel("Personas")
plt.tight_layout()
plt.savefig('Proyecto3/static/images/plot.png')
plt.close()
    
def graficarDispersion():
    plt.scatter(ColumnaAÑO,ColumnaZONAWIFI,color="orange")
    plt.title("PERSONAS CONECTADAS POR AÑO A LA WIFI")
    plt.xlabel("Año")
    plt.ylabel("Personas")
    plt.tight_layout()
    plt.savefig('static/images/plot.png')
    plt.close()

    plt.scatter(ColumnaMES, ColumnaCORREGIMIENTOBARRIO, color="orange")
    plt.title("PERSONAS CONECTADAS POR MES EN CORREGIMIENTO/BARRIO")
    plt.xlabel("MES")
    plt.xticks(rotation=90)
    plt.ylabel("CORREGIMIENTO/BARRIO")
    plt.tight_layout()
    plt.show()

    plt.scatter(ColumnaMES, ColumnaZONAWIFI,color="green")
    plt.title("CONSUMO POR PERSONA EN MES POR CORREGIMIENTO/BARRIO DE WIFI")
    plt.xlabel("MES")
    plt.xticks(rotation=90)
    plt.ylabel("CORREGIMIENTO/BARRIO")
    plt.tight_layout()
    plt.show()

    plt.scatter(ColumnaMES, ColumnaSMARTPHONE, color="purple")
    plt.title("SMARTPHONE conectados a wifi por MES")
    plt.xlabel("MES")
    plt.ylabel("Personas")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    plt.scatter(ColumnaMES, ColumnaPC, color="skyblue")
    plt.title("ORDENADORES conectados a wifi por MES")
    plt.xlabel("MES")
    plt.ylabel("Personas")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    plt.scatter(ColumnaMES, ColumnaTABLET, color="skyblue")
    plt.title("TABLETS conectados a wifi por MES")
    plt.xlabel("MES")
    plt.ylabel("Personas")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()







def graficarBarras():
    # Crear gráfico de barras
    plt.bar(ColumnaMES, ColumnaSMARTPHONE, color="skyblue")
    plt.title("SMARTPHONE conectados a wifi por MES")
    plt.xlabel("MES")
    plt.ylabel("Personas")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    plt.bar(ColumnaMES, ColumnaPC, color="skyblue")
    plt.title("ORDENADORES conectados a wifi por MES")
    plt.xlabel("MES")
    plt.ylabel("Personas")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    plt.bar(ColumnaMES, ColumnaTABLET, color="skyblue")
    plt.title("TABLETS conectados a wifi por MES")
    plt.xlabel("MES")
    plt.ylabel("Personas")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()





def graficarHistograma():
    # Crear histograma
    plt.hist(ColumnaAÑO, bins=5, color="orange", edgecolor="black")
    plt.title("PERSONAS CONECTADAS POR AÑO")
    plt.xlabel("Año")
    plt.ylabel("Personas")
    plt.tight_layout()
    plt.show()

    plt.hist(ColumnaMES, bins=5, color="orange", edgecolor="black")
    plt.title("PERSONAS CONECTADAS POR MES")
    plt.xlabel("MES")
    plt.ylabel("Personas")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    plt.hist(ColumnaCORREGIMIENTOBARRIO, bins=26, color="orange", edgecolor="black")
    plt.title("PERSONAS CONECTADAS POR CORREGIMIENTO/BARRIO")
    plt.xlabel("CORREGIMIENTO/BARRIO")
    plt.xticks(rotation=90)
    plt.ylabel("Personas")
    plt.tight_layout()
    plt.show()

    plt.hist(ColumnaZONAWIFI, bins=26, color="green", edgecolor="black")
    plt.title("CONSUMO POR PERSONA EN CORREGIMIENTO/BARRIO DE WIFI")
    plt.xlabel("CORREGIMIENTO/BARRIO")
    plt.xticks(rotation=90)
    plt.ylabel("Personas")
    plt.tight_layout()
    plt.show()

    plt.hist(ColumnaSMARTPHONE, bins=26, color="green", edgecolor="black")
    plt.title("PERSONAS EN SMARTPHONE UTILIZANDO WIFI")
    plt.xlabel("SMARTPHONE CONECTADOS")
    plt.xticks(rotation=90)
    plt.ylabel("Personas")
    plt.tight_layout()
    plt.show()

    plt.hist(ColumnaTABLET, bins=26, color="green", edgecolor="black")
    plt.title("PERSONAS EN TABLET UTILIZANDO WIFI")
    plt.xlabel("TABLETS CONECTADOS")
    plt.xticks(rotation=90)
    plt.ylabel("Personas")
    plt.tight_layout()
    plt.show()

    plt.hist(ColumnaPC, bins=26, color="green", edgecolor="black")
    plt.title("PERSONAS EN ORDENADORES UTILIZANDO WIFI")
    plt.xlabel("ORDENADORES CONECTADOS")
    plt.xticks(rotation=90)
    plt.ylabel("Personas")
    plt.tight_layout()
    plt.show()


#graficarBarras()
#graficarDispersion()
#graficarHistograma()