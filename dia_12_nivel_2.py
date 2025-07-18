#DA 12 NIVEL 2

#1 Colores hexadecimales
import random

def list_of_hexa_colors(n):
    colores = []
    for _ in range(n):
        color = '#'
        for _ in range(6):
            color += random.choice('0123456789abcdef')
        colores.append(color)
    return colores

print(list_of_hexa_colors(3))


#2 Lista RGB
def list_of_rgb_colors(n):
    colores = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colores.append(f"rgb({r},{g},{b})")
    return colores

print(list_of_rgb_colors(3))


#3 Genera cualquier color
def generate_colors(tipo, cantidad):
    if tipo == 'hexa':
        return list_of_hexa_colors(cantidad)
    elif tipo == 'rgb':
        return list_of_rgb_colors(cantidad)
    else:
        return "Tipo inválido. Usa 'hexa' o 'rgb'."

# Ejemplos:
print(generate_colors('hexa', 3))
print(generate_colors('rgb', 2))
