import pickle  # Importo el módulo pickle para serializar y deserializar datos

# Defino la clase Producto para representar un producto en el inventario
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        # Inicializo los atributos del producto
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Defino cómo se representa el producto como cadena de texto
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def actualizar_cantidad(self, nueva_cantidad):
        # Método para actualizar la cantidad del producto
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        # Método para actualizar el precio del producto
        self.precio = nuevo_precio


# Defino la clase Inventario para gestionar una colección de productos
class Inventario:
    def __init__(self):
        # Uso un diccionario para almacenar los productos, donde la clave es el ID
        self.productos = {}

    def agregar_producto(self, producto):
        # Método para agregar un producto al inventario
        if producto.id in self.productos:
            print("Error: Ya existe un producto con este ID.")
        else:
            self.productos[producto.id] = producto
            print(f"Producto '{producto.nombre}' agregado correctamente.")

    def eliminar_producto(self, id):
        # Método para eliminar un producto por su ID
        if id in self.productos:
            del self.productos[id]
            print(f"Producto con ID {id} eliminado correctamente.")
        else:
            print("Error: No existe un producto con este ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        # Método para actualizar la cantidad o el precio de un producto
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.actualizar_cantidad(cantidad)
            if precio is not None:
                producto.actualizar_precio(precio)
            print(f"Producto con ID {id} actualizado correctamente.")
        else:
            print("Error: No existe un producto con este ID.")

    def buscar_por_nombre(self, nombre):
        # Método para buscar productos por nombre (búsqueda parcial e insensible a mayúsculas)
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if resultados:
            print("Resultados de la búsqueda:")
            for producto in resultados:
                print(producto)
        else
