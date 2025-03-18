# CREAR BIBLIOTECA CON PROGRAMACIÓN ORIENTADA A OBJETOS (POO)

**📢 Tienes todos los proyectos de Python bien explicados en mi canal de Youtube:**
 🔗 [@DataAnalystAtares](https://www.youtube.com/@DataAnalystAtares)

## Descripción General

El código implementa un sistema de **Biblioteca** usando **Programación Orientada a Objetos (POO)** en Python. A lo largo del código se explican conceptos clave como **clases, atributos, métodos, herencia y polimorfismo**.

### **Paso 1: Creación de la clase `Libro`**

-   Se define la clase `Libro` con los atributos **título, autor, género y año**.
-   Se usa `__init__` para inicializar los atributos cuando se crea una nueva instancia de `Libro`.
-   Se crea un método `mostrar_informacion()` que imprime los datos del libro.
-   Se crean dos objetos `libro1` y `libro2` con datos específicos.

Aquí se entiende que **cada libro es un objeto** basado en la clase `Libro`.

----------

### **Paso 2: Herencia - Creación de `LibroDigital` y `LibroFisico`**

-   Se crean dos **subclases**:
    -   `LibroDigital` (hereda de `Libro` y añade el atributo `formato`).
    -   `LibroFisico` (hereda de `Libro` y añade el atributo `páginas`).
-   Se usa `super().__init__()` para reutilizar el constructor de la clase base `Libro`.
-   Se sobrescribe el método `mostrar_informacion()` para incluir los nuevos atributos.
-   Se crean dos objetos adicionales: `libro_digital1` y `libro_fisico1`.

Aquí se introduce el concepto de **herencia**, que permite extender las funcionalidades de la clase base sin repetir código.

----------

### **Paso 3: Creación de la clase `Biblioteca`**

-   Se crea la clase `Biblioteca` con una lista vacía de libros.
-   Se implementan métodos para:
    1.  **Agregar libros** (`agregar_libro()`)
    2.  **Eliminar libros** (`eliminar_libro()`)
    3.  **Buscar libros por título** (`buscar_libro()`)
    4.  **Mostrar todos los libros en la biblioteca** (`mostrar_libros()`)

Para agregar libros, la biblioteca recibe objetos `Libro`, lo que permite gestionar tanto libros físicos como digitales de manera uniforme.

----------

### **Paso 4: Uso de la clase `Biblioteca`**

-   Se crea una instancia `mi_biblioteca`.
-   Se agregan varios libros a la biblioteca.
-   Se listan los libros en la biblioteca con `mostrar_libros()`.
-   Se busca un libro por título con `buscar_libro()`, probando tanto un caso que existe como uno que no.

Aquí se ve **cómo una clase (`Biblioteca`) puede trabajar con instancias de otra (`Libro`)**, lo que demuestra la relación entre objetos en POO.

----------

### **Conceptos clave aprendidos en este proyecto**

1.  **Clases y objetos** → `Libro`, `Biblioteca` y sus instancias (`libro1`, `mi_biblioteca`).
2.  **Encapsulación** → Los atributos (`titulo`, `autor`, etc.) están dentro de cada objeto.
3.  **Herencia** → `LibroDigital` y `LibroFisico` heredan de `Libro`.
4.  **Polimorfismo** → `mostrar_informacion()` se sobrescribe en las subclases.
5.  **Métodos y atributos** → Cómo acceder y modificar datos dentro de una clase.
6.  **Interacción entre clases** → `Biblioteca` maneja objetos `Libro`.

Este proyecto sirve como una base sólida para aprender **POO en Python**, aplicando los conceptos fundamentales de una manera práctica y estructurada.
