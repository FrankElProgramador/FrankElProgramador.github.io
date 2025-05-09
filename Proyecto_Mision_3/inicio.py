import Analisis as ArchivoAnalisis
from flask import Flask, render_template
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import pandas as pd
import numpy as np

#ArchivoAnalisis.graficarBarras()
#ArchivoAnalisis.graficarDispersion()
#ArchivoAnalisis.graficarHistograma()
app = Flask(__name__)
    
@app.route('/')
def principal():
    print("\n Ingresando al inicio \n")
    return render_template('inicio.html')

@app.route('/barras')
def contact():
    print("\n Ingresando a barras \n")
    return render_template('barras.html')

@app.route('/dispersion')
def analysis():
    print("\n Ingresando a dispersion \n")
    return render_template('dispersion.html')

@app.route('/histograma')
def analysis2():
    print("\n Ingresando a histograma \n")
    return render_template('histograma.html')
@app.route('/contacto')
def analysis3():
    print("\n Ingresando a contacto \n")
    return render_template('contacto.html')


if __name__ =='__main__':
    # El modo debug reinicia automáticamente el servidor al hacer cambios,
    # pero es necesario recargar la página en el navegador para ver esos cambios.
    app.run(debug=True)