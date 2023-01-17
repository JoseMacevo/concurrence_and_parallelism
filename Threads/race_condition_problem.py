import logging
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='%(threadName)s: %(message)s')

BALANCE = 0


def incomes():
    global BALANCE

    for _ in range(0, 100000):
        BALANCE += 1


def withdrawals():
    global BALANCE

    for _ in range(0, 100000):
        BALANCE -= 1


if __name__ == '__main__':
    thread_1 = threading.Thread(target=incomes)
    thread_2 = threading.Thread(target=withdrawals)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    logging.info(f"The final balance is: {BALANCE}")
