#DIA 7
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1 LONGITUD
print(len(it_companies))

#2 AGREGAR TWITER
it_companies.add ('Twiter')
print(it_companies)

#3 AGREGAR VARIOS 
it_companies.update(['TikTok',  'YouTube', 'Instagram'])
print(it_companies)

#4 ELIMINAR EMPRESA
it_companies.remove('Apple')
print(it_companies)


#
#
#NIVEL 2
#
#


#1 UNIR A Y B
print(A.union(B))

#2 INTERSECCION
print(A.intersection(B))

#3 A ES CONJUNTO DE B
print(A.issubset(B))

#4 A Y B SON CONJUNTOS DISJUNTOS
A.isdisjoint(B)

#5 UNIR A CON B Y B CON A
union_AB = A.union(B)
union_BA = B.union(A)

print("A unido con B:", union_AB)
print("B unido con A:", union_BA)

#6 DIFERENCIA
print(A ^ B)

#7 ELIMINAR CONNJUNTOS
del it_companies
del A
del B


#
#
#NIVEL 3
#
#


#1

print("Longitud de la lista:", len(age))
print("Longitud del conjunto:", len(set(age)))

#3
oracion = "Soy profesor y me encanta inspirar y enseñar."
palabras = oracion.lower().replace(".", "").split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
print("Número de palabras únicas:", len(palabras_unicas))
