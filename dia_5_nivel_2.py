#DIA 5 NIVEL 2

#DECLARAR LISTA
edad = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]



#EDAD MINIMA Y MAXIMA
edad.sort
edad_min = min(edad)
edad_max = max(edad)
print(edad_min)
print(edad_max)



#AGREGAR OTRA VES LA EDAD MINIMA Y MAXIMA
edad.append(edad_max)
edad.append(edad_min)
print("Lista con min y max agregados:", edad)



#EDAD DEL MEDIO
edad.sort()
cantidad = len(edad)

if cantidad % 2 == 0:
    mediana = (edad[cantidad // 2 - 1] + edad[cantidad // 2]) / 2
else:
    mediana = edad[cantidad // 2]

print("Edad mediana:", mediana)



#PROMEDIO DE EDADES
promedio = sum(edad) / len(edad)
print("Promedio de edades:", round(promedio, 2))



#RANGO
rango = edad_max - edad_min
print("Rango de edades:", rango)



#COMPARAR
print("Diferencia mínima:", abs(edad_min - promedio))
print("Diferencia máxima:", abs(edad_max - promedio))



#LISTA DE PAISES
paises = ['China', 'Russia', 'USA', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']



#PAIS DEL MEDIO
cantidad = len(paises)

if cantidad % 2 == 0:
    medio = paises[cantidad // 2 - 1 : cantidad // 2 + 1]
else:
    medio = [paises[cantidad // 2]]

print("País(es) del medio:", medio)



#DIVIR LA LISTA EN 2
if cantidad % 2 == 0:
    primera_mitad = paises[:cantidad // 2]
    segunda_mitad = paises[cantidad // 2:]
else:
    primera_mitad = paises[:cantidad // 2 + 1]
    segunda_mitad = paises[cantidad // 2 + 1:]

print("Primera mitad:", primera_mitad)
print("Segunda mitad:", segunda_mitad)



#DESEMPAQUETAR LOS PRIMERO 3 PAISES
pais1, pais2, pais3, *paises_escandinavos = paises

print("Primeros países:", pais1, pais2, pais3)
print("Países escandinavos:", paises_escandinavos)
