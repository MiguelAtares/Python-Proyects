# Proyecto de Solicitudes Básicas a una API con Python

## Descripción General

Este código tiene como objetivo practicar solicitudes básicas a una **API RESTful** utilizando el módulo `requests` de Python. Implementa los métodos HTTP fundamentales (**GET, POST, PUT, PATCH, DELETE**) para interactuar con la API **JSONPlaceholder**, que es un servicio gratuito de prueba.

## Funcionalidades Principales

### 1. **Obtener Publicaciones (GET)**

La función `get_posts()`:

-   Realiza una solicitud `GET` a la API para obtener todas las publicaciones.
-   Verifica si la solicitud fue exitosa (`status_code == 200`).
-   Imprime los **5 primeros** resultados para evitar sobrecarga de información.

### 2. **Crear una Nueva Publicación (POST)**

La función `create_post()`:

-   Define un nuevo post en formato JSON con los campos `title`, `body` y `userId`.
-   Envía una solicitud `POST` a la API.
-   Verifica que la publicación se haya creado correctamente (`status_code == 201`).
-   Muestra el ID y título del post recién creado.

### 3. **Actualizar una Publicación (PUT)**

La función `update_post(post_id)`:

-   Recibe un ID de publicación para actualizar.
-   Envía una solicitud `PUT` reemplazando completamente el contenido del post.
-   Verifica que la actualización fue exitosa (`status_code == 200`).
-   Muestra los nuevos datos de la publicación.

### 4. **Actualizar Parcialmente una Publicación (PATCH)**

La función `patch_post(post_id)`:

-   Recibe un ID de publicación para modificar.
-   Envía una solicitud `PATCH` para modificar solo el título del post.
-   Verifica que la actualización parcial fue exitosa (`status_code == 200`).
-   Muestra el título actualizado de la publicación.

### 5. **Eliminar una Publicación (DELETE)**

La función `delete_post(post_id)`:

-   Recibe un ID de publicación para eliminar.
-   Envía una solicitud `DELETE` a la API.
-   Verifica si la eliminación fue exitosa (`status_code == 200`).
-   Muestra un mensaje confirmando la eliminación.

## Flujo de Uso

1.  **Se ejecutan las funciones en orden dentro del bloque `if __name__ == "__main__":`**
    -   Se obtiene la lista de publicaciones (`GET`).
    -   Se crea una nueva publicación (`POST`).
    -   Se actualiza completamente una publicación existente (`PUT`).
    -   Se actualiza parcialmente una publicación (`PATCH`).
    -   Se elimina una publicación (`DELETE`).

## Salidas Clave

-   **Mensajes en Consola:** Indican el estado de cada operación (éxito o error).
-   **Publicaciones Obtenidas:** Muestra las primeras 5 publicaciones con su ID y título.
-   **Confirmaciones de Creación/Actualización:** Indican que un post ha sido modificado o añadido con éxito.
-   **Confirmaciones de Eliminación:** Informan cuando un post ha sido eliminado.

## Validaciones y Consideraciones

-   Se valida el código de estado (`status_code`) en cada solicitud antes de procesar la respuesta.
-   Se usa `response.json()` para convertir las respuestas JSON en diccionarios de Python.
-   Se limitan las publicaciones mostradas en `get_posts()` para evitar grandes volúmenes de salida.

Este código es un excelente punto de partida para familiarizarse con **APIs RESTful** en Python y entender cómo funcionan los distintos métodos HTTP.
