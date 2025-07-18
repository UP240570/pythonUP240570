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
