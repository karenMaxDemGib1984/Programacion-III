#import PyQt5
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QPushButton,QLineEdit, QMessageBox, QComboBox)

import sys 

def calcularIMC(peso, estatura):
    pass
    
    
    
  

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
#boton.clicked.connect(mensaje)

widgets = [peso, Peso, opcionPeso, estatura, opcionEstatura, Estat , boton]
ventana.setLayout(layout)
for w in widgets:
    layout.addWidget(w)
ventana.show()
sys.exit(app.exec_())