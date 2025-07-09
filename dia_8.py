#DIA 7

#1 CREAR UN DICCIONARIO VACION
dog = {}

#2 AGG INFO
dog["nombre"] = "Docky"
dog["color"] = "Cafe"
dog["raza"] = "Pug"
dog["patas"] = 4
dog["edad"] = 3

print(dog)

#3 CREAR DIC ESTUDIANTE
student = {}

student["nombre"] = "Andres"
student["apellido"] = "Lopez"
student["sexo"] = "Masculino"
student["edad"] = 19
student["estado civil"] = "Soltero"
student["habilidades"] = "Trabajador"
student["pais"] = "Mexico"
student["ciudad"] = "Ags"
student["direccion"] = "Vistabella"

#4 LONGITUD DE STUDENT
print(len(student))

#5 VALOR DE HABILIDAES Y TIPO DE DATO
print((student['habilidades']))
print(type(student['habilidades']))

#6 AÑADIR HABILIDADES
student["habilidades"] = student["habilidades"].split(", ")
student["habilidades"].append("Sociable")
print(student)

#7 CLAVES EN FORMA DE LISTA 
print(student.keys())

#8 EN FORMA DE LISTA
print(student.values())

#9 TUPLAS
print(student.items())

#10 ELIMINAR UN ELEMENTO
del student['apellido']  
print(student)

#11 ELIMINAR UNO DE LOS DIRECCIONARIOS
del student