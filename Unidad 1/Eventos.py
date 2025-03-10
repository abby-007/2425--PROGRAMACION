import threading
import time
evento = threading.Event()

def esperar_evento():
    print("Esperando al evento...")
    evento.wait()  # Bloqueo hasta activación
    print("Evento activado!")

def activar_evento():
    print("Esperando 5 segundos...")
    time.sleep(5)
    evento.set()    # Envía señal
    print("Evento activado")

hilo1 = threading.Thread(target=esperar_evento)
hilo2 = threading.Thread(target=activar_evento)
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()
print("Programa terminado")  