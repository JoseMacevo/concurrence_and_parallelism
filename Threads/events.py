import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='%(threadName)s: %(message)s')


def thread_1(event):
    logging.info("Hi, I'm wating the signal...")
    event.wait()
    logging.info("The signal was given, the signal is True")


def thread_2(event):
    while not event.is_set():
        logging.info("Waiting for the signal....")
        time.sleep(0.5)


if __name__ == '__main__':
    event = threading.Event()
    thread1 = threading.Thread(target=thread_1, args=(event, ))
    thread2 = threading.Thread(target=thread_2, args=(event, ))
    thread1.start()
    thread2.start()
    time.sleep(3)
    event.set()
    event.clear()

