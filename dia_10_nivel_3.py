#DIA 10 NIVEL 3

#1 Todos los paises que acaban en land
from countries import countries

for country in countries:
    if 'land' in country:
        print(country)

#2 Invertir lista 
frutas = ['banana', 'orange', 'mango', 'lemon']
frutas_reversa = []

for i in range(len(frutas) - 1, -1, -1):
    frutas_reversa.append(frutas[i])

print(frutas_reversa)


#3 Contar los idiomas
from countries_data import countries_data

idiomas = set()

for pais in countries_data:
    for idioma in pais['languages']:
        idiomas.add(idioma)

print("Número total de idiomas únicos:", len(idiomas))


#4 Idiomas mas hablados
from collections import Counter

idioma_contador = Counter()

for pais in countries_data:
    for idioma in pais['languages']:
        idioma_contador[idioma] += 1

top_10_idiomas = idioma_contador.most_common(10)

for idioma, cantidad in top_10_idiomas:
    print(f"{idioma}: {cantidad} países")


#5 Paises mas poblados
paises_ordenados = sorted(countries_data, key=lambda x: x['population'], reverse=True)

for pais in paises_ordenados[:10]:
    print(f"{pais['name']}: {pais['population']}")
