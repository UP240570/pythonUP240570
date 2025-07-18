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
    print(fruits)
