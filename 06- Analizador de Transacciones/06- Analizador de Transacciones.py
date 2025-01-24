# El objetivo es hacer un analizador básico de un registro de transacciones.

transacciones = [
    "2024-12-01,Compra,100.50,Supermercado",
    "2024-12-02,Ingreso,2000.00,Salario",
    "2024-12-03,Compra,20.75,Restaurante",
    "2024-12-04,Retiro,50.00,Cajero"
]

# Separar cada transacción en una lista. Recorrer un bucle for de esta manera es hacer una list comprehension.
transacciones_depuradas1 = [transaccion.split(",") for transaccion in transacciones] 
print(transacciones_depuradas1)

#Reemplazar la palabra "Compra" por "Gasto".
transacciones_depuradas2 = [[elemento.replace("Compra", "Gasto") for elemento in transaccion] for transaccion in transacciones_depuradas1] 
print(transacciones_depuradas2)

# Extraer solo las transacciones de tipo "Gasto":
gastos = [transaccion for transaccion in transacciones_depuradas2 if transaccion[1] == "Gasto"]
print(gastos)

#Extraer el monto de las transacciones totales:
monto = [float(transaccion[2]) for transaccion in transacciones_depuradas2] 
print(monto)

# Lista de descripciones en mayúsculas
descripciones_mayus = [transaccion[3].upper() for transaccion in transacciones_depuradas2]
print(descripciones_mayus)

# Cambiar solo las descripciones a mayúsculas, manteniendo el resto de los datos
transacciones_modificadas = [ [transaccion[0], transaccion[1], transaccion[2], transaccion[3].upper()] for transaccion in transacciones_depuradas2] 
print(transacciones_modificadas)

#Calcular el total pero solo de los montos:
total_gastos =sum(float(transaccion[2]) for transaccion in transacciones_depuradas2 if transaccion[1] == "Gasto") 
print(total_gastos)

# Agrupar transacciones por tipo:
transacciones_por_tipo = { tipo: [transaccion for transaccion in transacciones_depuradas2 if transaccion[1] == tipo]
    for tipo in set(transaccion[1] for transaccion in transacciones_depuradas2)}
print(transacciones_por_tipo)

# Crear un reporte formateado:
reporte = [
    f"Fecha: {transaccion[0]}, Tipo: {transaccion[1]}, Monto: {transaccion[2]}, Descripción: {transaccion[3]}"
    for transaccion in transacciones_depuradas2
]
print("\n".join(reporte))

# Calcular el saldo total:
saldo_total = sum(
    float(transaccion[2]) if transaccion[1] in ["Ingreso"] else -float(transaccion[2])
    for transaccion in transacciones_depuradas2
)
print(saldo_total)
