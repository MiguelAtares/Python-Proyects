#El objetivo es crear un generador de contraseñas de diferentes maneras
import random

#MÉTODO 1
def nueva_contraseña1(longitud1):
    caracteres = "abcdefghijklmñopqrstuvwxyz123456789¿?!¡."
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud1)) 
    return contraseña 

longitud1 = int(input("Número de caractéres de la contraseña: "))
print(f"Tu contraseña es: {nueva_contraseña1(longitud1)}")

#MÉTODO 2
def nueva_contraseña2(longitud2):
    caracteres = "abcdefghijklmñopqrstuvwxyz123456789¿?!¡." 
    contraseña = ''.join(random.sample(caracteres,longitud2)) 
    if len(contraseña) < 6 and all(caracter not in contraseña for caracter in ("¿", "?", "!", "¡")): 
        print("Contraseña floja")
    else:
        print("Contraseña fuerte")
    return contraseña 

longitud2 = int(input("Número de caractéres de la contraseña: "))
print(f"Tu contraseña es: {nueva_contraseña2(longitud2)}")

#MÉTODO 3
def nueva_contraseña3(longitud3):
    caracteres = "abcdefghijklmñopqrstuvwxyz123456789¿?!¡."
    lista_caracteres = list(caracteres) 
    random.shuffle(lista_caracteres) 
    contraseña = ''.join(lista_caracteres)[:longitud3] 
    return contraseña

longitud3 = int(input("Número de caractéres de la contraseña: "))
print(f"Tu contraseña es: {nueva_contraseña3(longitud3)}")


#FUNCIONES import random más usadas:
#1) randint(a, b):
print(random.randint(1, 20)) #Devuelve un número entero aleatorio entre a y b, ambos incluidos.

#2) uniform(a, b)
print(random.uniform(1.5, 5.5)) #Genera un número flotante aleatorio entre a y b.

#3) choice(seq)
opciones = ["rojo", "verde", "azul"]
print(random.choice(opciones))  #Selecciona un elemento aleatorio de una secuencia (lista, tupla, cadena, etc.).

#4) sample(population, k)
numeros = [1, 2, 3, 4, 5]
print(random.sample(numeros, 3))  #Devuelve una lista de k elementos únicos seleccionados aleatoriamente de la población.

#5) shuffle(list)
lista = [1, 2, 3, 4]
print(random.shuffle(lista)) #Mezcla los elementos de una lista en su lugar. ¡PERO NO ME DA LA LISTA!
print(lista)

#6) choices(population, weights=None, k=1)
colores = ["rojo", "verde", "azul"]
print(random.choices(colores, weights=[10, 1, 1], k=2))  # Selecciona k elementos aleatorios de una población, con un peso dado (en este caso, tiene x10 veces más de probabilidad). Si fuese 10, 2, 2 (seria x5 solo)
