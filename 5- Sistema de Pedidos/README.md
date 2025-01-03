
# Sistema de Pedidos de Comida

## Descripción General

Este código implementa un sistema interactivo de pedidos de comida. Permite a los usuarios:

1.  Ver el menú con los precios.
2.  Seleccionar y añadir productos al pedido.
3.  Consultar el total acumulado de su pedido.
4.  Eliminar elementos del pedido si lo desean.
5.  Recibir un resumen del pedido final con el total de elementos y precio.

## Funcionalidades Principales

### 1. Mostrar Menú

La función `mostrar_menu(menu)` imprime los platos disponibles junto con sus precios en formato claro y organizado.

-   **Entrada:** Diccionario `menu` con platos como claves y precios como valores.
-   **Salida:** Menú mostrado en la consola.

### 2. Tomar Pedido

La función `tomar_pedido(menu)` permite al usuario:

-   Seleccionar platos del menú ingresándolos por teclado.
    
-   Ver el total acumulado del pedido en tiempo real.
    
-   Salir del proceso de selección escribiendo "salir".
    
-   **Entradas:**
    
    -   El diccionario `menu` para verificar los platos disponibles.
-   **Salidas:**
    
    -   Lista de platos seleccionados (`pedido`).
    -   Total de elementos pedidos (`total_platos`).
    -   Precio total del pedido (`total_precio`).

### 3. Borrar Pedidos

La función `borrar_pedidos(menu)` permite al usuario eliminar platos de su pedido actual.

-   **Proceso:**
    -   Pregunta al usuario si desea eliminar platos.
    -   Si responde "sí", el usuario puede eliminar elementos uno por uno.
    -   Permite salir del modo de eliminación escribiendo "salir".
-   **Entradas:**
    -   Lista de platos seleccionados (`pedido_usuario`).
    -   Diccionario `menu` para verificar precios de los platos eliminados.
-   **Salidas:**
    -   Precio total eliminado (`precio_eliminado`), que se resta del precio final.

### 4. Resumen Final

Después de tomar el pedido y realizar modificaciones, el sistema muestra:

-   Los platos finales seleccionados.
-   El número total de platos.
-   El costo total, ajustado según los platos eliminados.

## Flujo de Uso

1.  Se presenta el menú utilizando `mostrar_menu`.
2.  El usuario selecciona los platos mediante `tomar_pedido`.
3.  Se ofrece la posibilidad de eliminar platos con `borrar_pedidos`.
4.  Se imprime un resumen del pedido final.
