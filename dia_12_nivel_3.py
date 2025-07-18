#DIA 12 NIVEL 3
#1 Lista aleatoria
import random

def shuffle_list(lista):
    lista_copia = lista[:]
    random.shuffle(lista_copia)
    return lista_copia

lista = [1, 2, 3, 4, 5]
print(shuffle_list(lista))


#2 Numeros aleatorios
def unique_random_numbers():
    return random.sample(range(10), 7)

print(unique_random_numbers())

