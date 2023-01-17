import logging
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')


def callback():
    logging.info("Hi, I'm a callback that doesn't run immediately")


if __name__ == '__main__':
    thread = threading.Timer(3, callback)
    thread.start()
    logging.info("Hi, I'm the main thread.")
    logging.info("We're waiting for the execution of the callback")


