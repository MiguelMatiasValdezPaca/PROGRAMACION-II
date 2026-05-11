class Biblioteca:

    class Horario:
        def __init__(self, dias, hora_apertura, hora_cierre):
            self.dias = dias
            self.hora_apertura = hora_apertura
            self.hora_cierre = hora_cierre

        def mostrar_horario(self):
            print(f"Horario: {self.dias} de {self.hora_apertura} a {self.hora_cierre}")

    def __init__(self, nombre, dias, apertura, cierre):
        self.nombre = nombre
        self.libros = []      
        self.autores = []     
        self.prestamos = []
        self.horario = Biblioteca.Horario(dias, apertura, cierre)

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_autor(self, autor):
        self.autores.append(autor)

    def prestar_libro(self, estudiante, libro):
        prestamo = Prestamo(estudiante, libro)  
        self.prestamos.append(prestamo)

    def mostrar_estado(self):
        print(f"\n=== Biblioteca: {self.nombre} ===")
        self.horario.mostrar_horario()

        print("\nLibros:")
        for l in self.libros:
            print("-", l.titulo)

        print("\nAutores:")
        for a in self.autores:
            a.mostrar_info()

        print("\nPréstamos:")
        for p in self.prestamos:
            p.mostrar_info()

    def cerrar_biblioteca(self):
        print("\nLa biblioteca está cerrada.")
        self.prestamos.clear()

class Libro:

    class Pagina:
        def __init__(self, numero, contenido):
            self.numero = numero
            self.contenido = contenido

        def mostrar_pagina(self):
            print(f"Página {self.numero}: {self.contenido}")

    def __init__(self, titulo, isbn, contenidos):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = []

        for i, texto in enumerate(contenidos):
            self.paginas.append(Libro.Pagina(i + 1, texto))

    def leer(self):
        for p in self.paginas:
            p.mostrar_pagina()

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrar_info(self):
        print(f"Autor: {self.nombre} ({self.nacionalidad})")

class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrar_info(self):
        print(f"Estudiante: {self.nombre} - Código: {self.codigo}")

class Prestamo:
    def __init__(self, estudiante, libro):
        self.estudiante = estudiante
        self.libro = libro
        self.fecha_prestamo = "05/05/2026"
        self.fecha_devolucion = "12/05/2026"

    def mostrar_info(self):
        print(f"Préstamo: {self.libro.titulo}")
        self.estudiante.mostrar_info()
        print(f"Desde: {self.fecha_prestamo} hasta: {self.fecha_devolucion}")


# Crear biblioteca
b = Biblioteca("UMSA", "Lunes a Viernes", "08:00", "18:00")

# Crear autores
a1 = Autor("Gabriel García Márquez", "Colombia")
a2 = Autor("Mario Vargas Llosa", "Perú")

b.agregar_autor(a1)
b.agregar_autor(a2)

# Crear libros
l1 = Libro("Cien años de soledad", "123", ["Inicio", "Desarrollo", "Final"])
l2 = Libro("La ciudad y los perros", "456", ["Cap1", "Cap2"])

b.agregar_libro(l1)
b.agregar_libro(l2)

# Crear estudiante
e1 = Estudiante("2025", "Miguel")

# Préstamo
b.prestar_libro(e1, l1)

# Mostrar estado
b.mostrar_estado()

# Leer libro
print("\nLeyendo libro:")
l1.leer()

# Cerrar biblioteca
b.cerrar_biblioteca()