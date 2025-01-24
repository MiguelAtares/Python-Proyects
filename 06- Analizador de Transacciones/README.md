
# Analizador Básico de Registro de Transacciones

## Descripción General

Este código implementa un analizador básico para procesar un registro de transacciones financieras. Permite realizar diversas operaciones sobre las transacciones, como filtrar, modificar, calcular totales y generar reportes.

## Funcionalidades Principales

### 1. Procesar Transacciones

-   Las transacciones iniciales son strings que se convierten en listas utilizando **list comprehensions**.
-   Se separan los elementos de cada transacción (`Fecha`, `Tipo`, `Monto`, `Descripción`).

### 2. Modificar Transacciones

-   Se reemplaza la palabra `"Compra"` por `"Gasto"` en las transacciones.
-   Las descripciones se pueden convertir a mayúsculas manteniendo el resto de los datos intactos.

### 3. Filtrar Transacciones

-   Se extraen solo las transacciones de tipo `"Gasto"` para análisis adicional.
-   Las transacciones se agrupan por tipo (`Ingreso`, `Gasto`, `Retiro`) en un diccionario para facilitar el acceso.

### 4. Calcular Montos y Totales

-   Se extraen los montos individuales de todas las transacciones.
-   Se calcula el total de gastos sumando únicamente los montos de transacciones de tipo `"Gasto"`.
-   Se calcula el saldo total considerando ingresos como positivos y gastos/retiros como negativos.

### 5. Generar Reporte Formateado

-   Se crea un reporte de todas las transacciones en formato legible, con detalles como fecha, tipo, monto y descripción.

## Flujo de Uso

1.  **Procesar y Limpiar Transacciones:**
    -   Se separan y procesan los datos para facilitar su análisis.
2.  **Modificaciones Específicas:**
    -   Cambiar palabras clave (`Compra` a `Gasto`) o formatos (`descripciones` en mayúsculas).
3.  **Filtrados y Agrupaciones:**
    -   Extraer transacciones según criterios como tipo o descripción.
4.  **Cálculos Financieros:**
    -   Determinar totales de gastos e ingresos.
    -   Calcular el saldo final.
5.  **Generación de Reporte:**
    -   Crear una vista consolidada de todas las transacciones.

## Salidas Clave

-   **Transacciones Depuradas:** Una lista de listas que contiene los datos organizados.
-   **Transacciones Agrupadas:** Un diccionario donde las claves son tipos de transacción y los valores son listas de transacciones de ese tipo.
-   **Reporte:** Un listado legible de todas las transacciones, con formato específico.
-   **Totales:**
    -   Total de gastos.
    -   Saldo total.
