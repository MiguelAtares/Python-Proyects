import random
lista_palos_blackjack = ["Oros", "Copas", "Espadas", "Bastos"]
lista_valores_blackjack = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
baraja_blackjack = [[valor, palo] for valor in lista_valores_blackjack for palo in lista_palos_blackjack]

Jugar = True
def jugar_blackjack ():
    puntuacion_total = 0
    while Jugar == True:
        sacar_carta = input(f"Cartas actuales en blackyack: {len(baraja_blackjack)}. ¿Sacamos una carta? si/no").lower()
        if sacar_carta == "si":
            carta_blackjack = random.sample(baraja_blackjack, 1)[0]
            print(f"Valor sacado: {carta_blackjack}")
            baraja_blackjack.remove(carta_blackjack)
            puntuacion_total += (carta_blackjack[0])
            print(puntuacion_total)
        elif sacar_carta == "no":
            break
        else:
            print("¿Puedes repetir por favor?")
    return puntuacion_total

while True:
    jugador1 = input("¿Quieres jugar al blackjack? si/no").lower()
    if jugador1 == "si":
            total_puntos = jugar_blackjack()
            break
    elif jugador1 == "no":
        print("Tu te lo pierdes!")
        exit()
    else:
        print("¿Cómo? No te he entendido")

total_puntos_jugador1 = total_puntos
if total_puntos_jugador1 > 21:
    print("Has obtenido más de 21 puntos, has perdido!")
elif total_puntos_jugador1 <= 21:
    print("Muy bien, veamos como lo hace el segundo jugador...")

while True:
    jugador2 = input("¿Quieres jugar al blackjack? si/no").lower()
    if jugador2 == "si":
            total_puntos = jugar_blackjack()
            break
    else:
        print("Bueno, ya has quedado con tu amigo para jugar... JUEGA")

total_puntos_jugador2 = total_puntos
if total_puntos_jugador2 > 21:
    print("Has obtenido más de 21 puntos, has perdido!")
elif total_puntos_jugador2 <= 21:
    print("Muy bien, es hora de desvelar las cartas de los dos!")

print(f"Total puntos jugador 1: {total_puntos_jugador1}")
print(f"Total puntos jugador 2: {total_puntos_jugador2}")

if total_puntos_jugador1 == total_puntos_jugador2:
     print("Habeis empatado!")
elif total_puntos_jugador1 > total_puntos_jugador2:
     print("Jugador 1 ha ganado!")
else:
     print("Jugador 2 ha ganado!")


