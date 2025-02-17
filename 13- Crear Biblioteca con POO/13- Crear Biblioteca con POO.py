# Paso 1: Introducción a POO: clases, atributos, métodos, __init__ y self

class Libro:
    def __init__(self, titulo, autor, genero, año): 
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año = año

    # Método para mostrar información del libro
    def mostrar_informacion(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Año: {self.año}")

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 1967) 
libro2 = Libro("1984", "George Orwell", "Distopía", 1949)

# Mostrar información de los libros
libro1.mostrar_informacion()
libro2.mostrar_informacion()

# Subclase con herencia para libros digitales
class LibroDigital(Libro): 
    def __init__(self, titulo, autor, genero, año, formato):
        super().__init__(titulo, autor, genero, año) 
        self.formato = formato  # Nuevo atributo exclusivo de libros digitales

    # Sobrescribir método con polimorfismo para mostrar información específica de libros digitales. 
    def mostrar_informacion(self):
        super().mostrar_informacion()  
        print(f"Formato: {self.formato}")

# Subclase para libros físicos
class LibroFisico(Libro):
    def __init__(self, titulo, autor, genero, año, paginas):
        super().__init__(titulo, autor, genero, año)
        self.paginas = paginas  # Nuevo atributo exclusivo de libros físicos

    def mostrar_informacion(self):
        super().mostrar_informacion()  
        print(f"Páginas: {self.paginas}")

# Crear instancias de libros digitales y físicos
libro_digital1 = LibroDigital("El código Da Vinci", "Dan Brown", "Suspenso", 2003, "PDF")
libro_fisico1 = LibroFisico("El señor de los anillos", "J.R.R. Tolkien", "Fantasía", 1954, 1178)

# Ejemplo de método sin self. Si no usamos self, no podremos acceder a los atributos de la clase, ya que cada objeto tiene sus atriburos y métodos y self accede a ellos de manera automática.
class LibroSinSelf:
    def __init__(titulo, autor):  # Error: falta self como primer argumento
        titulo.titulo = titulo  # Esto no funcionará correctamente
        titulo.autor = autor

# Paso 2: Añadimos la clase Biblioteca para gestionar varios libros
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.") 
    
    def eliminar_libro(self, libro): 
        if libro in self.libros: 
            self.libros.remove(libro)
            print(f"Libro '{libro.titulo}' eliminado de la biblioteca.")
        else:
            print("El libro no está en la biblioteca.")

    def buscar_libro(self, titulo):
            for libro in self.libros:
                if libro.titulo.lower() == titulo.lower():
                    print("Libro encontrado:")
                    libro.mostrar_informacion()
                    return 
            print(f"El libro '{titulo}' no se encuentra en la biblioteca.") 

    def mostrar_libros(self):
            if not self.libros:
                print("La biblioteca está vacía.")
            else:
                print("Libros en la biblioteca:")
                for libro in self.libros:
                    libro.mostrar_informacion() 

# Crear una instancia de Biblioteca
mi_biblioteca = Biblioteca()

# Agregar libros a la biblioteca
mi_biblioteca.agregar_libro(libro1) 
mi_biblioteca.agregar_libro(libro2) 
mi_biblioteca.agregar_libro(libro_digital1)
mi_biblioteca.agregar_libro(libro_fisico1)

# Mostrar todos los libros en la biblioteca
mi_biblioteca.mostrar_libros()

#Buscar un libro por título:
mi_biblioteca.buscar_libro("cien años de soledad") 
mi_biblioteca.buscar_libro("ecatombe") #No estará porque no existe
