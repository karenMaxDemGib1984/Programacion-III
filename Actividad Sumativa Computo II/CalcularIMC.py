#import PyQt5
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QPushButton,QLineEdit, QMessageBox)

import sys 


app = QApplication(sys.argv)
ventana = QWidget()

#Propiedades de la ventana 
ventana.setWindowTitle("Calcular IMC")
ventana.setGeometry(100,100,300,200)
layout = QVBoxLayout()
peso = QLabel("Ingresa tu peso (kg)  ")
estatura = QLabel("Ingresa tu estatura(m)")
Peso = QLineEdit()
Estat = QLineEdit()
boton = QPushButton("Calcular")
#boton.clicked.connect(mensaje)

widgets = [peso, Peso, estatura, Estat , boton]
for w in widgets:
    layout.addWidget(w)
ventana.show()
sys.exit(app.exec_())
 