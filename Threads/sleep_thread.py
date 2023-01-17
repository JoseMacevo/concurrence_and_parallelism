import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='(thread)s -> %(threadName)s -> %(message)s')


def task():
    logging.info("We're executing a new task....")
    time.sleep(2)
    logging.info('Finished task')


if __name__ == '__main__':
    """
    El objeto Thread:

        El modo más sencillo para usar un hilo es instanciar un objeto de la clase Thread con una 
    función objetivo y hacer una llamada a su método start().

    """
    thread_1 = threading.Thread(target=task)
    thread_1.start()

