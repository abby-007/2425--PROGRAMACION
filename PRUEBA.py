def mostrar_menu():
    while True:
        print("\n📌 MENÚ DE PRUEBA")
        print("1 ➜ Mostrar mensaje")
        print("2 ➜ Mostrar otro mensaje")
        print("0 ➜ Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("✅ Elegiste la opción 1: ¡Hola, este es un mensaje de prueba!")
        elif opcion == "2":
            print("🔹 Elegiste la opción 2: Otro mensaje de prueba aquí.")
        elif opcion == "0":
            print("👋 Saliendo del programa...")
            break
        else:
            print("⚠️ Opción no válida, intenta de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    mostrar_menu()
