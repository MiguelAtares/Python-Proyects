
#Generador de Contraseñas en Python

##📢 Tienes todos los proyectos de Python bien explicados en mi canal de Youtube:
    ##🔗 [@DataAnalystAtares](https://www.youtube.com/@DataAnalystAtares)  


Este proyecto implementa un **generador de contraseñas** utilizando tres métodos diferentes. También incluye ejemplos del uso de las funciones más comunes del módulo `random` en Python. El objetivo principal es demostrar varias formas de crear contraseñas de diferentes niveles de complejidad y flexibilidad.

----------

**Objetivo del proyecto**

El objetivo es crear contraseñas seguras y aleatorias, ofreciendo tres enfoques diferentes:

1.  Utilizar una selección aleatoria de caracteres basada en una cadena de caracteres definidos.
2.  Incorporar validación de fortaleza de contraseñas.
3.  Usar operaciones avanzadas como barajado de listas.

----------

**Explicación de los métodos**

1.  **Método 1: Generación básica de contraseñas**
    
    -   Este método utiliza `random.choice()` para seleccionar caracteres de una cadena predefinida.
    -   Se define una longitud ingresada por el usuario y se genera una contraseña concatenando caracteres aleatorios.
    
    **Ventaja:** Simple y fácil de implementar.
    
    **Proceso:**
    
    -   Se toma una cadena de caracteres posibles (`abcdefghijklmñopqrstuvwxyz123456789¿?!¡.`).
    -   Se genera una contraseña utilizando un bucle en combinación con `random.choice()`.
    
    **Salida esperada:** Una contraseña de la longitud deseada, por ejemplo: `8m¿pqrj`.
    
2.  **Método 2: Validación de fortaleza de contraseñas**
    
    -   Este método utiliza `random.sample()` para garantizar que no se repitan caracteres dentro de la contraseña.
    -   Además, incluye validaciones para comprobar si la contraseña es "fuerte" o "débil" basándose en su longitud y la inclusión de caracteres especiales.
    
    **Ventaja:** Ofrece validación de seguridad básica.
    
    **Proceso:**
    
    -   Se utiliza `random.sample()` para seleccionar caracteres únicos.
    -   Se verifica que la contraseña tenga al menos 6 caracteres y contenga símbolos especiales como `¿`, `!`, `¡`.
    
    **Salida esperada:**
    
    -   Contraseña con validación de seguridad. Por ejemplo:
        -   Contraseña débil: `a3fb`.
        -   Contraseña fuerte: `m¿6tn?`.
3.  **Método 3: Barajado y generación avanzada**
    
    -   Este método utiliza `random.shuffle()` para mezclar una lista de caracteres.
    -   Posteriormente, se toma una subcadena de la lista mezclada para generar la contraseña.
    
    **Ventaja:** Genera contraseñas más impredecibles al utilizar un orden completamente aleatorio de caracteres.
    
    **Proceso:**
    
    -   Convierte una cadena de caracteres en una lista.
    -   Baraja la lista con `random.shuffle()` y selecciona los primeros `n` caracteres.
    
    **Salida esperada:** Una contraseña con los caracteres mezclados, por ejemplo: `q4nm¿`.
    

----------

**Funciones comunes del módulo `random`**

Además de los generadores de contraseñas, el código incluye ejemplos prácticos de las funciones más comunes del módulo `random`:

1.  **`random.randint(a, b)`**
    
    -   Devuelve un número entero aleatorio entre `a` y `b` (incluyendo ambos).
    -   Ejemplo: `random.randint(1, 20)` podría devolver `15`.
2.  **`random.uniform(a, b)`**
    
    -   Genera un número flotante aleatorio entre `a` y `b`.
    -   Ejemplo: `random.uniform(1.5, 5.5)` podría devolver `3.14`.
3.  **`random.choice(seq)`**
    
    -   Selecciona un elemento aleatorio de una secuencia como una lista o cadena.
    -   Ejemplo: `random.choice(["rojo", "verde", "azul"])` podría devolver `verde`.
4.  **`random.sample(population, k)`**
    
    -   Devuelve una lista de `k` elementos únicos seleccionados aleatoriamente de la población.
    -   Ejemplo: `random.sample([1, 2, 3, 4, 5], 3)` podría devolver `[3, 1, 5]`.
5.  **`random.shuffle(list)`**
    
    -   Mezcla los elementos de una lista en su lugar (sin devolver una nueva lista).
    -   Ejemplo: Mezclar `[1, 2, 3, 4]` con `random.shuffle()` podría dar `[3, 1, 4, 2]`.
6.  **`random.choices(population, weights=None, k=1)`**
    
    -   Selecciona `k` elementos aleatorios de una población con probabilidades opcionales (pesos).
    -   Ejemplo: `random.choices(["rojo", "verde", "azul"], weights=[10, 1, 1], k=2)` podría devolver `["rojo", "azul"]`.
    - 
 **Conclusión**

Este proyecto ofrece una introducción práctica a la generación de contraseñas utilizando diferentes enfoques. También demuestra el uso de las herramientas más versátiles del módulo `random`.

Si tienes ideas para mejorar o ampliar este generador de contraseñas, ¡abre un issue o envía un pull request! 🚀

