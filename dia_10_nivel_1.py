#DIA 10 NIVEL 1

#1 Iterar del 0 al 10 con for y while
# Usando for
for i in range(11):
    print(i)

# Usando while
i = 0
while i <= 10:
    print(i)
    i += 1


#2 Iterar del 10 al 0 con for y while
# Usando for
for i in range(10, -1, -1):
    print(i)

# Usando while
i = 10
while i >= 0:
    print(i)
    i -= 1


#3 Triangulo usando #
for i in range(1, 8):
    print('#' * i)


#4 Bucles anidados cuadrado
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()  # Salto de línea


#5 Multiplicacion
for i in range(11):
    print(f"{i} x {i} = {i * i}")


#6 Recorrer lista
tecnologias = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in tecnologias:
    print(item)


#7 Numeros del 0 al 100 solo pares
for i in range(101):
    if i % 2 == 0:
        print(i)


#8 Numeros del 0 al 100 solo impares
for i in range(101):
    if i % 2 != 0:
        print(i)
