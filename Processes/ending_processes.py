import os
import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')

def son_process():
    logging.info('Hi, from a son process')
    time.sleep(2)
    logging.info('Son process ending...')


if __name__ == '__main__':
    process = multiprocessing.Process(target=son_process)
    process.start()
    time.sleep(5)
    if process.is_alive():
        process.terminate()
        logging.info("Son Process finished early...!")
    logging.info("Ending Program")

