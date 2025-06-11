import math

edad = 19
altura = 23.254
complejo = 4-4j



#AREA DE UN TRIANGULO 
b = float(input("Ingresa la base del triangulo: "))
h = float(input("Ingresa la altura del triangulo: "))
print("La area del triangulo es de: ", 0.5*b*h) 



#PERIMETO DE UN TRIANGULO
l1 = int(input("Ingresa la medida del lado 1: "))
l2 = int(input("Ingresa la medida del lado 2: "))
l3 = int(input("Ingresa la medida del lado 3: "))
print("El perimetro del triangulo es: ", (l1+l2+l3))



#AREA DE UN RECTANGULO
largo = float(input("Ingresa el largo del rectangulo: "))
ancho = float(input("Ingresa el ancho del rectangulo: "))
print("El area del rectangulo es de: ", largo*ancho)



#PERIMETRO DE UN RECTANGULO
largo1 = int(input("Ingresa el largo del rectangulo: "))
ancho1 = int(input("Ingresa el ancho del rectangulo: "))
print("El area del rectangulo es de: ",2*(largo1+ancho1))



#AREA DE UN CIRCULO
radio = float(input("Ingresa el radio del circulo: "))
print("El area del circulo es: ", 3.14*(radio*radio))



#CIRCUNFERENCIA DE UN CIRCULO
print("La circunferencia del circulo es: ", 2*3.14*radio)



#INTERSECCION CON EJE X Y Y
m = 2    
b = -2  

print("La pendiente es:", m)

x_y = 0
y_interseccion = m * x_y + b
print("La intersección con el eje y es: (", x_y, ",", y_interseccion, ")")

y_x = 0
x_interseccion = (y_x - b) / m
print("La intersección con el eje x es: (", x_interseccion, ",", y_x, ")")



#PENDIENTE Y DISTANCIA EUCLADIANA
x1 = 2
y1 = 2
x2 = 6
y2 = 10

pen = (y2 - y1) / (x2 - x1)

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) # Calcular la distancia euclidiana

print("La pendiente (m) es:", pen)
print("La distancia euclidiana es:", d)



#VALOR DE Y
x1 = -5
y1 = x1**2 + 6*x1 + 9
print("Si x =", x1, "entonces y =", y1)

x2 = -4
y2 = x2**2 + 6*x2 + 9
print("Si x =", x2, "entonces y =", y2)

x3 = -3
y3 = x3**2 + 6*x3 + 9
print("Si x =", x3, "entonces y =", y3)

x4 = -2
y4 = x4**2 + 6*x4 + 9
print("Si x =", x4, "entonces y =", y4)

# Verificar cuándo y es igual a 0
if y1 == 0:
    print("y es 0 cuando x =", x1)
if y2 == 0:
    print("y es 0 cuando x =", x2)
if y3 == 0:
    print("y es 0 cuando x =", x3)
if y4 == 0:
    print("y es 0 cuando x =", x4)




#LONGITUD PYTHON Y DRAGON

palabra1 = len("python")
palabra2 = len("dragon")


print("Longitud de 'python':", len('python'))
print("Longitud de 'dragon':", len('dragon'))

comparacion = palabra1 > palabra2

print("¿Es la longitud de 'python' es mayor que la de 'dragon'? ", comparacion)



#COMPROBAR SI "ON" ESTA EN LAS PALABRAS
palabra = "python"
palabra = "dragon"

resultado = ("on" in palabra) and ("on" in palabra)

print("¿La cadena 'on' está en ambas palabras 'python' y 'dragon'? ", resultado)



#COMPROBAR QUE JERGA NO SE ENCUENTRE EN LA ORACION
oracion = input("Ingresa una oracion: ")

com = ("jerga" in oracion)

print("¿La palabra jerga se encuentra en la oracion? ", com)


#CAMBIAR TIPO DE VARIABLE A PYTHON
texto = "Python"

longitud = len(texto)
print("Longitud (entero):", longitud)

flo = float(longitud)
print("Longitud como número flotante:", flo)

cad = str(flo)
print("Longitud como cadena:", cad)



#NUMERO PAR O IMPAR
num = int (input("Ingresa un numero: "))

if (num %2 == 0):
    print("El numero es par")

else:
    print("El numero es impar")



#COMPROBAR SI EL RESIDUO DE 7 ENTRE 3 EST IGUAL A 2.7
div = 7 % 3
r = 2.7

compar = div == r

print("El resiudo si es igual a 2.7? ", compar)



#COMPROBAR SI '10' ES IGUAL A 10
j = '10' 
l = 10  

ad = type(j) == type(l)

print("¿El tipo de '10' es igual al tipo de 10?", ad)



#COMPROBAR SI '9.8' ES IGUAL A 10
f = int(9.8) 
c = 10 

run = type(f) == type(c)

print("¿El tipo de 9.8 es igual al tipo de 10?", run)



#SALARIO
hrs = float(input("Ingresa las horas: "))
tar = float(input("Ingresa la tarifa por hora: "))

print("Tu salario es de: ", hrs * tar)



#CUANTOS SEGUNDOS VIVE UNA PERSONA
years = int(input("Ingresa los años que ha vivido: "))

print("Los segundos que ha vivido son: ", years * 31536000 )



#IMPRIMIR TABLA
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)
