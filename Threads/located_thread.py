import threading
import time


def worker():
    print(threading.current_thread().name, "-> Launched")
    time.sleep(10)
    print(threading.current_thread().name, "Stopped <-")


def service():
    print(threading.current_thread().name, "Launched")
    print(threading.current_thread().name, "Stopped")


if __name__ == '__main__':
    """
    Saber en que Thread nos encontramos
    Se pueden usar argumentos para nombrar los threads que creamos aunque no es necesario. Cada instancia de la clase
Thread tiene un nombre asigndo por defecto.
    Nombrar los threads puede ser útil por ejemplo, a la hora de clarificar nuestro código. 
    """
    t = threading.Thread(target=service, name='service')
    w = threading.Thread(target=worker, name="worker")
    z = threading.Thread(target=worker)
    w.start()
    z.start()
    t.start()
