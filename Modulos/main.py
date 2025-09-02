from Package.modul import *


#Manejo de excepciones try- except
while True:
    try:
       print("************** Datos de su viaje ****************")
       origen = input("Ingrese su lugar de origen ")
       destino = input("Ingrese su lugar de destino ")
       tiempo = float(input("Ingrese las horas que dura el viaje "))
       costo = float(input("Ingrese lo que cuenta el viaje "))       
    except:
        print("Debe ingresar solo datos válidos")        
    finally:
        op = input("¿Desea ingresar datos de otro viaje? (s/n)")
        if (op == "n"):
            break



viaje1 = Viaje('San Miguel', 'San Salvador', 4, 5)     
viaje1.mostrar_viajes()
viaje1.resumen_semanal()

