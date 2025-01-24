
# Simulación de Baraja de Cartas con Operaciones

## Descripción General

Este programa simula una baraja de cartas y permite realizar diversas operaciones con ella. Se utilizan tuplas, conjuntos y diccionarios para gestionar las cartas y realizar tareas como:

-   Mostrar las cartas disponibles.
-   Sacar una carta al azar.
-   Realizar operaciones con conjuntos para comparar cartas.
-   Buscar cartas específicas.
-   Calcular probabilidades de sacar ciertas cartas.

## Funcionalidades Principales

### 1. Configuración Inicial

-   **Tuplas inmutables:**
    -   `tupla_palos` contiene los palos de la baraja.
    -   `tupla_valores` contiene los valores de las cartas.
-   **Set de la baraja:**
    -   Cada carta se representa como una tupla `(valor, palo)` generada dinámicamente con comprensión de conjuntos.
    -   El set permite operaciones como unión, intersección, diferencia y diferencia asimétrica.

### 2. Sacar una Carta

La función `sacar_carta(baraja)` realiza las siguientes tareas:

-   Selecciona una carta al azar utilizando `random.sample()`.
-   Elimina la carta de la baraja.
-   Lleva un conteo global de cuántas cartas de cada palo han sido sacadas.
-   Permite al usuario decidir si quiere continuar sacando cartas.

### 3. Operaciones con Conjuntos

Se realizan operaciones matemáticas con los palos de la baraja:

-   **Unión:** Combina cartas de dos palos.
-   **Intersección:** Muestra cartas comunes entre dos palos (ninguna en este caso).
-   **Diferencia:** Muestra cartas de un palo que no están en el otro.
-   **Diferencia asimétrica:** Muestra cartas únicas en cada conjunto, excluyendo las repetidas.

### 4. Buscar Cartas

La función `buscar_cartas(baraja, valor=None, palo=None)` permite filtrar cartas por valor, palo, o ambos:

-   Si se especifica un valor y un palo, devuelve la carta exacta.
-   Si solo se especifica un valor o palo, filtra las cartas correspondientes.
-   Si no se especifica nada, devuelve toda la baraja.

### 5. Calcular Probabilidades

La función `calcular_probabilidad(baraja, valor=None, palo=None)` calcula la probabilidad de sacar ciertas cartas:

-   Si se especifica un valor y un palo, la probabilidad es `1 / tamaño de la baraja`.
-   Si se especifica solo un palo o un valor, la probabilidad es la proporción de cartas correspondientes en la baraja.

## Flujo de Uso

1.  **Inicialización:**
    -   La baraja se genera automáticamente como un conjunto.
    -   Se imprime la cantidad total de cartas.
2.  **Interacción:**
    -   El usuario puede sacar cartas al azar hasta que se agoten o decida detenerse.
    -   Se muestran las cartas restantes después de cada extracción.
3.  **Operaciones y Consultas:**
    -   Comparación entre palos usando operaciones de conjuntos.
    -   Búsqueda de cartas específicas.
    -   Cálculo de probabilidades de sacar cartas específicas o de un conjunto.

## Salidas Clave

-   **Cartas disponibles:** Imprime las cartas restantes en la baraja.
-   **Resultados de operaciones:**
    -   Unión, intersección, diferencia y diferencia asimétrica entre palos.
-   **Cartas encontradas:** Resultado de búsquedas específicas.
-   **Probabilidades:** Valores calculados en porcentaje para facilitar la interpretación.


