import os
import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG,
                    format="%(message)s")


def new_process():
    logging.info("Hi, I'm a new process")
    time.sleep(30)
    logging.info("End process")


if __name__ == '__main__':
    process = multiprocessing.Process(target=new_process)
    process.start()

