#DIA NIVEL 3

age = [22, 19, 24, 25, 26, 24, 25, 24]
#
#1

print("Longitud de la lista:", len(age))
print("Longitud del conjunto:", len(set(age)))

#3
oracion = "Soy profesor y me encanta inspirar y enseñar."
palabras = oracion.lower().replace(".", "").split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
print("Número de palabras únicas:", len(palabras_unicas))
