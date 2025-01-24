# Piedra, Papel o Tijeras

## Objetivo del proyecto:
Este proyecto consiste en desarrollar un juego interactivo donde el usuario elige entre "piedra", "papel" o "tijera", y la computadora selecciona aleatoriamente una opción. El programa evalúa las elecciones y determina al ganador según las reglas clásicas del juego.

---

## Explicación del código paso a paso:

### 1. Importación de la librería `random`:
El primer paso del programa es importar la librería `random`. Esto nos permite utilizar funciones para generar valores aleatorios, esenciales para que la computadora tome una decisión impredecible. En este caso, usaremos `random.choice()` para seleccionar entre las opciones disponibles: "piedra", "papel" o "tijera".

### 2. Inicialización de contadores:
- **Contadores de selección:** Para registrar cuántas veces el usuario elige "piedra", "papel" o "tijera".
- **Contadores de resultados:** Para contabilizar las victorias, derrotas y empates acumulados durante la sesión.

Todos los contadores se inicializan en 0, ya que no hay datos previos cuando el programa comienza.

### 3. Creación del bucle principal:
Para permitir al usuario jugar indefinidamente hasta que decida salir, utilizamos un bucle `while`. Dentro de este bucle:
- Creamos una lista `opciones` que contiene las elecciones posibles: `"piedra"`, `"papel"` y `"tijera"`.
- Pedimos al usuario que introduzca su elección mediante la función `input()`. Usamos `.lower()` para garantizar que su entrada sea reconocida correctamente, independientemente de si escribe en mayúsculas o minúsculas.
- Incluimos la opción de salida con el comando `"exit"`. Si el usuario introduce `"exit"`, se utiliza `break` para detener el bucle y finalizar el juego.

### 4. Validación de la entrada del usuario:
Para evitar entradas inválidas, comprobamos si la elección del usuario pertenece a la lista `opciones`. Si no es así, usamos `exit()` para terminar el programa.

### 5. Elección de la computadora:
La elección de la computadora se realiza usando la función `random.choice(opciones)`.

### 6. Lógica del juego:
Definimos las reglas para determinar el resultado de cada partida:
- **Empate:** Si la elección del usuario y la de la computadora son iguales.
- **Derrota:** Si la elección del usuario pierde contra la de la computadora.
- **Victoria:** Si la elección del usuario gana frente a la de la computadora.

Actualizamos los contadores correspondientes y mostramos el resultado al jugador.

### 7. Actualización y visualización de estadísticas:
Tras cada ronda, mostramos estadísticas acumuladas:
- Número de victorias, derrotas y empates.
- Frecuencia de selección de cada opción por parte del usuario.

---

## Conclusión:
Este proyecto ha sido una gran forma de aprender y poner en práctica varios conceptos clave de la programación, como bucles, condicionales y listas. También me ha ayudado a estructurar el código para que sea claro y fácil de leer.

¡Estoy emocionado de seguir aprendiendo y creando proyectos más complejos en el futuro! 🚀
