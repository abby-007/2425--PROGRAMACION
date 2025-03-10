class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una tupla para almacenar el título y el autor, ya que son inmutables
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Libro: {self.titulo_autor[0]} por {self.titulo_autor[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para almacenar los libros prestados al usuario

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario para almacenar libros por ISBN
        self.usuarios_registrados = set()  # Conjunto para almacenar IDs de usuarios únicos
        self.usuarios = {}  # Diccionario para almacenar objetos de usuario por ID

    def añadir_libro(self, libro):
        if libro.isbn in self.libros_disponibles:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' añadido correctamente.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado correctamente.")
        else:
            print(f"El libro con ISBN {isbn} no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios_registrados:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            if self.usuarios[id_usuario].libros_prestados:
                print(f"El usuario con ID {id_usuario} tiene libros prestados y no puede ser eliminado.")
            else:
                self.usuarios_registrados.remove(id_usuario)
                del self.usuarios[id_usuario]
                print(f"Usuario con ID {id_usuario} dado de baja correctamente.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")

    def buscar_libro_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros_disponibles.values() if titulo.lower() in libro.titulo_autor[0].lower()]
        if resultados:
            print(f"Resultados de la búsqueda por título '{titulo}':")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros con el título '{titulo}'.")

    def buscar_libro_por_autor(self, autor):
        resultados = [libro for libro in self.libros_disponibles.values() if autor.lower() in libro.titulo_autor[1].lower()]
        if resultados:
            print(f"Resultados de la búsqueda por autor '{autor}':")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros del autor '{autor}'.")

    def buscar_libro_por_categoria(self, categoria):
        resultados = [libro for libro in self.libros_disponibles.values() if categoria.lower() in libro.categoria.lower()]
        if resultados:
            print(f"Resultados de la búsqueda por categoría '{categoria}':")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros en la categoría '{categoria}'.")

