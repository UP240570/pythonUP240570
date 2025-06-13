# CONCATENAR TRAINA DIAS DE PYTHON
cadena1 = "Treinta"
cadena2 = "Días"
cadena3 = "De"
cadena4 = "Python"

print(cadena1 + " " + cadena2 + " " + cadena3 + " " + cadena4)



# CONCATENAR CODIFICACION PARA TODOS
c1 = "Codificacion"
c2 = "Para"
c3 = "Todos"

print(c1 + " " + c2 + " " + c3 )



#DECLARAR LA VARIABLE EMPRESA
empresa = 'Codificacion Para Todos'



#IMPRIMIR VARIABLE EMPRESA
print(empresa)



#IMPRIMIR LONGITUD DE EMPRESA
print(len(empresa))



#IMPRIMIR EN MAYUSCULAS
print(empresa.upper())



#IMPRIMIR EN MINUSCULA
print(empresa.lower())



#FOMATEAR
print(empresa.capitalize()) 
print(empresa.title())  
print(empresa.swapcase())  



#CORTAR PRIMER PALABRA CADENA
print(empresa[13:23])



#COMPROBAR SI CODIFICACION ESTA EN LA CADENA
print("Codificacion" in empresa)



#REEMPLAZAR CODIFICACION POR PYTHON
print(empresa.replace('Codificacion', 'Python'))



#SEPARAR CADENA
print(empresa.split())



#SEPARAR POR COMAS
cad = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(cad.split(", "))



#QUE LETRA ESTA EN EL LUGAR 0
print(empresa[0])



#QUE LETRA ESTA EN EL FINAL
print(empresa[22])



#QUE LETRA ESTA EN EL LUGAR 10
print(empresa[10])



#ACRONIMOS PARA "PYTHON PARA TODOS"
print("Acrónimos para 'Python para todos':")

print("PPT  = Python Para Todos")
print("PyTo = PYthon para TOdos")



#ACRONIMO PARA "CODIFICACION PARA TODOS"
print("Acrónimos para 'Codificacion Para Todos':")

print("CPT  = Codificacion Para Todos")
print("CodPT = Codificacion Para Todos")



#POSICION DE LETRA C
oracion = "Codificacion Para Todos"

print("La posicion en la que esta le letra C es: ", oracion.index("C"))



#POSICION DE LETRA P
print("La posicion en la que esta le letra C es: ", oracion.index("P"))



#ULTIMA APARICION DE LA LETRA L
ora = "Coding For All People"
print("La última aparición de 'l' en la oracion", ora.rfind("l"))



#POSICION DE BECAUSE
ora1 = "You cannot end a sentence with because because because is a conjunction"
print("El lugar donde aparece 'because' en la oracion es: ", ora1.index("because"))



#ULTIMA OCURRENCIA DE BECAUSE
print("El lugar donde aparece 'because' en la oracion es: ", ora1.rfind("because"))



#ELIMINAR BECAUSE BECAUSE BECAUSE
print("La nueva oracion sin la frases because es: ", ora1.replace("because because because", ""))



#PRIMERA POSICION DE BECAUSE
print("La primera aparición de 'because' está en el índice:", ora1.find("because") )



#EMPIEZA CON CODING
texto = 'Coding For All'
print(texto.startswith("Coding"))



#TERMINA CON CODING
print(texto.endswith("coding"))



#ELIMINAR LOS ESPACIOS
texto1 = '   Coding For All   '
print(texto1.strip())


#CUAL DEVUELVE VERDADERO CON INSIDENTIFER
print("30DaysOfPython".isidentifier())        
print("thirty_days_of_python".isidentifier())



#UNIR LISTA
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(libraries))



#TABULACION PARA IMPRIMIR EN OTRA LINEA
print("I am enjoying this challenge.\nI just wonder what is next.")



#IMPRIMIR CON TABULADOR
print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")



#AREA DE UN CIRCULO EN FORMATO DE CADENA
radio = 10
areas = 3.14 * radio ** 2

print("El área de un círculo con radio ",radio," es ", areas," metros cuadrados.")



#USANDO FORMATO
a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b)) 
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))

