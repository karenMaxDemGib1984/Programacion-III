#import PyQt5
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QPushButton,QLineEdit, QMessageBox, QComboBox)

import sys 

def calcularIMC(peso, unidadPeso, estatura, unidadEstatura):
    try:
        peso = float(peso)
        estatura = float(estatura)
        if unidadPeso == "lb":
            peso = peso * 0.453592  
        if unidadEstatura == "cm":
            estatura = estatura / 100  
        imc = peso / (estatura ** 2)
        if imc < 18.5:
            estado = "Bajo peso"
        elif 18.5 <= imc < 25:
            estado = "Normal"
        elif 25 <= imc < 30:
            estado = "Sobrepeso"
        else:
            estado = "Obesidad"

        return imc, estado

    except:
        return None, "Error en los datos"
    

def mensaje():
    p = Peso.text()
    e = Estat.text()
    unidadP = opcionPeso.currentText()
    unidadE = opcionEstatura.currentText()

    imc, estado = calcularIMC(p, unidadP, e, unidadE)

    if imc is None:
        QMessageBox.warning(ventana, "Error", estado)
    else:
        QMessageBox.information(ventana, "Resultado", f"Tu IMC es {imc:.2f}\nEstado: {estado}")
    

app = QApplication(sys.argv)
ventana = QWidget()

#Propiedades de la ventana 
ventana.setWindowTitle("Calcular IMC")
ventana.setGeometry(100,100,300,200)
layout = QVBoxLayout()
peso = QLabel("Ingresa tu peso ")
opcionPeso = QComboBox()
opcionPeso.addItems(["kg","lb"])
estatura = QLabel("Ingresa tu estatura")
opcionEstatura = QComboBox()
opcionEstatura.addItems(["m","cm"])

Peso = QLineEdit()
Estat = QLineEdit()
boton = QPushButton("Calcular")
boton.clicked.connect(mensaje)

widgets = [peso, Peso, opcionPeso, estatura, opcionEstatura, Estat , boton]
ventana.setLayout(layout)
for w in widgets:
    layout.addWidget(w)
ventana.show()
sys.exit(app.exec_())