class Viaje:
    #Declaración de la lista viajes
    viajes = []
    
    #Constructor de la clase
    def __init__(self,origen,destino,tiempo,costo):
        self.origen = origen
        self.destino = destino
        self.tiempo = tiempo
        self.costo = costo
        self.viajes.append(self)
    
    #Función para mostrar llos viajes
    def mostrar_viajes(self):
        for i,viaje in enumerate(Viaje.viajes,1):
            print(f"{i} - Origen: {viaje.origen} "+
                f"Destino: {viaje.destino} Tiempo: {viaje.tiempo} horas Costo: ${viaje.costo}")
    
    #Método para mostrar un resumen de los viajes         
    def resumen_semanal(self):
        total_tiempo = sum(viaje.tiempo for viaje in self.viajes)
        total_costo = sum(viaje.costo for viaje in self.viajes)
        print(f"Resumen Semanal: Tiempo total invertido: {total_tiempo} horas, Gasto total: ${total_costo}")


viaje1 = Viaje('San Miguel', 'San Salvador', 4, 5)     
viaje1.mostrar_viajes()
viaje1.resumen_semanal()







