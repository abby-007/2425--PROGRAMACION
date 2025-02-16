# Sistema de Gestión de Inventarios
# Este programa permite gestionar productos en una tienda. Podrás añadir, actualizar, eliminar, buscar y mostrar todos los productos disponibles.

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Constructor para crear un producto con su ID, nombre, cantidad y precio
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Representación del producto en formato de texto para que sea más fácil de leer
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        # El inventario contiene una lista de productos, inicialmente vacía
        self.productos = []

    def añadir_producto(self, producto):
        # Verifica si el ID ya existe para evitar duplicados
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("ID ya existente. No se puede añadir.")
        else:
            self.productos.append(producto)
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        # Busca y elimina un producto por su ID
        producto = next((p for p in self.productos if p.id_producto == id_producto), None)
        if producto:
            self.productos.remove(producto)
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualiza la cantidad y/o el precio de un producto por su ID
        producto = next((p for p in self.productos if p.id_producto == id_producto), None)
        if producto:
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Busca productos cuyo nombre contenga la palabra clave ingresada
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            print("Resultados de la búsqueda:")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        # Muestra todos los productos del inventario, o un mensaje si está vacío
        if self.productos:
            print("Inventario actual:")
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")


# Función para mostrar el menú principal
def mostrar_menu():
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


# Crear una instancia del inventario
inventario = Inventario()

# Bucle principal para mostrar el menú y ejecutar las opciones
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # Añadir un nuevo producto
        id_producto = input("ID del producto: ")
        nombre = input("Nombre del producto: ")
        try:
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
        except ValueError:
            print("Error: La cantidad y el precio deben ser valores numéricos.")

    elif opcion == "2":
        # Eliminar un producto por su ID
        id_producto = input("ID del producto a eliminar: ")
        inventario.eliminar_producto(id_producto)

    elif opcion == "3":
        # Actualizar la cantidad o el precio de un producto
        id_producto = input("ID del producto a actualizar: ")
        cantidad = input("Nueva cantidad (deja en blanco para no cambiar): ")
        precio = input("Nuevo precio (deja en blanco para no cambiar): ")
        try:
            inventario.actualizar_producto(
                id_producto,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None,
            )
        except ValueError:
            print("Error: La cantidad y el precio deben ser valores numéricos.")

    elif opcion == "4":
        # Buscar un producto por su nombre
        nombre = input("Nombre del producto a buscar: ")
        inventario.buscar_producto(nombre)

    elif opcion == "5":
        # Mostrar todos los productos
        inventario.mostrar_productos()

    elif opcion == "6":
        # Salir del programa
        print("Saliendo del sistema. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")