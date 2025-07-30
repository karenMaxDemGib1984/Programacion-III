def operaciones(n1, n2):    
    return n1+n2



def operacion(n):
    suma = lambda  x: x+n
    resta = lambda  x: x- n
    multiplicacion = lambda  x: x * n
    division = lambda  x: x / n
    return suma, resta, multiplicacion, division


def opbasicas(n1, n2):
    diccionario = {
        "suma" : n1 + n2,
        "resta": n1 - n2, 
        "mul" : n1 * n2,
        "div" : n1 / n2, 
        "cua"  : n1 ** n2,
        "resto" : n1 % n2 
    }
    return diccionario





