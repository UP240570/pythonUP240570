#DIA 6 NIVEL 2


#2 CRAER TUPLAS PRODUCTOS ANIMAL, VENGETALES Y FRITAS Y UNIRLAS
vegetales = ('Jitomate', 'Chile', 'Cebolla')
frutas = ('Sandia', 'Platano', 'Manzana')
produc_animal = ('leche', 'huevo', 'crema')
comida_tp = vegetales + frutas + produc_animal
print(comida_tp)

#3 CAMBIAR TUPLA COMIDA A LISTA
comida_lt = list(comida_tp)

#4 SEPARAR EL ELEMENTO DE MEDIO
medio = comida_tp[len(comida_tp)//2]
print(medio)

#5 SEPARAR LOS PRIMEROS 3 Y LOS ULTIMOS 3
primer = comida_lt[:3]
ultima = comida_lt[-3:]
print(primer)
print(ultima)

#6 ELIMINAR TUPLA
del comida_tp

#7.1 COMPROBAR SI HAY ISLANDIA EN LA TUPLA
paises = ('Dinamarca', 'Finlandia', 'Islandia', 'Noruega', 'Suecia')
print('Estonia' in paises)

#7.2 COMPROBAR SI HAY ESTONIA EN LA TUPLA
print('Islandia' in paises)