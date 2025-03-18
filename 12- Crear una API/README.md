# API de Star Wars con Flask

**📢 Tienes todos los proyectos de Python bien explicados en mi canal de Youtube:**
 🔗 [@DataAnalystAtares](https://www.youtube.com/@DataAnalystAtares)

## Descripción General

Este proyecto implementa una API RESTful con Flask para gestionar información sobre personajes de Star Wars. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre una lista de personajes, además de filtrar resultados y gestionar errores.

## Funcionalidades Principales

1.  **Estructura del Proyecto**
    
    -   Flask se usa para definir la API y manejar las rutas.
    -   Los datos se envían y reciben en formato JSON.
    -   Se definen rutas para acceder, modificar y eliminar personajes.
2.  **Rutas Disponibles**
    
    -   Ruta Base:
        
        -   "/" (GET): Devuelve un mensaje de bienvenida.
    -   Obtener Personajes:
        
        -   "/characters" (GET): Devuelve todos los personajes en formato JSON.
        -   "/characters?species=<especie>" (GET): Filtra personajes por especie.
        -   "/characters/int:id" (GET): Obtiene un personaje por su ID.
    -   Añadir un Nuevo Personaje:
        
        -   "/characters" (POST): Permite añadir un nuevo personaje a la lista.
    -   Actualizar un Personaje:
        
        -   "/characters/update/int:id" (PUT): Actualiza completamente un personaje.
        -   "/characters/update/int:id" (PATCH): Modifica solo los campos enviados en la solicitud.
    -   Eliminar un Personaje:
        
        -   "/characters/delete/int:id" (DELETE): Elimina un personaje de la lista.

## Detalles Técnicos

1.  **Estructura de un Personaje**

Cada personaje tiene los siguientes atributos:

-   id: Identificador único del personaje.
-   name: Nombre del personaje.
-   species: Especie del personaje.

Ejemplo de un personaje en formato JSON:

{ "id": 1, "name": "Luke Skywalker", "species": "Human" }

2.  **Manejo de Errores**

La API incluye validaciones y mensajes de error en JSON:

-   400 → Falta un campo obligatorio.
-   404 → Personaje no encontrado.
-   409 → Conflicto (Ejemplo: ID duplicado).
-   500 → Error interno inesperado.

3.  **Ejemplo de Solicitudes**

Para obtener la lista de personajes (GET):

curl -X GET [http://127.0.0.1:5000/characters](http://127.0.0.1:5000/characters)

Para añadir un personaje nuevo (POST):

curl -X POST [http://127.0.0.1:5000/characters](http://127.0.0.1:5000/characters) -H "Content-Type: application/json" -d '{"id": 4, "name": "Obi-Wan Kenobi", "species": "Human"}'

Para eliminar un personaje por ID (DELETE):

curl -X DELETE http://127.0.0.1:5000/characters/delete/1

## Cómo Ejecutar la API

1.  Instalar Flask con el siguiente comando:

pip install flask

2.  Ejecutar el servidor con el siguiente comando:

python nombre_del_archivo.py

3.  Acceder a la API en la siguiente dirección:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)



## Conclusión

Esta API es una excelente introducción al desarrollo de APIs REST con Flask, permitiendo practicar el uso de métodos HTTP y el manejo de datos en JSON.
