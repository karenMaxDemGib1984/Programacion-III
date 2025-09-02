#soy erick
from Package.modul import *

#Agregar mas datos 
#def resumen_semanal(self):
#total_tiempo = sum(viaje.tiempo for viaje in self.viajes)
#total_costo = sum(viaje.costo for viaje in self.viajes)
#print(f"Resumen Semanal: Tiempo total invertido: {total_tiempo} horas, Gasto total: ${total_costo}") #

viaje2 = Viaje('Santa Ana', 'Sonsonate', 4, 5)     
viaje2.resumen_semanal()
viaje3 = Viaje('Soyapango', 'San Salvador', 5, 3)     
viaje3.resumen_semanal()
viaje4 = Viaje('La Union', 'Sonsonate', 2, 1)     
viaje4.resumen_semanal()
viaje5 = Viaje('Santa Ana', 'Sonsonate', 6, 7)     
viaje5.resumen_semanal()


