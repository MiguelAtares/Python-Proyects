
# Juego del Ahorcado

**📢 Tienes todos los proyectos de Python bien explicados en mi canal de Youtube:**
 🔗 [@DataAnalystAtares](https://www.youtube.com/@DataAnalystAtares)

## Descripción General

Este código implementa un juego interactivo del **ahorcado**. Los usuarios deben adivinar una palabra seleccionada previamente, teniendo un límite de intentos. Se verifica cada letra ingresada, y se proporciona retroalimentación en cada turno.

## Funcionalidades Principales

### 1. Configuración del Juego

-   **Abecedario:** Incluye letras del español y tildes para validar las entradas.
-   **Palabra a adivinar:** El usuario ingresa la palabra a través de `getpass.getpass()`, que la oculta durante la entrada.
-   **Validación de palabra:** Verifica que todas las letras de la palabra pertenezcan al abecedario; de lo contrario, el programa se detiene.

### 2. Desarrollo del Juego

-   **Variables Iniciales:**
    
    -   `intentos`: Comienza con 6 intentos.
    -   `letra_adivinada`: Un conjunto vacío para almacenar letras acertadas.
    -   `letras_falladas`: Un conjunto vacío para almacenar letras erróneas.
-   **Bucle Principal:** Continúa mientras queden intentos.
    
    -   **Progreso de la Palabra:** Se muestra la palabra actual con letras acertadas y guiones bajos `_` para las restantes.
    -   **Control de Entrada:**
        -   Solicita una letra.
        -   Verifica que sea válida (una letra del abecedario y no repetida).
    -   **Evaluación de la Letra:**
        -   Si es correcta, se agrega a `letra_adivinada`.
        -   Si es incorrecta, se agrega a `letras_falladas` y se reduce el contador de intentos.
    -   **Condición de Victoria:** Si todas las letras de la palabra son acertadas, el usuario gana.
    -   **Condición de Derrota:** Si los intentos llegan a 0, el usuario pierde.

### 3. Validaciones

-   **Palabra Inicial:** Comprueba que todas las letras de la palabra a adivinar estén en el abecedario.
-   **Entrada del Jugador:**
    -   Debe ser una sola letra.
    -   Debe estar en el abecedario.
    -   No debe haber sido ingresada previamente.
-   **Control del Juego:** Permite salir del juego en cualquier momento escribiendo "salir".

## Flujo de Uso

1.  **Inicio:**
    -   El jugador introduce la palabra a adivinar.
    -   Se valida la palabra y comienza el juego.
2.  **Turnos:**
    -   Se muestra el progreso de la palabra, letras falladas e intentos restantes.
    -   El jugador ingresa una letra válida.
    -   El programa evalúa la entrada y actualiza el estado del juego.
3.  **Final:**
    -   El jugador gana si adivina toda la palabra antes de agotar los intentos.
    -   El jugador pierde si agota los intentos sin completar la palabra.

## Salidas Clave

-   **Progreso del Juego:**
    -   Palabra con letras acertadas y guiones bajos `_`.
    -   Letras falladas y número de intentos restantes.
-   **Mensajes Informativos:**
    -   Letra correcta o incorrecta.
    -   Advertencia sobre entradas no válidas o repetidas.
-   **Resultados Finales:**
    -   Mensaje de victoria o derrota, indicando la palabra correcta en caso de perder.
