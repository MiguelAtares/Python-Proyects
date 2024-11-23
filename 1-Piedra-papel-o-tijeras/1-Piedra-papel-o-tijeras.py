import random
#Objetivo del juego: el usuario elije entre "piedra", "papel" o "tijera" y la computadora hace lo mismo pero de forma aleatoria. 

#Inicializar contadores:

contador_piedra = 0
contador_tijera = 0
contador_papel = 0

contador_victorias = 0
contador_derrotas = 0
contador_empates = 0

#Condiciones del juego:

while True: 
    opciones = ["piedra", "papel", "tijera"]
    usuario = input("Elige piedra, papel o tijera (o pulsa 'exit' para salir):").lower()
    
    if usuario == "piedra":
        contador_piedra += 1
    if usuario == "tijera":
        contador_tijera += 1
    if usuario == "papel":
        contador_papel += 1

    if usuario == "exit":
        print("Gracias por jugar! Hasta luego!")
        break

    #Introducción del usuario:

    if usuario not in opciones: 
        print("No has seleccionado piedra, papel o tijera (o 'exit')")
        exit()
    computadora = random.choice(opciones)
    print(f"Tu elegiste: {usuario}")
    print(f"La computadora eligió: {computadora}")

    #Lógica del juego:

    if usuario == computadora:
        print("Habéis empatado!")
        contador_empates += 1
    elif (usuario == "piedra" and computadora == "papel") or \
        (usuario == "papel" and computadora == "tijera" ) or \
        (usuario == "tijera" and computadora == "piedra"):
        print("La computadora te ha ganado!")
        contador_derrotas += 1
    else: 
        print("HUMANITY WINS")
        contador_victorias += 1

    print(f"Has ganado {contador_victorias} veces, has perdido {contador_derrotas} y has empatado {contador_empates}.")
    print(f"Has seleccionado piedra {contador_piedra} veces, papel {contador_papel} veces y tijera {contador_tijera} veces.")

