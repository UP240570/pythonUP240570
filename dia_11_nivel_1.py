#DIA 11 NIVEL 1

#1 Función add_two_numbers
def add_two_numbers(a, b):
    return a + b


#2 Area de circuclo
import math

def area_of_circle(radio):
    return math.pi * radio * radio


#3 Todos los numeros
def add_all_nums(*args):
    suma = 0
    for num in args:
        if isinstance(num, (int, float)):
            suma += num
        else:
            return "Todos los elementos deben ser números."
    return suma


#4 De G° a F°
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


#5 Devuelve estacion del año
def check_season(month):
    month = month.lower()
    if month in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif month in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif month in ['junio', 'julio', 'agosto']:
        return 'Verano'
    elif month in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    else:
        return 'Mes no válido'


#6 Pendiente de ecuacion
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Infinito (pendiente indefinida)"
    return (y2 - y1) / (x2 - x1)


#7 Ecuacion cuadratica
import math

def solve_quadratic_eqn(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay soluciones reales"
    elif discriminante == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2


#8 Lista
def print_list(lista):
    for item in lista:
        print(item)


#9 Inverso lista
def reverse_list(lista):
    reversed_list = []
    for i in range(len(lista)-1, -1, -1):
        reversed_list.append(lista[i])
    return reversed_list
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]


#12 Poner en mayuscula lista
def capitalize_list_items(lista):
    return [item.capitalize() for item in lista]


#11 Agregar elemeto
def add_item(lista, item):
    lista.append(item)
    return lista

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))    
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))   

#12 Eliminar
def remove_item(lista, item):
    if item in lista:
        lista.remove(item)
    return lista

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  


#13 Suma de numeros
def sum_of_numbers(numero):
    suma = 0
    for i in range(numero + 1):
        suma += i
    return suma

print(sum_of_numbers(5)) 
print(sum_of_numbers(10)) 
print(sum_of_numbers(100))

#14 Suma probabilidades
def sum_of_odds(numero):
    suma = 0
    for i in range(numero + 1):
        if i % 2 != 0:
            suma += i
    return suma


#15 Suma de numeros par
def sum_of_even(numero):
    suma = 0
    for i in range(numero + 1):
        if i % 2 == 0:
            suma += i
    return suma
