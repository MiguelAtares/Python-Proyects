# Juego de Blackjack

## Descripción General

Este programa simula una partida de **Blackjack** para dos jugadores. Cada jugador puede sacar cartas de una baraja, sumando sus valores hasta decidir detenerse o superar los 21 puntos (lo que significa perder automáticamente). Al final, se comparan las puntuaciones de ambos jugadores para determinar al ganador.

## Funcionalidades Principales

### 1. Configuración Inicial

-   **Baraja:** Generada como una lista de listas donde cada carta tiene un valor (`1-12`) y un palo (`Oros`, `Copas`, `Espadas`, `Bastos`).
-   **Variables iniciales:**
    -   `Jugar`: Controla si el juego continúa.
    -   `puntuacion_total`: Almacena la puntuación acumulada de cada jugador.

### 2. Módulo de Juego

La función `jugar_blackjack()` realiza las siguientes tareas:

-   Solicita al jugador si desea sacar una carta.
-   Si elige "sí":
    -   Se selecciona una carta al azar de la baraja usando `random.sample()`.
    -   Se elimina la carta seleccionada de la baraja.
    -   Se actualiza la puntuación total del jugador con el valor de la carta.
-   Si elige "no", el turno del jugador finaliza.
-   Retorna la puntuación total del jugador al finalizar su turno.

### 3. Flujo de Juego

#### Turno del Jugador 1

-   Se pregunta al jugador si desea jugar.
-   Si responde "sí", se inicia su turno usando `jugar_blackjack()`.
-   Si supera los 21 puntos, pierde automáticamente.

#### Turno del Jugador 2

-   Se inicia el turno del segundo jugador de manera similar.
-   Si supera los 21 puntos, pierde automáticamente.

#### Determinación del Ganador

-   Se comparan las puntuaciones finales de ambos jugadores:
    -   **Empate:** Si las puntuaciones son iguales.
    -   **Victoria del Jugador 1:** Si su puntuación es mayor y no supera 21.
    -   **Victoria del Jugador 2:** Si su puntuación es mayor y no supera 21.

## Salidas Clave

-   **Cartas seleccionadas:** Muestra las cartas extraídas y su valor.
-   **Puntuación actual:** Se imprime después de cada carta extraída.
-   **Estado final de los jugadores:**
    -   Puntos acumulados.
    -   Mensaje indicando si han perdido por superar los 21 puntos.
-   **Resultado final:** Anuncia al ganador o si hay un empate.

## Detalles Adicionales

-   Se valida la entrada de los jugadores para evitar errores tipográficos.
-   La baraja se actualiza dinámicamente para evitar la reutilización de cartas ya extraídas.
-   El flujo incluye mensajes claros y comentarios para guiar a los jugadores durante la partida.
