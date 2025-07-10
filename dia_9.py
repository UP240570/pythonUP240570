#DIA 9

#1 PARA CONDUCIR
'''edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Tiene la edad suficiente para conducir")

else: 
    print("Necesita", 18-edad ,"años mas para poder conducir")


#2 DIFERENCIA DE EDAD
mi_edad = 19
tu_edad = int(input("Ingresa tu edad: "))


if  tu_edad > mi_edad:
    dif=  tu_edad - mi_edad
    if dif == 1:
        print("Eres un 1 mayor que yo")
    else:
        print("Eres", dif ,"años mayor que yo")
elif tu_edad < mi_edad:
    dif= mi_edad - tu_edad
    if dif == 1:
        print("Soy un 1 mayor que tu")
    else:
        print("Tengo", dif ,"años mas que tu")
else:
    print("Tenemos la misma edad")

#3 NUMERO MAYOR
A = int(input("Ingresa un numero:" ))
B = int(input("Ingresa otro numero:" ))

if A > B:
    print(A ,"Es mayor que", B)
elif A < B:
    print(B ,"Es mayor que", A)
else:
    print("Son iguales")

#
#
#NIVEL 2
#
#

#1 CALIFICACIONES
calif = int(input("Ingresa la calificacion (0 - 100): "))

if calif > 79:
    print("A")
elif calif > 69: 
    print("B")
elif calif > 59: 
    print("C")
elif calif > 49: 
    print("D")
elif calif >= 0: 
    print("F")

else:
    print("ERROR, DEBE SER MENOR O IGUAL A 100")

#2 ETAPA DEL AÑO
mes = input("Ingresa un mes: ")

if mes in ["septiembre", "octubre", "noviembre"]:
    print("Es otoño.")
elif mes in ["diciembre", "enero", "febrero"]:
    print("Es invierno.")
elif mes in ["marzo", "abril", "mayo"]:
    print("Es primavera.")
elif mes in ["junio", "julio", "agosto"]:
    print("Es verano.")
else:
    print("Mes no válido.")

#3 AGREGAR FRUTA
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits = ['banana', 'orange', 'mango', 'lemon']

nueva_fruta = input("Ingresa el nombre de una fruta: ")

if nueva_fruta in fruits:
    print("Esa fruta ya existe en la lista.")
else:
    fruits.append(nueva_fruta)
    print("Fruta añadida. La lista actualizada es:")
    print(fruits)'''

#
#
#NIVEL 3
#
#

#1 MODIFICAR DICCIONARIO
person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
    'street': 'Space street',
    'zipcode': '02210'
}
}

if 'skills' in person:
    habilidades = person['skills']  
    cantidad = len(habilidades) 
    mitad = cantidad // 2  
    print("La habilidad del centro es:", habilidades[mitad])

if 'skills' in person:
    if 'Python' in person['skills']:
        print("Sí tiene la habilidad de Python.")
    else:
        print("No tiene la habilidad de Python.")

if 'skills' in person:
    habilidades = person['skills']

    if habilidades == ['JavaScript', 'React']:
        print("Es desarrollador front-end.")
    elif 'Node' in habilidades and 'Python' in habilidades and 'MongoDB' in habilidades:
        print("Es desarrollador back-end.")
    elif 'React' in habilidades and 'Node' in habilidades and 'MongoDB' in habilidades:
        print("Es desarrollador fullstack.")
    else:
        print("No se conoce el título del desarrollador.")

if person['is_marred'] == True and person['country'] == 'Finland':
    nombre_completo = person['first_name'] + " " + person['last_name']
    print(nombre_completo, "reside en Finland. Está casado.")
