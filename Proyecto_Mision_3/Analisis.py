"""

crear entorno virtual --> recordar estar dentro de la carpeta Raiz /PROYECTO_MISION_3/
python -m venv Proyecto 3

installar librerias
pip install pandas
pip install matplotlib
pip install flask
python.exe -m pip install --upgrade pip

Después ingresar al entorno en el cmd dentro de la carpeta raiz 
Proyecto3/Scripts/Activate --> ingresar al ambiente virtual
Ejecutar el archivo python py inicio.py
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask

df = pd.read_csv("csv/Dispositivos_conectados_en_las_zonas_wifi_del_distrito_de_Cartagena_20250508.csv")
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

def graficarDispersion():
    # Crear gráfico de dispersión
    print("\n Generando gráficos de Dispersion \n")
    plt.scatter(ColumnaAÑO,ColumnaZONAWIFI,color="orange")
    plt.title("PERSONAS CONECTADAS POR AÑO A LA WIFI")
    plt.xlabel("Año")
    plt.ylabel("Personas")
    plt.tight_layout()
    plt.savefig('static/images/dispersion1.png')
    plt.close()

    plt.scatter(ColumnaMES, ColumnaCORREGIMIENTOBARRIO, color="orange")
    plt.title("PERSONAS CONECTADAS POR MES EN CORREGIMIENTO/BARRIO")
    plt.xlabel("MES")
    plt.xticks(rotation=90)
    plt.ylabel("CORREGIMIENTO/BARRIO")
    plt.tight_layout()
    plt.savefig('static/images/dispersion2.png')
    plt.close()

    plt.scatter(ColumnaMES, ColumnaZONAWIFI,color="green")
    plt.title("CONSUMO POR PERSONA EN MES POR CORREGIMIENTO/BARRIO DE WIFI")
    plt.xlabel("MES")
    plt.xticks(rotation=90)
    plt.ylabel("CORREGIMIENTO/BARRIO")
    plt.tight_layout()
    plt.savefig('static/images/dispersion3.png')
    plt.close()

    plt.scatter(ColumnaMES, ColumnaSMARTPHONE, color="purple")
    plt.title("SMARTPHONE conectados a wifi por MES")
    plt.xlabel("MES")
    plt.ylabel("Personas")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('static/images/dispersion4.png')
    plt.close()

    plt.scatter(ColumnaMES, ColumnaPC, color="skyblue")
    plt.title("ORDENADORES conectados a wifi por MES")
    plt.xlabel("MES")
    plt.ylabel("Personas")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('static/images/dispersion5.png')
    plt.close()

    plt.scatter(ColumnaMES, ColumnaTABLET, color="skyblue")
    plt.title("TABLETS conectados a wifi por MES")
    plt.xlabel("MES")
    plt.ylabel("Personas")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('static/images/dispersion6.png')
    plt.close()


def graficarBarras():
    # Crear gráfico de barras
    print("\n Generando gráficos de Barras \n")
    plt.bar(ColumnaMES, ColumnaSMARTPHONE, color="skyblue")
    plt.title("SMARTPHONE conectados a wifi por MES")
    plt.xlabel("MES")
    plt.ylabel("Personas")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('static/images/barras1.png')
    plt.close()

    plt.bar(ColumnaMES, ColumnaPC, color="skyblue")
    plt.title("ORDENADORES conectados a wifi por MES")
    plt.xlabel("MES")
    plt.ylabel("Personas")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('static/images/barras2.png')
    plt.close()

    plt.bar(ColumnaMES, ColumnaTABLET, color="skyblue")
    plt.title("TABLETS conectados a wifi por MES")
    plt.xlabel("MES")
    plt.ylabel("Personas")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('static/images/barras3.png')
    plt.close()

def graficarHistograma():
    # Crear histograma
    print("\n Generando gráficos de Histograma \n")
    plt.hist(ColumnaAÑO, bins=5, color="orange", edgecolor="black")
    plt.title("PERSONAS CONECTADAS POR AÑO")
    plt.xlabel("Año")
    plt.ylabel("Personas")
    plt.tight_layout()
    plt.savefig('static/images/histograma1.png')
    plt.close()

    plt.hist(ColumnaMES, bins=5, color="orange", edgecolor="black")
    plt.title("PERSONAS CONECTADAS POR MES")
    plt.xlabel("MES")
    plt.ylabel("Personas")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('static/images/histograma2.png')
    plt.close()

    plt.hist(ColumnaCORREGIMIENTOBARRIO, bins=26, color="orange", edgecolor="black")
    plt.title("PERSONAS CONECTADAS POR CORREGIMIENTO/BARRIO")
    plt.xlabel("CORREGIMIENTO/BARRIO")
    plt.xticks(rotation=90)
    plt.ylabel("Personas")
    plt.tight_layout()
    plt.savefig('static/images/histograma3.png')
    plt.close()

    plt.hist(ColumnaZONAWIFI, bins=26, color="green", edgecolor="black")
    plt.title("CONSUMO POR PERSONA EN CORREGIMIENTO/BARRIO DE WIFI")
    plt.xlabel("CORREGIMIENTO/BARRIO")
    plt.xticks(rotation=90)
    plt.ylabel("Personas")
    plt.tight_layout()
    plt.savefig('static/images/histograma4.png')
    plt.close()

    plt.hist(ColumnaSMARTPHONE, bins=26, color="green", edgecolor="black")
    plt.title("PERSONAS EN SMARTPHONE UTILIZANDO WIFI")
    plt.xlabel("SMARTPHONE CONECTADOS")
    plt.xticks(rotation=90)
    plt.ylabel("Personas")
    plt.tight_layout()
    plt.savefig('static/images/histograma5.png')
    plt.close()

    plt.hist(ColumnaTABLET, bins=26, color="green", edgecolor="black")
    plt.title("PERSONAS EN TABLET UTILIZANDO WIFI")
    plt.xlabel("TABLETS CONECTADOS")
    plt.xticks(rotation=90)
    plt.ylabel("Personas")
    plt.tight_layout()
    plt.savefig('static/images/histograma6.png')
    plt.close()

    plt.hist(ColumnaPC, bins=26, color="green", edgecolor="black")
    plt.title("PERSONAS EN ORDENADORES UTILIZANDO WIFI")
    plt.xlabel("ORDENADORES CONECTADOS")
    plt.xticks(rotation=90)
    plt.ylabel("Personas")
    plt.tight_layout()
    plt.savefig('static/images/histograma7.png')
    plt.close()
#crear graficas
graficarDispersion()
graficarBarras()
graficarHistograma()




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