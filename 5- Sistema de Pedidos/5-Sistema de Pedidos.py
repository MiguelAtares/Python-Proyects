#El objetivo es crear un sistema de pedidos de comida

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

def mostrar_menu(menu):
    print("Menú de comida:")
    for plato,precio in menu.items():  
        print(f"{plato}: ${precio}")
mostrar_menu(menu) 

def tomar_pedido(menu):
    pedido = [] 
    total_precio = 0 
    while True:
        plato = input("Elija cada pieza del menu por separado o pulse 'salir' si ya no quiere más:")
        if plato == "salir" and pedido == []: 
            exit()
        elif plato in menu: 
            precio_plato = menu[plato] 
            pedido.append(plato)
            total_precio += precio_plato
            print(f"Has añadido: {plato}, que cuesta ${precio_plato}")
            print(f"Total acumulado hasta ahora: ${total_precio}")
        elif plato == "salir":
            break
        else:
            print("El plato seleccionado no está en el menú. Vuélvalo a intentar.")
    total_platos = len(pedido) 
    return pedido, total_platos, total_precio 

pedido_usuario, total_pedidos, total_dinero = tomar_pedido(menu) 
print(f"Tu pedido final es: {pedido_usuario}") 
print(f"Has pedido {total_pedidos} cosas")
print(f"El precio total es: ${total_dinero}")

def borrar_pedidos(menu):
    continuar = True 
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
                    pedido_usuario.remove(plato_eliminado) 
                    print(f"Perfecto, has eliminado: {plato_eliminado}")
                elif plato_eliminado == "salir":
                    continuar = False 
                    break
                else:
                    print("Ese plato no se encuentra entre los que ha selccionado.")
        else:
            print("No te he entendido. ¿'si' o 'no' ?:")
    return precio_eliminado_total 
precio_eliminado = borrar_pedidos(menu) 
total_dinero -= precio_eliminado
print(f"Tu pedido final es: {pedido_usuario}")
print(f"El total es: ${total_dinero}")
