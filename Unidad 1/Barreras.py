import threading

# Crear una barrera para 2 hilos
barrera = threading.Barrier(2)

def tarea():
    print("Hilo iniciado")
    barrera.wait()  # Espera a que ambos hilos lleguen aquí
    print("Hilo continuando")

# Crear e iniciar hilos
hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)
hilo1.start()
hilo2.start()

# Esperar a que terminen
hilo1.join()
hilo2.join()

print("Programa terminado")