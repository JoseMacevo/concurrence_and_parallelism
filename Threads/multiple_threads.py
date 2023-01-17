import threading


def executor_a(id=0):
    for x in range(0, 10):
        print(f"Hi, I'm the Thread {id}, iteration: {x}")


def executor_b(id=0):
    for x in range(0, 10):
        print(f"Hi, I'm the Thread {id}, iteration: {x}")


def executor_c(id=0):
    for x in range(0, 10):
        print(f"Hi, I'm the Thread {id}, iteration: {x}")


if __name__ == '__main__':
    thread_1 = threading.Thread(target=executor_a, args=[1])  # Paso de argumentos en forma de lista
    thread_2 = threading.Thread(target=executor_b, args=(2, ))  # Paso de argumentos en forma de tupla
    thread_3 = threading.Thread(target=executor_c, kwargs={'id': 3})  # Paso de argumentos en forma de diccionario
    thread_1.start()
    thread_2.start()
    thread_3.start()
