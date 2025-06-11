#NIVEL 2


nombre = 'Andres'
apellido = 'Lopez'
nombre_completo = ('Mauricio', 'Andres', 'Rodriguez', 'Lopez')
pais = 'Mexico'
ciudad = 'Italia'
ano = 2025
edad = 19
casado = True
luz_encendida = False

print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(ano))
print(type(casado))
print(type(luz_encendida))

completo = input("Ingresa tu nombre completo: ")
print(len(completo))

nombre_1 = input("Ingresa tu nombre: ")
apellido_1 = input("Ingresa tu apellido: ")
print("La cantidad de letras en tu nombres es de: ", len(nombre_1), " y de tu apellido son: ", len(apellido_1))

num_1 = 5
num_2 = 4 

print("La suma es: ", num_1 + num_2)
print("La resta es: ", num_1 - num_2)
print("La multiplicacion es: ", num_1 * num_2)
print("La division es: ", num_1 / num_2)

residuo = num_1 % num_2
print("El residuo es: ", residuo)

exp = num_1 ** num_2
print("El resultado es: ", exp)

floor_division = num_1 // num_2
print("La division de piso es: ", floor_division)

area_circulo = 3.1416*(30**2)
print("La area del circulo es: ", area_circulo)

circunferencia_circulo = 2*3.1416*30
print(circunferencia_circulo)


radio = float(input("Ingresa el radio del circulo: "))
print ("La area del circulo es de: ", 3.1416*(radio)**2)

nom = input("Ingresa tu nombre: ")
ape = input("Ingresa tu apellido: ")
anos = input("Ingresa tu edad")
pai = input("Ingresa tu pais: ")
