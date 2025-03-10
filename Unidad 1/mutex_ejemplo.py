import threading

contador_global = 0
mutex = threading.Lock()

def incrementar():
    global contador_global
    with mutex:  # Bloquea y libera automáticamente
        contador_global += 1  # Sección crítica

def tarea():
    for _ in range(100000):
        incrementar()

if __name__ == "__main__":
    # Crear los hilos
    hilo1 = threading.Thread(target=tarea)
    hilo2 = threading.Thread(target=tarea)

    # Iniciar los hilos
    hilo1.start()
    hilo2.start()

    # Esperar a que los hilos terminen
    hilo1.join()
    hilo2.join()

    # Mostrar el resultado final
    print("Contador final:", contador_global)
