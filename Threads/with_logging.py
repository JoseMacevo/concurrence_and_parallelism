import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s -> %(threadName)s -> %(message)s')


def worker():
    logging.debug("Launched")
    time.sleep(2)
    logging.debug("Stopped")


if __name__ == '__main__':
    """
    Usando el módulo logging
    Si vamos a depurar o logear algo relacionado con los threads lo mejor es que utilicemos el módulo logging para ello. 
    """
    w = threading.Thread(target=worker, name="Worker")
    w.start()
