import getpass

abecedario = "abcdefghijklmñopqrstuvwxyzáéíóú" #Añadimos tildes
adivinar_palabra = getpass.getpass("¡Juguemos al ahorcado! Dime que palabra tienen que adivinar, pero escóndela!:").lower() #De esta manera, ocultamos la palabra mientras la ponemos.
if not all(letra in abecedario for letra in adivinar_palabra): #Verifica que todas las letras estén en abecedario. all evalúa que todo sea True. Si alguna no está, hará el print. 'letra' solo está en este sitio
    print("Ese no es un carácter válido. Vuelve a empezar.")
    exit()

def ahorcado():
    intentos = 6 #Debemos poner todo fuera del bucle, si no cada vez que se reinicia el bucle, se reinicia estas variables y no queremos.
    letra_adivinada = set() #Creamos un set vacío donde vamos a ir añadiendo todas las letras que acertemos
    letras_falladas = set()
    
    while intentos > 0:
        palabra = "".join([letra if letra in letra_adivinada else "_" for letra in adivinar_palabra]) #adivinar_palabra tiene un orden específico. teta será t-e-t-a, ya que hacemos un bucle for, se evalua cada una.
        # Aquí decimos, pon la letra si letra está en la letra_adivinada. Si no, pon un _. Si es teta y yo digo e, primero se evalua la t, como no está en letra_adivinda, se pone _. Luego e si se pone, las demás son 
        print(f"Palabra actual: {palabra}")
        print(f"Letras falladas: {', '.join(letras_falladas)}") #Si pongo solo el set, me va a imprimir todo el rato: "set()"
        print(f"Intentos restantes: {intentos}")

        if palabra == adivinar_palabra:  #Ponemos esto lo primero, ya que nada mas palabra se actualice, si acertamos toda nos pondra que hemos ganado. Si lo ponemos al final, nos pedirá otra letra antes de ganar.
            print("¡Enhorabuena, has ganado!")
            exit()

        letra_seleccionada = input("Elige una letra o pulsa salir para finalizar:").lower()

        if letra_seleccionada == "salir":
             exit()

        if len(letra_seleccionada) !=1  or letra_seleccionada not in abecedario: #Validar esto es fácil. Si no es una sola letra o no está en el abecedario, fuera. ¡NO TE COMPLIQUES PONIENDO VARIAS CONDICIONES!
            print("Carácter inválido. Vuelve a intentarlo.")
            continue #¡OJO! No me acordaba, pero continue lo que hace es SALTAR TODO EL RESTO DEL CÓDIGO Y VOLVER AL BUCLE INICIALMENTE

        if letra_seleccionada in letras_falladas or letra_seleccionada in letra_adivinada:
            print(f"¡Cuidado! Ya has elegido esta letra: {letra_seleccionada}.")
            continue
        
        if letra_seleccionada in adivinar_palabra:
            print("Has certado la letra!")
            letra_adivinada.add(letra_seleccionada)

        elif letra_seleccionada not in adivinar_palabra:
            print("Esa letra no está!")
            letras_falladas.add(letra_seleccionada)
            intentos -= 1

    if intentos == 0:
        print(f"¡Has gastado todos tus intentos, has perdido! La palabra era: {adivinar_palabra}")
        exit()
    
ahorcado()
