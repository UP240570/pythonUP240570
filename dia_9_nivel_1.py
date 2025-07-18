#DIA 9

#1 PARA CONDUCIR
edad = int(input("Ingresa tu edad: "))

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
