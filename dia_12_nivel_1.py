#DIA 12 NIVEL 1

#1 Id 
import random
import string

def random_user_id():
    caracteres = string.ascii_letters + string.digits
    id_aleatorio = ''.join(random.choice(caracteres) for _ in range(6))
    return id_aleatorio

print(random_user_id())  


#2
def user_id_gen_by_user():
    import random
    import string

num_caracteres = int(input("¿Cuántos caracteres por ID?: "))
num_ids = int(input("¿Cuántos IDs quieres generar?: "))

caracteres = string.ascii_letters + string.digits

for _ in range(num_ids):
    id_generado = ''.join(random.choice(caracteres) for _ in range(num_caracteres))
    print(id_generado)


#3 Color RGB
import random

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())  
