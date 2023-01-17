import time
import queue
import random
import logging
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='%(threadName)s: %(message)s')


""" 
Producer and consumer problem.
The program describe two processes, producer and consumer, both of them
are sharing a finite size buffer.
The task of the producer is generate an item, store it, and restart again,
wile the consumer give (simultaneously), items one by one.
The problem is that the producer doesn't add more items, that the buffer capacity
and the consumer doesn't try take an item if the buffer is empty.
"""

queue = queue.Queue(maxsize=10)

def producer():
    while True:
        if not queue.full():
            item = random.randint(1,10)
            queue.put(item)
            logging.info(f"New element {item} inside que queue.")
            time_to_sleep = random.randint(1, 3)
            time.sleep(time_to_sleep)


def consumer():
    while True:
        if not queue.empty():
            item = queue.get()
            queue.task_done()
            logging.info(f"New element {item} has been obtained...")
            time_to_sleep = random.randint(1, 3)
            time.sleep(time_to_sleep)




if __name__ == '__main__':
    thread_producer = threading.Thread(target=producer)
    thread_consumer = threading.Thread(target=consumer)
    thread_producer.start()
    thread_consumer.start()


