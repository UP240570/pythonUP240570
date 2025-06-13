#DIA 5 NIVEL 1

#DECLARAR LISTA VACIA
lista_vacia = []



#LISTA CON 5 ELEMENTOS
numeros = [1, 2, 3, 4, 5, 6]



#LONGITUD DE LISTA
print(len(numeros))



#TOMAR EL PRIMER, MEDIO Y ULTIMO NUMERO DE LA LISTA
print("Primero:", numeros[0])
print("Medio:", numeros[len(numeros) // 2])
print("Último:", numeros[-1])


#DECLARAR VARIABLE mixed_data_types
mixed_data_types = ["Elisabeth", 12, 1.50, "soltera", "México"]



#LISTA DE EMPRESAS
compañia = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]



#IMPRIMIR COMPAÑIA
print(compañia)



#NUMERO DE COMPAÑIAS EN LA LISTA
print("Número de empresas:", len(compañia))



#COMPAÑIA DE ENMEDIO INICIO Y FINAL
print("Primera:", compañia[0])
print("Media:", compañia[len(compañia)//2])
print("Última:", compañia[-1])



#CAMBIAR GOOGLE POR OPNEIA
compañia[1] = "OpenAI"
print(compañia)



#AGREGAR EMPRESA 
compañia.append("Tesla")
print(compañia)



#INSERTAR EMPRESA EN MEDIO
medio = len(compañia) // 2
compañia.insert(medio, "Intel")
print(compañia)



#CONVERTIR EMPRESA EN MATUSCULAS
compañia[0] = compañia[0].upper()
print(compañia)



#UNIR EMPRESAS CON #;
unidas = "#; ".join(compañia)
print(unidas)



#VERIFICAR SI UNA EMPRESA ESTA EN LA LISTA
print("Google" in compañia)



#ORDENRA POR ALFABETO
compañia.sort()
print(compañia)



#INVERTIR ORDEN
compañia.sort()
print(compañia)



#CORTAR 3 PRIMERAS EMPRESAS
print(compañia[:3])



#CORTAR LAS ULTIMAS 3
print(compañia[-3:])



#CORTAR EMPRESAS DE ENMEDIO
medio = len(compañia) // 2
if len(compañia) % 2 == 0:
    print(compañia[medio-1:medio+1])
else:
    print(compañia[medio])



#ELIMINAR PRIMER EMPRESA
compañia.pop(0)
print(compañia)



#ELIMNAR EMPRESA DEL MEDIO
medio = len(compañia) // 2
compañia.pop(medio)
print(compañia)



#ELIMINAR ULTIMA EMPRESA
compañia.pop()
print(compañia)



#ELIMINAR TODAS LAS EMPRESAS
compañia.clear()
print(compañia)


#DESTRUIR LISTA
del compañia



#UNIR DOS LISTAS
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
union = front_end + back_end
print(union)



# INSERTAR DESPUES DE REDUX
union.insert(5, 'Python')
union.insert(6, 'SQL')
print(union)

