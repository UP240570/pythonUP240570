#DIA 11 NIVEL 3

#1 Numero primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

print(es_primo(7))  
print(es_primo(10))  


#2 Verificar si los elementos no se repiten
def todos_unicos(lista):
    return len(lista) == len(set(lista))

print(todos_unicos([1, 2, 3]))     
print(todos_unicos([1, 2, 2, 3])) 


#3 Si son del mismo dato
def mismo_tipo(lista):
    if len(lista) == 0:
        return True
    tipo = type(lista[0])
    for elemento in lista:
        if type(elemento) != tipo:
            return False

print(mismo_tipo([1, 2, 3]))        
print(mismo_tipo([1, "dos", 3]))   


#4 Nombre valido en python 
def es_variable_valida(nombre):
    return nombre.isidentifier()

print(es_variable_valida("mi_variable")) 
print(es_variable_valida("123variable")) 


#5 Idiomas mas hablados
from countries_data import countries_data

def idiomas_mas_hablados(cantidad):
    conteo = {}
    for pais in countries_data:
        for idioma in pais["languages"]:
            if idioma in conteo:
                conteo[idioma] += 1
            else:
                conteo[idioma] = 1

    
    lista_ordenada = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
    return lista_ordenada[:cantidad]

print(idiomas_mas_hablados(10))


#Paises mas poblados
from countries_data import countries_data

def paises_mas_poblados(cantidad):
    lista_ordenada = sorted(countries_data, key=lambda pais: pais['population'], reverse=True)
    resultado = []
    for pais in lista_ordenada[:cantidad]:
        resultado.append({
            'pais': pais['name'],
            'poblacion': pais['population']
        })
    return resultado


print(paises_mas_poblados(10))


