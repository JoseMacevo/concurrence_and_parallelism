import time
import logging
import threading
import queue

logging.basicConfig(level=logging.DEBUG,
                    format='%(threadName)s: %(message)s')


def show_elements():
    while not queue.empty():
        item = queue.get()
        logging.info(f"The element is: {item}")
        queue.task_done()
        time.sleep(0.5)


if __name__ == '__main__':
    queue = queue.Queue()  # FIFO by default.
    for val in range(20):
        queue.put(val)

    logging.info("This queue already has elements...")

    for _ in range(4):
        threads = threading.Thread(target=show_elements)
        threads.start()
        
