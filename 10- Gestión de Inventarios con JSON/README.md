# Sistema de Gestión de Inventario con JSON

## Descripción General

Este programa implementa un sistema de inventario interactivo que permite gestionar productos almacenados en un archivo JSON. Incluye funcionalidades para añadir, modificar y eliminar productos, asegurando que los datos sean persistentes.

## Funcionalidades Principales

### 1. Gestión del Archivo JSON

-   **Creación Automática del Archivo:**
    -   Si el archivo `inventario.json` no existe, se genera automáticamente con una estructura inicial: `{"productos": []}`.
-   **Lectura del Archivo:**
    -   Convierte el contenido del JSON en un diccionario para manipular los datos.
-   **Guardado de Cambios:**
    -   Actualiza el archivo JSON con los datos modificados, asegurando la persistencia de los cambios.

### 2. Mostrar Inventario

-   Lista todos los productos actuales del inventario.
-   Muestra detalles como el nombre, la cantidad y el precio de cada producto en un formato legible.

### 3. Añadir Producto

-   Solicita al usuario los detalles del producto (nombre, cantidad y precio).
-   Valida que el producto no exista ya en el inventario.
-   Agrega el nuevo producto al archivo JSON.

### 4. Modificar Producto

-   Permite al usuario cambiar la cantidad o el precio de un producto existente.
-   Asegura que ni la cantidad ni el precio sean negativos después de los cambios.
-   Guarda los cambios en el archivo JSON.

### 5. Eliminar Producto

-   Permite al usuario eliminar un producto del inventario.
-   Actualiza el archivo JSON eliminando el producto seleccionado.

### 6. Menú Interactivo

-   Ofrece las siguientes opciones:
    -   **Añadir Producto:** Agrega un nuevo producto al inventario.
    -   **Modificar Producto:** Permite cambiar los datos de un producto existente.
    -   **Eliminar Producto:** Elimina un producto del inventario.
    -   **Salir:** Termina la ejecución del programa.

## Flujo de Uso

1.  **Inicio:**
    -   El programa verifica si el archivo JSON existe; si no, lo crea automáticamente.
    -   Muestra el inventario actual (si hay datos).
2.  **Interacción:**
    -   El usuario selecciona una opción del menú.
    -   Según la elección, se ejecuta la función correspondiente.
3.  **Persistencia:**
    -   Los cambios realizados (añadir, modificar, eliminar) se guardan automáticamente en el archivo JSON.
4.  **Finalización:**
    -   El programa se cierra cuando el usuario selecciona la opción de salir.

## Validaciones

-   **Archivo JSON:**
    -   Comprueba la existencia del archivo antes de leer o escribir.
-   **Entradas del Usuario:**
    -   Verifica que la cantidad sea un número entero.
    -   Verifica que el precio sea un número decimal.
    -   Impide que la cantidad o el precio resultantes sean negativos.
-   **Duplicados:**
    -   Previene la adición de productos ya existentes en el inventario.

## Salidas Clave

-   **Mensajes Informativos:**
    -   Indica si una operación se completó con éxito o si ocurrió un error.
-   **Inventario Actualizado:**
    -   Muestra el estado actual del inventario después de cada operación.
-   **Confirmaciones:**
    -   Solicita confirmación para las acciones más críticas, como eliminar un producto.

Este sistema es ideal para pequeñas empresas o proyectos personales que requieran una solución básica de gestión de inventarios con persistencia en JSON.
