#En El Salvador, muchas personas dependen del transporte público para ir
#a su trabajo, estudio o actividades diarias. Cada día realizan distintos viajes
#en rutas urbanas o rurales, con tiempos y costos variables. Sin un registro,
#es difícil saber cuánto se gasta en transporte semanalmente ni cuáles rutas
#consumen más tiempo o dinero.

#Se busca un sistema que permita registrar los viajes realizados, y generar
#una salida en pantalla al final que muestre los datos ordenados de cada
#viaje realizado. Además, el sistema debe mostrar un resumen con el gasto
#total semanal y el tiempo total invertido.

# Preguntas
#¿Qué ventajas tiene en comparación con poner todo el código en un solo archivo o utilizar módulos?

#¿Cómo aplicaron la Programación Orientada a Objetos en su solución? Describan el papel de las clases creadas.

#¿De qué manera el uso de GitHub facilitó el trabajo colaborativo en equipo? Den un ejemplo concreto

class Viaje:
    viajes = []
    
    def __init__(self,origen,destino,tiempo,costo):
        self.origen = origen
        self.destino = destino
        self.tiempo = tiempo
        self.costo = costo
        self.viajes.append(self)
        
    def mostrar_viajes(self):
        for i,viaje in enumerate(Viaje.viajes,1):
            print(f"{i} - Origen: {viaje.origen} "+
                f"Destino: {viaje.destino} Tiempo: {viaje.tiempo} mins Costo: ${viaje.costo}")
                
    def resumen_semanal(self):
        total_tiempo = sum(viaje.tiempo for viaje in self.viajes)
        total_costo = sum(viaje.costo for viaje in self.viajes)
        print(f"Resumen Semanal: Tiempo total invertido: {total_tiempo} mins, Gasto total: ${total_costo}")