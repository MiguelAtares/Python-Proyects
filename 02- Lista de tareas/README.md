# Lista de Tareas

📢 Tienes todos los proyectos de Python bien explicados en mi canal de Youtube:
    🔗 [@DataAnalystAtares](https://www.youtube.com/@DataAnalystAtares)  

## 1. Introducción: la lista inicial

El objetivo de este programa es gestionar una lista diaria de tareas. Para comenzar, se definen dos listas principales:

- **`tareas_diarias`**: Contiene una lista predeterminada de tareas rutinarias.
- **`day_of_week`**: Enumera los días de la semana en español para validar la entrada del usuario.

El programa solicita al usuario que indique el día de la semana actual, y a partir de ahí decide cómo gestionar la lista de tareas para ese día.

---

## 2. Validación del día de la semana

Para garantizar que el usuario introduce un día válido, usamos un bucle `while True`. Dentro del bucle:

- Se solicita al usuario que introduzca un día mediante `input()`.
- Si el día ingresado pertenece a la lista `day_of_week`, el bucle se rompe con `break`.
- Si no es válido, mostramos un mensaje de error y el bucle vuelve a preguntar.

Este enfoque asegura que el usuario solo pueda avanzar cuando introduce un día correcto.

---

## 3. Tareas entre semana

Para los días laborables (lunes a viernes), se siguen los siguientes pasos:

1. Se imprimen las tareas diarias predefinidas.
2. Se ofrece al usuario la opción de añadir nuevas tareas mediante un bucle:
   - Si el usuario elige "sí", se le solicita que añada tareas una por una, usando otro bucle. Puede seguir añadiendo hasta que escriba `"salir"`.
   - Si elige "no", se muestra la lista definitiva y el programa avanza.
3. Cualquier respuesta inválida vuelve a preguntar hasta obtener una entrada clara.

Esto permite flexibilidad al usuario para personalizar su lista de tareas según lo necesite.

---

## 4. Sábado: tareas especiales

Para el sábado, el programa añade una tarea específica (`"Poner la lavadora"`) al inicio de la lista y elimina la segunda tarea de la lista original. Esto refleja que los fines de semana suelen incluir actividades diferentes.

El flujo después de estos cambios es idéntico al de los días laborables: permite añadir tareas adicionales o conservar la lista tal cual.

---

## 5. Domingo: día de descanso

El domingo se trata como una excepción. El programa imprime un mensaje indicando que es un día de descanso y no permite añadir tareas nuevas. Esto evita que el usuario programe actividades en un día dedicado al reposo.

---

## Conclusión

Este proyecto me ha servido para practicar cómo estructurar programas más dinámicos y adaptables. Me gusta que cada día de la semana tenga su propio flujo de tareas porque refleja cómo organizamos nuestra vida real, lo que hace que el programa tenga un propósito muy práctico.

Además, trabajar con bucles anidados, listas y condicionales me ha ayudado a mejorar la lógica detrás de las decisiones del programa. Algo que me ha resultado interesante es cómo cada entrada del usuario puede guiar el programa hacia un comportamiento diferente. Por ejemplo, el hecho de que los fines de semana se gestionen de manera especial o que el domingo sea un día de descanso muestra cómo podemos personalizar un código para que se ajuste a nuestras necesidades.

En general, este ejercicio no solo me ha enseñado más sobre programación, sino también sobre cómo organizarme mejor. Poco a poco, voy viendo cómo los proyectos se hacen más interesantes, y eso me motiva a seguir aprendiendo y experimentando con nuevas ideas.

¡A por el siguiente proyecto! 😊
