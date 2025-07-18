#DIA 7 NIVEL 2
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

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
