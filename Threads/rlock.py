import logging
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='%(threadName)s: %(message)s')


BALANCE = 100

lock = threading.RLock()


if __name__ == '__main__':
    lock.acquire()
    lock.acquire()
    BALANCE -= 10
    lock.release()
    lock.release()
    logging.info(f"The final balance is: {BALANCE}")


    