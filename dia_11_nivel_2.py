#DIA 11 NIVEL 2

#1 Cuantos numero pares e impares en n numeros
def pares_e_impares(numero):
    pares = 0
    impares = 0
    for i in range(numero + 1):  
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    print("Cantidad de números impares:", impares)
    print("Cantidad de números pares:", pares)

pares_e_impares(100)


#2 Factorial numeros
def factorial(numero):
    if numero < 0:
        return "El número debe ser positivo"
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

print("El factorial de 5 es:", factorial(5))


#3 Verificar si esta vacio
def esta_vacio(valor):
    if valor == "" or valor == [] or valor == {} or valor is None:
        return True
    else:
        return False

print(esta_vacio(""))         
print(esta_vacio([1, 2, 3]))
print(esta_vacio(None))       


#4 Estadistica 
#Media
def calcular_media(lista):
    suma = sum(lista)
    cantidad = len(lista)
    return suma / cantidad

#Mediana 
def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    cantidad = len(lista_ordenada)
    medio = cantidad // 2
    if cantidad % 2 == 0:
        return (lista_ordenada[medio - 1] + lista_ordenada[medio]) / 2
    else:
        return lista_ordenada[medio]


#Moda
def calcular_moda(lista):
    conteo = {}
    for numero in lista:
        if numero in conteo:
            conteo[numero] += 1
        else:
            conteo[numero] = 1

    max_repeticiones = max(conteo.values())
    modas = []
    for clave in conteo:
        if conteo[clave] == max_repeticiones:
            modas.append(clave)

    if len(modas) == 1:
        return modas[0]
    else:
        return modas  # puede haber más de una moda


#Rango
def calcular_rango(lista):
    return max(lista) - min(lista)


#Varianza
def calcular_varianza(lista):
    media = calcular_media(lista)
    suma = 0
    for numero in lista:
        suma += (numero - media) ** 2
    return suma / len(lista)


#Desviacion estandar 
def calcular_desviacion(lista):
    import math
    varianza = calcular_varianza(lista)
    return math.sqrt(varianza)

numeros = [2, 4, 4, 4, 5, 5, 7, 9]
