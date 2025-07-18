#DIA 13
#1 Numeros negativos
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_cero = [n for n in numbers if n <= 0]
print(negativos_y_cero)


#2 Juntar listas 
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_aplanada = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print(lista_aplanada)


#3 Tupla
tuplas = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
for t in tuplas:
    print(t)


#4 Nueva lista 
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

nueva_lista = [
    [country.upper(), country[:3].upper(), city.upper()]
    for [(country, city)] in countries
]

print(nueva_lista)


#5 De lista a diccionario
lista_diccionarios = [
    {'country': country.upper(), 'city': city.upper()}
    for [(country, city)] in countries
]

print(lista_diccionarios)


#6 
names = [('Asabeneh', 'Yetayeh'), ('David', 'Smith'), ('Donald', 'Trump'), ('Bill', 'Gates')]
nombres_completos = [f"{nombre} {apellido}" for nombre, apellido in names]
print(nombres_completos)


#7 Funcion lambda
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else "Indefinida"
print(slope(1, 2, 3, 6)) 
