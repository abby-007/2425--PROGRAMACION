class Producto:
    """
    Esta clase representa un producto en el sistema de inventario.
    """

    def __init__(self, id_prod, nombre_prod, cant_prod, precio_prod):
        """
        Al crear un producto, le asigno un ID, un nombre, una cantidad y un precio.
        """
        self.id_producto = id_prod
        self.nombre = nombre_prod
        self.cantidad = cant_prod
        self.precio = precio_prod


class Inventario:
    """
    Esta clase maneja el inventario de productos.
    Permite agregar, eliminar, actualizar y ver productos.
    """

    def __init__(self):
        """
        Cuando inicio el inventario, está vacío.
        """
        self.productos = []

    def agregar_producto(self, producto_nuevo):
        """
        Agrego un producto nuevo, pero antes reviso si su ID ya está en el inventario.
        """
        for producto in self.productos:
            if producto.id_producto == producto_nuevo.id_producto:
                print("Ya existe un producto con este ID. No se puede agregar nuevamente.")
                return
        self.productos.append(producto_nuevo)
        print(f"Producto '{producto_nuevo.nombre}' agregado con éxito.")

    def eliminar_producto(self, id_a_eliminar):
        """
        Elimino un producto si encuentro su ID en el inventario.
        """
        for producto in self.productos:
            if producto.id_producto == id_a_eliminar:
                self.productos.remove(producto)
                print(f"Producto '{producto.nombre}' eliminado correctamente.")
                return
        print("No encontré un producto con ese ID.")

    def actualizar_producto(self, id_a_actualizar, nueva_cant, nuevo_precio):
        """
        Actualizo la cantidad y el precio de un producto si su ID existe en el inventario.
        """
        for producto in self.productos:
            if producto.id_producto == id_a_actualizar:
                producto.cantidad = nueva_cant
                producto.precio = nuevo_precio
                print(f"Producto '{producto.nombre}' actualizado correctamente.")
                return
        print("No encontré un producto con ese ID.")

    def mostrar_inventario(self):
        """
        Muestro todos los productos que están en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("\nInventario de Productos:")
        for producto in self.productos:
            print(f"ID: {producto.id_producto} | Nombre: {producto.nombre} | Cantidad: {producto.cantidad} | Precio: ${producto.precio:.2f}")


# --- Interacción con el usuario ---
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

