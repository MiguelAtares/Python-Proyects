import json 
import os 

directorio_actual = os.path.dirname(os.path.abspath(__file__)) 
ruta_archivo = os.path.join(directorio_actual, "inventario.json") 

print(f"Directorio actual del script: {directorio_actual}")
print(f"Ruta esperada del archivo JSON: {ruta_archivo}")


# A)Crea un archivo JSON vacío con una estructura inicial ({"productos": []}) si no existe. Útil para inicializar el sistema de inventario y evitar errores al leer o modificar un archivo inexistente. 
def crear_json(): 
    try:
        datos_iniciales = {"productos": []} 
        with open(ruta_archivo, "w") as archivo: 
            json.dump(datos_iniciales, archivo, indent=4) 
        print(f"Archivo JSON creado con éxito en {ruta_archivo}")
    except Exception as e:
        print(f"Error al crear el archivo: {e}")

if not os.path.exists("inventario.json"): 
    crear_json()

# B) Carga los datos del archivo JSON y los convierte en un diccionario de Python. Permite trabajar con el contenido del inventario en memoria. Si el archivo no existe, maneja el error y devuelve None.
def leer_json():
    try:
        with open(ruta_archivo, "r") as archivo: 
            return json.load(archivo) 
    except FileNotFoundError:
        print("El archivo JSON no existe")
        return None

# C) Sobrescribe el archivo JSON con datos actualizados. Recibe un diccionario en memoria, lo convierte a formato JSON y lo guarda en el archivo. Es esencial para persistir los cambios realizados en el inventario.
def guardar_json(datos):
    try:
        with open(ruta_archivo, "w") as archivo:  
            json.dump(datos, archivo, indent=4) 
        print("Inventario actualizado correctamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

# D) Lee y muestra los productos del inventario. Utiliza leer_json para acceder al contenido y formatea la salida de forma legible. Si el inventario está vacío, muestra un mensaje adecuado. No modifica ni guarda datos.
def mostrar_inventario():
    inventario = leer_json() 
    if inventario and "productos" in inventario: 
        print("\nInventario actual:")
        for idx, producto in enumerate(inventario["productos"], start=1): 
            print(f"{idx}. {producto['nombre']} - Cantidad: {producto['cantidad']} - Precio: {producto['precio']}")
    else:
        print("\nEl inventario está vacío.")

#Perfecto, ya tenemos una herramienta para crear, leer, guardar y actualizar el JSON y ya es visible en la consola. Ahora queda poder actualizar el inventario.

def añadir_producto():
    nuevo = leer_json()
    if nuevo is None:
        return
    
    nombre = input("Nombre del producto:")
    try:
        cantidad = int(input("Cantidad de producto: "))
        precio = float(input("Precio del producto: "))
    except ValueError:
        print("Error: La cantidad debe ser un número entero y el precio un número decimal.")
        return


    for producto in nuevo["productos"]:
        if producto["nombre"].lower() == nombre.lower():
            print("El producto ya existe. Modifica su cantidad o precio desde el menú.")
            return
    nuevo["productos"].append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    guardar_json(nuevo)
    print(f"Producto: {nombre} añadido con éxito.")

def modificar_producto():
    modificar = leer_json()
    if modificar is None:
        print("Error: No se pudo leer el archivo JSON.")
        return
    
    nombre = input("Nombre del producto a modificar: ")
    for producto in modificar["productos"]:
        if producto["nombre"].lower() == nombre.lower():
            try:
                cantidad = int(input(f"Añade o elimina cantidad para '{nombre}' (Actual: {producto['cantidad']}): "))
                precio = float(input(f"Añade, elimina o manten el precio para '{nombre}' (Actual: {producto['precio']}): "))
            except ValueError:
                print("Error: La cantidad debe ser un número entero y el precio un número decimal.")
                return

            if producto["cantidad"] + cantidad < 0:
                print("Error: La cantidad no puede ser negativa.")
                return
            if producto["precio"] + precio < 0:
                print("Error: El precio no puede ser negativo.")
                return
            
            producto["cantidad"] += cantidad 
            producto["precio"] += precio
            guardar_json(modificar)
            print(f"Producto '{nombre}' actualizado con éxito.")
            return
        
    print("El producto a modificar no existe") 

def eliminar_producto():
    eliminar = leer_json()
    if eliminar is None:
        return
    
    nombre = input("Producto a eliminar:")
    for producto in eliminar["productos"]:
        if producto["nombre"].lower() == nombre.lower():
            eliminar["productos"].remove(producto)
            guardar_json(eliminar)
            print(f"Producto {nombre} eliminado con éxito")
            return
        
    print("El producto a eliminar no existe")

def menu():
   
    while True:
        mostrar_inventario() 
        print("\n-- Fin del inventario --")
        print("\nOpciones:")
        print("1. Añadir producto")
        print("2. Modificar producto")
        print("3. Eliminar producto")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            añadir_producto()
        elif opcion == "2":
            modificar_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
menu()
