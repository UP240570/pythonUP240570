#DIA 6 NIVEL 1

#1 CREAR TUPLA VACIA
t = ()


#2 CREAR TUPLA 
brothers = ('Andres', 'Gabriel', 'Axel', 'Julio')
sisters = ('Fanny', 'Andrea', 'Alexa', 'Ivonne')


#3 UNIR TUPLAS
siblings =  brothers + sisters
print(siblings)


#4 CUANTOS HERMANOS SON
print("¿Cuantos hermanos son?", len(siblings))


#5 AGREGAR NOMBRE DE PADRE Y MADRE
father = 'Mauricio'
mother = 'Gloria'
family = siblings + (father, mother)
print(family)

