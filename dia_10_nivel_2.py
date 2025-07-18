#DIA 10 NIVEL 2

#1 Suma de numeros del 0 al 100
suma = 0
for i in range(101):
    suma += i
print("La suma de todos los números es:", suma)


#2 Suma de numeros pares e impares
suma_pares = 0
suma_impares = 0

for i in range(101):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i

print("Suma de pares:", suma_pares)
print("Suma de impares:", suma_impares)
