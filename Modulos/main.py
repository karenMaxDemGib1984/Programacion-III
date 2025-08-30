import Package.modul as Modulo


v1 = float(input("Ingresa un valor "))
v2 = float(input("ingresa otro valor "))
items = Modulo.opbasicas(v1, v2)

print("La suma es igual a " + str(items["suma"]))
print("La resta es igual a " +str(items["resta"]))
print("La multiplicación  es igual a " +str(items["mul"]))
print("La división es igual a " +str(items["div"]))
print("La elevación del primer numero al segundo es de " +str(items["cua"]))
print("El modulo de dividir es igual a " +str(items["div"]))


print("Karen")