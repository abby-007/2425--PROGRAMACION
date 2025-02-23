import os

class Producto:
    """
    Clase que representa un producto en el inventario.
    """
    def __init__(self, id_prod, nombre_prod, cant_prod, precio_prod):
        self.id_producto = id_prod
        self.nombre = nombre_prod
        self.cantidad = cant_prod
        self.precio = precio_prod

    def __str__(self):
        """
        Representación en cadena del producto para guardar en archivo.
        """
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    """
    Clase que maneja el inventario de productos, incluyendo la carga y guardado en archivos.
    """
    def __init__(self, archivo_inventario="inventario.txt"):
        self.archivo_inventario = archivo_inventario
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """
        Carga los productos desde el archivo de inventario.
        Si el archivo no existe, lo crea.
        """
        try:
            if not os.path.exists(self.archivo_inventario):
                with open(self.archivo_inventario, "w") as archivo:
                    archivo.write("")  # Crear archivo vacío
                print(f"Archivo '{self.archivo_inventario}' creado.")
            else:
                with open(self.archivo_inventario, "r") as archivo:
                    for linea in archivo:
                        id_prod, nombre, cantidad, precio = linea.strip().split(",")
                        producto = Producto(id_prod, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
                print(f"Inventario cargado desde '{self.archivo_inventario}'.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """
        Guarda los productos en el archivo de inventario.
        """
        try:
            with open(self.archivo_inventario, "w") as archivo:
                for producto in self.productos:
                    archivo.write(f"{producto}\n")
            print(f"Inventario guardado en '{self.archivo_inventario}'.")
        except PermissionError as e:
            print(f"Error al guardar el inventario: {e}")

    def buscar_producto_por_id(self, id_producto):
        """
        Busca un producto por su ID.
        """
        for producto in self.productos:
            if producto.id_producto == id_producto:
                return producto
        return None

    def agregar_producto(self, producto_nuevo):
        """
        Agrega un producto al inventario si no existe otro con el mismo ID.
        """
        if self.buscar_producto_por_id(producto_nuevo.id_producto):
            print("Ya existe un producto con este ID. No se puede agregar nuevamente.")
            return
        self.productos.append(producto_nuevo)
        self.guardar_inventario()
        print(f"Producto '{producto_nuevo.nombre}' agregado con éxito.")

    def eliminar_producto(self, id_a_eliminar):
        """
        Elimina un producto del inventario si se encuentra su ID.
        """
        producto = self.buscar_producto_por_id(id_a_eliminar)
        if producto:
            self.productos.remove(producto)
            self.guardar_inventario()
            print(f"Producto '{producto.nombre}' eliminado correctamente.")
        else:
            print("No encontré un producto con ese ID.")

    def actualizar_producto(self, id_a_actualizar, nueva_cant, nuevo_precio):
        """
        Actualiza la cantidad y el precio de un producto si su ID existe en el inventario.
        """
        producto = self.buscar_producto_por_id(id_a_actualizar)
        if producto:
            producto.cantidad = nueva_cant
            producto.precio = nuevo_precio
            self.guardar_inventario()
            print(f"Producto '{producto.nombre}' actualizado correctamente.")
        else:
            print("No encontré un producto con ese ID.")

    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("\nInventario de Productos:")
        for producto in self.productos:
            print(f"ID: {producto.id_producto} | Nombre: {producto.nombre} | Cantidad: {producto.cantidad} | Precio: ${producto.precio:.2f}")


# --- Interacción con el usuario ---
def menu():
    """
    Muestra el menú de opciones y maneja la interacción con el usuario.
    """
    inventario = Inventario()

    while True:
        print("\nMenú de Inventario:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            id_ingresado = input("Ingresa el ID del producto: ")
            nombre_ingresado = input("Ingresa el nombre del producto: ")
            cantidad_ingresada = int(input("Ingresa la cantidad: "))
            precio_ingresado = float(input("Ingresa el precio: "))
            producto_creado = Producto(id_ingresado, nombre_ingresado, cantidad_ingresada, precio_ingresado)
            inventario.agregar_producto(producto_creado)

        elif opcion == "2":
            id_eliminar = input("Ingresa el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_eliminar)

        elif opcion == "3":
            id_actualizar = input("Ingresa el ID del producto a actualizar: ")
            cantidad_nueva = int(input("Ingresa la nueva cantidad: "))
            precio_nuevo = float(input("Ingresa el nuevo precio: "))
            inventario.actualizar_producto(id_actualizar, cantidad_nueva, precio_nuevo)

        elif opcion == "4":
            inventario.mostrar_inventario()

        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()