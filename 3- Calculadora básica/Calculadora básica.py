#Objetivo: crear una calculadora básica

print("¡Bienvenido a mi calculadora básica! Puedes sumar (+), restar (-), multiplicar (*) o dividir (/).")
def calculadora(num1, operador,num2):
    print("¡Oh, calcular eso es muy fácil!")
    if operador == "+":
        print(num1 + num2)
    elif operador == "-":
        print(num1 - num2)
    elif operador == "*":
        print(num1 * num2)
    elif operador == "/":
        if num2 == 0:
            print("Error: has dividido por 0")
        else:
            print(num1 / num2)
    else:
        print("Algo ha ido mal")

numero1 = float(input("Número 1: ")) 
operación = input("Operación: ")
numero2 = float(input("Número 2: ")) 
calculadora(numero1,operación,numero2)

#SIMPLIFICAR SI SIEMPRE QUIERO HACER SIEMPRE LA MISMA OPERACIÓN:

numero1 = float(input("Número 1: "))
numero2 = float(input("Número 2: "))
calculadora(numero1, "+", numero2)
calculadora(numero1, "-", numero2)
calculadora(numero1, "*", numero2)
calculadora(numero1, "/", numero2)

#¿QUIERO HACERLO CONSTANTEMENTE?:

while True:

    entrada1 = input("Número 1 (o pulsa salir): ").lower()
    if entrada1 == "salir": 
        break

    entrada2 = input("Número 2 (o pulsa salir): ").lower()
    if entrada2 == "salir":
        break

    try:
        numero1 = float(entrada1)
        numero2 = float(entrada2)
    except ValueError: 
        print("Error. Ingresa numeros válidos o sal del programa.")
    
    calculadora(numero1, "+", numero2)
