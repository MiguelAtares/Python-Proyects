**EXPLICACIÓN SISTEMA DE PEDIDOS**

**OBJETIVO:**

El objetivo de este proyecto es crear un sistema que permita gestionar pedidos de comida de manera sencilla y eficiente, utilizando funciones, bibliotecas y retornos para estructurar correctamente el código.

**1. Creación de la biblioteca del menú:**

Comenzamos definiendo una biblioteca (menu) que contiene los platos disponibles junto con sus precios. Esto nos permite trabajar con una estructura clara, donde cada plato (clave) está asociado a un valor (precio). Esto facilita la consulta y manipulación de los datos.

**2. Función para mostrar el menú:**

La función mostrar\_menu(menu) se encarga de imprimir todos los platos y precios de la biblioteca. Para recorrer la biblioteca usamos un bucle for con el método .items(), que nos da acceso tanto a las claves como a los valores (platos y precios). Esto asegura que al llamar a la función, podemos mostrar el menú completo. Llamamos a la función con mostrar\_menu(menu) para ejecutarla y mostrar el menú al usuario.

**3. Función para tomar pedidos:**

Esta función, tomar\_pedido(menu), permite al usuario realizar un pedido paso a paso. El flujo es similar al de un restaurante: primero el usuario observa el menú y luego selecciona los platos que desea añadir a su pedido.

1. **Variables iniciales:**
   1. pedido: una lista vacía que almacena los platos seleccionados.
   1. total\_precio: una variable para calcular el costo acumulado del pedido.
1. **Bucle while True:**
   1. Solicitamos al usuario un plato mediante input().
   1. Creamos varias condiciones para manejar las entradas:
      1. Si el usuario escribe "salir" con un pedido vacío (pedido == []), el programa termina inmediatamente con exit().
      1. Si el plato ingresado está en el menú, se calcula su precio, se añade al pedido, y se actualiza el precio total.
      1. Si el usuario escribe "salir" tras añadir platos, el bucle se rompe.
      1. Si el usuario escribe algo inválido, mostramos un mensaje de error.
1. **Retorno de valores:** Al final, devolvemos tres valores:
   1. pedido: la lista de platos seleccionados.
   1. total\_platos: la cantidad total de platos (calculada con len()).
   1. total\_precio: el costo total.

Al llamar a esta función, asignamos los valores retornados a tres nuevas variables:

*pedido\_usuario, total\_pedidos, total\_dinero = tomar\_pedido(menu)*

Estas variables se imprimen posteriormente para mostrar un resumen del pedido.

**4. Función para borrar pedidos:**

La función borrar\_pedidos(menu) permite al usuario eliminar platos de su pedido en caso de arrepentirse. Este paso es útil para replicar situaciones reales donde las decisiones cambian.

1. **Control de bucles:**
   1. Usamos una variable continuar = True para manejar un bucle interno y externo. Esto permite salir del bucle más interno y, al mismo tiempo, finalizar el proceso de eliminación si el usuario lo decide.
1. **Flujo de eliminación:**
   1. Preguntamos si el usuario desea eliminar platos.
   1. Si responde "sí", activamos un bucle donde el usuario selecciona los platos que quiere eliminar uno por uno:
      1. Si el plato existe en el pedido, lo eliminamos con .remove() (más adecuado que .pop() para listas de strings).
      1. Actualizamos el precio total eliminado y verificamos que el plato ha sido eliminado.
      1. Si escribe "salir", salimos de ambos bucles.
   1. Si responde "no", simplemente finalizamos el proceso.
1. **Retorno de valores:** Al final, retornamos el total del precio eliminado. Esto es importante porque nos permite actualizar el costo total del pedido restando este valor:

*total\_dinero -= precio\_eliminado*

**5. Resumen del pedido final:**

Tras ejecutar ambas funciones (tomar\_pedido y borrar\_pedidos), mostramos el pedido actualizado junto con el costo total. Esto da al usuario un resumen claro y organizado de su selección final.





**CONCLUSIÓN**

Este proyecto me ha ayudado a trabajar con funciones y estructuras de datos como bibliotecas y listas. Algo que aprendí es cómo devolver múltiples valores usando return y luego asignarlos a variables separadas, lo cual es muy útil para organizar mejor el flujo del código. También descubrí la importancia de manejar cuidadosamente los bucles para evitar errores y hacer el programa más robusto.

Lo que más me gustó fue replicar un sistema tan cotidiano como un pedido en un restaurante, ya que hace que el proyecto tenga un propósito práctico. Siento que cada vez estoy mejorando en cómo estructurar mis programas para que sean más claros y fáciles de entender. Aunque este proyecto fue más complejo, me motivó a aprender más y sentir que estoy avanzando. ¡Ya estoy pensando en cómo puedo mejorarlo o hacerlo más interactivo! 
