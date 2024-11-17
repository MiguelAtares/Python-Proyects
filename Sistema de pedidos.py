#El objetivo es crear un sistema de pedidos de comida

#Creamos una biblioteca con los menus y su valor ($) asociado:

menu = {
    "Pizza":10,
    "Hamburguesa": 8,
    "Ensalada": 6,
    "Bocadillo": 7.5,
    "Agua": 2,
    "Bebida con gas": 2.5,
    "Vino blanco": 12,
    "Vino tinto": 11
}
#Creamos la función mostrar menu:

def mostrar_menu(menu):
    print("Menú de comida:")
    for plato,precio in menu.items():  #Lo que hace el .items() es darme acceso a los strings (el 1º valor) y sus numeros (el 2º valor). Ya sabes que lo de después de for, lo llamo como quiero yo.
        print(f"{plato}: ${precio}")
mostrar_menu(menu) #Al llamar a la función, la ejecuto.

def tomar_pedido(menu):
    pedido = [] #Creo una lista vacía, que será el pedido del usuario.
    total_precio = 0 #El precio va sumando en función a los platos que pida
    while True:
        plato = input("Elija cada pieza del menu por separado o pulse 'salir' si ya no quiere más:")
        if plato == "salir" and pedido == []: #Así, si elijes de primeras 'salir' no se imprime lo demás de codigo. NO funciona si pones 'False' o si pones 0. Debes poner la lista vacía: [].
            exit()
        elif plato in menu: #Cuando yo le pido que lo recorra en "menu", al ser una biblioteca, solo busca los valores de string, pero no los numéricos. Por eso funciona. El 1º nombre (plato) da igual.
            precio_plato = menu[plato] #Esto lo que hace es acceder al valor ($) asociado al input que asignamos como plato, en el diccionario menu.
            pedido.append(plato)
            total_precio += precio_plato
            print(f"Has añadido: {plato}, que cuesta ${precio_plato}")
            print(f"Total acumulado hasta ahora: ${total_precio}")
        elif plato == "salir":
            break
        else:
            print("El plato seleccionado no está en el menú. Vuélvalo a intentar.")
    total_platos = len(pedido) #Aquí calculo en nº de veces que se ha pedido algo
    return pedido, total_platos, total_precio #Return lo que hace es que, cuando yo llame a esta función, me devuelva exactamente pedido, total_platos y total_precio, que ya estará actualizado con los platos.

pedido_usuario, total_pedidos, total_dinero = tomar_pedido(menu) #Llamo a la función. Cada variable corresponde al valor que me devuelve return, en orden claro.
print(f"Tu pedido final es: {pedido_usuario}") #En todas estas, imprimo en orden el resulado de la función de cada uno de los variables a los que doy return.
print(f"Has pedido {total_pedidos} cosas")
print(f"El precio total es: ${total_dinero}")

def borrar_pedidos(menu):
    continuar = True #Esto es para controlar correctamente todos los bucles. No tienes forma de romper el bucle siguiente, asi que haces que cuando acabe ese, pongas esta variable como False.
    precio_eliminado_total = 0
    eliminar_pedido = input("¿Quieres borrar algun plato o bebida? Escriba 'si' o 'no':")
    while continuar: 
        if eliminar_pedido == "no":
            break
        elif eliminar_pedido == "si":
            while True:
                plato_eliminado = input(f"Elija los productos a eliminar o pulse 'salir'. Su lista actual es: {pedido_usuario} Eliminar:")
                if plato_eliminado in pedido_usuario:
                    precio_plato_eliminado = menu[plato_eliminado]
                    precio_eliminado_total += precio_plato_eliminado
                    pedido_usuario.remove(plato_eliminado) # .pop aqui no vale, ya que esto es una cadena de texto.
                    print(f"Perfecto, has eliminado: {plato_eliminado}")
                elif plato_eliminado == "salir":
                    continuar = False #Aqui es donde ponemos Falso esto, para que una vez termine este bucle, acabe denegandose el externo.
                    break
                else:
                    print("Ese plato no se encuentra entre los que ha selccionado.")
        else:
            print("No te he entendido. ¿'si' o 'no' ?:")
    return precio_eliminado_total #Le doy a devolver a la función de arriba del todo. Si esta función está en algun if, si no se ejecuta esa condición, nunca se crea la variable y da error al dar return.
precio_eliminado = borrar_pedidos(menu) #Llamo a la función. Me va a devolver lo que le doy en return. Si antes elijo no, no quito nada y precio_eliminado = 0. Si elijo que si, se va sumando.
total_dinero -= precio_eliminado
print(f"Tu pedido final es: {pedido_usuario}")
print(f"El total es: ${total_dinero}")


                




    

