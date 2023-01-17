import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')


def thread():
    logging.info("Hi, I'm a normal thread")
    time.sleep(2)
    logging.info("The program ended when I ended...")


def daemon_thread():
    while True:
        logging.info("We're executing in the background...")
        time.sleep(0.5)


if __name__ == '__main__':
    thread_1 = threading.Thread(target=daemon_thread, daemon=True)
    thread_1.start()
    input("Press a key to finished the main thread")
