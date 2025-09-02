from Package.modul import *

viajes = []
viaje = []
#Manejo de excepciones try- except
while True:
    try:
       print("************** Datos de su viaje ****************")
       origen = input("Ingrese su lugar de origen ")
       destino = input("Ingrese su lugar de destino ")
       tiempo = float(input("Ingrese las horas que dura el viaje "))
       costo = float(input("Ingrese lo que cuenta el viaje ")) 
       viaje.append(origen)
       viaje.append(destino) 
       viaje.append(tiempo) 
       viaje.append(costo) 
       viajes.append(viaje)           
    except:
        print("Debe ingresar solo datos válidos")        
    finally:
        op = input("¿Desea ingresar datos de otro viaje? (s/n)")
        if (op == "n"):
            break




for v in viajes:
    viaje2 = Viaje(v[0], v[1], v[2], v[3])     
    viaje2.mostrar_viajes()
    viaje2.resumen_semanal() 
