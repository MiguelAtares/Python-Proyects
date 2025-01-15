#El objetivo es crear un programa que simule sacar una carta de la baraja, usando tuplas, diccionarios y conjuntos, además de algunas operaciones con ellos.
#Habrá que: mostrar todas las cartas disponibles, sacar una carta al azar actualizando la baraja y hacer operaciones con conjuntos para comparar diferentes barajas, además de lo que se me ocurra.

import random
#Creo las tuplas pues son inmutables
tupla_palos = ("Oros", "Copas", "Espadas", "Bastos")
tupla_valores = ("As", "2", "3", "4", "5", "6", "7", "Sota", "Caballo", "Rey")

#Aplicamos un contador global de cuantos palos va sacando el programa
numero_oros = 0
numero_copas = 0
numero_espadas = 0
numero_bastos = 0

#Creo un set en el que cada carta es una tupla con 2 valores: el valor y el palo. Hago un set ara luego hacer operaciones, aunque no tengan orden y sea un poco mierda.
baraja = {(valor, palo) for valor in tupla_valores for palo in tupla_palos} #Esto funciona no solo para sets, si no para otros conjuntos como listas.
print(f"Total cartas: {len(baraja)}")

#Hagamos operaciones y definamos funciones
def sacar_carta(baraja):
    global numero_oros, numero_copas, numero_espadas, numero_bastos  # Declaro variables posteriores como globales ya que si no no las podría usar. Otra opcion seria ponerlas dentro.
    # Escoge una carta al azar y desempaqueta
    carta = random.sample(list(baraja), 1)[0] #Con list pasamos el set a lista, pues no tienen orden y no lo podemos eliminar. [0] extrae el elemento de la lista que nos ha dado random (solo 1 hemos indicado)
    print(f"Carta seleccionada: {carta}")  # Verificar la carta seleccionada

    # Eliminar la carta si está en el conjunto
    if carta in baraja:
        baraja.remove(carta)
        print(f"Carta eliminada: {carta}")
    else:
        print("Error: La carta seleccionada no está en la baraja.")

    print(f"Cartas restantes: {len(baraja)}")
    
    # Ir añadiendo cuantas veces sale cada palo con el [1] pues el set (ahora convertido en lista) tiene 2 items en cada uno: valor y palo
    if carta[1] == "Oros":
        numero_oros += 1
    elif carta[1] == "Copas":
        numero_copas += 1
    elif carta[1] == "Espadas":
        numero_espadas += 1
    elif carta[1] == "Bastos":
        numero_bastos += 1
    else:
        print("No es un palo disponible")

#Ahora queremos ir sacando cartas cada vez que decimos "si", pero si ponemos "no", debe parar de sacar cartas. Para ello, hay que hacer dos bucles while, uno de sacar carta y otro de validar la entrada del usuario.
validar_sacar_carta = True
while len(baraja) > 0 and validar_sacar_carta:
    sacar_carta(baraja)
    while True:
        continuar = input("Seguimos sacando cartas? si/no:").lower()
        if continuar == "si":
            print("Toma otra cartita")
            break
        elif continuar == "no":
            validar_sacar_carta = False 
            break  #Así salimos del bucle interno de validar entrada del usuario y a la vez del externo de llamar a la función para seguir sacando cartas.
        else:
            print("Repite por favor")
print(f"Nº bastos: {numero_bastos}, nº copas: {numero_copas}, nº espadas: {numero_espadas}, nº oros: {numero_oros}")

#Creamos variables de todas las cartas de cada tipo de palo
cartas_oros = {carta for carta in baraja if carta[1] == "Oros"}
cartas_espadas = {carta for carta in baraja if carta[1] == "Espadas"}
carta_copas = {carta for carta in baraja if carta[1] == "Copas"}
carta_bastos = {carta for carta in baraja if carta[1] == "Bastos"}

#Probamos a hacer alguna operacion con sets:
cartas_oros_espadas = cartas_oros | cartas_espadas #Unión de cartas oros y espadas
print(f"1.Conjunto oros y espadas: {cartas_oros_espadas}")
interseccion_oros_espadas = cartas_oros & cartas_espadas #Con la intersección incluimos los que estan em los dos. En este caso, ninguno claro
print(f"2.Intersección oros y espadas: {interseccion_oros_espadas}")
diferencia_oros_espadas = cartas_oros - cartas_espadas
print(f"3.Diferencia oros y espadas: {diferencia_oros_espadas}") #La diferencia incluye los elementos del primer conjunto, pero no los del segundo (los resta por así decirlo si están repetidos)
diferencia_asimetrica_oros_espadas = cartas_oros ^ cartas_espadas
print(f"4.Diferencia asimétrica oros y espadas: {diferencia_asimetrica_oros_espadas}") #La diferencia asimétrica elimina los repetidos, nos da los individuales de los dos conjuntos

#Creamos una función para buscar cartas específicas en la baraja:
def buscar_cartas(baraja, valor=None, palo=None): #Hacer =None permite que los parámetros sean opcionales. Si no se pasa un valor o palo, será None
    # Filtrar por valor y/o palo
    if valor and palo:
        resultado = {carta for carta in baraja if carta == (valor, palo)} #Como ya sabes, carta aqui (las dos) es una variable temporal (una tupla de hecho) que puedo llamar de cualquier manera.
    elif valor:
        resultado = {carta for carta in baraja if carta[0] == valor} #¿Por qué pongo otro if en cada resultado =? Porque este if es el que filtra la carta específica de la baraja. Si no, me daría todas las cartas.
    elif palo:
        resultado = {carta for carta in baraja if carta[1] == palo}
    else:
        resultado = baraja  # Si no se especifica nada, devuelve toda la baraja

    return resultado

# Ejemplo de uso
print(f"Cartas con un As: {buscar_cartas(baraja, valor='As')}") #Se ponen todas con (') porque con la comilla normal (") ESTÁS CERRANDO EL F STRING. EL " SE PONE AL PRINCIPIO Y AL FINAL!
print(f"Cartas con los palos de Oros: {buscar_cartas(baraja, palo='Oros')}")
print(f"Saca el Rey de Espadas: {buscar_cartas(baraja, valor='Rey', palo='Espadas')}")

def calcular_probabilidad(baraja, valor=None, palo=None):
    if valor and palo:
        print(f"Cantidad de cartas totales: {len(baraja)}")
        probabilidad = 1/len(baraja)
    elif palo:
        cantidad_palos = {carta for carta in baraja if carta[1]==palo} #Len no funcionaria en una sola linea, tenemos que convertir primero a variable.
        print(f"Cantidad de {palo}: {len(cantidad_palos)}")
        print(f"Cantidad de cartas totales: {len(baraja)}")
        probabilidad = len(cantidad_palos) / len(baraja) 
    elif valor:
        cantidad_valores = {carta for carta in baraja if carta[0]==valor}
        print(f"Cantidad de {valor}: {len(cantidad_valores)}")
        print(f"Cantidad de cartas totales: {len(baraja)}")
        probabilidad = len(cantidad_valores) / len(baraja) 

    return probabilidad

print(f"Probabilidad Rey de Oros:{int(calcular_probabilidad(baraja, valor = 'Rey', palo = 'Oros')*100)}%")
print(f"Probabilidad de sacar cualquier carta de espadas:{int(calcular_probabilidad(baraja, palo='Espadas')*100)}%")
print(f"Probabilidad de sacar un Rey: {int(calcular_probabilidad(baraja, valor='Rey')*100)}%")





