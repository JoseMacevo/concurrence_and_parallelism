import os
import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG,
                    format="%(process)s %(processName)s %(message)s")


def new_process(message):
    logging.info("Hi, I'm a new process")
    time.sleep(3)
    logging.info(message)
    logging.info("End process")


if __name__ == '__main__':
    process = multiprocessing.Process(target=new_process, name="Son Process ->",
                                      args=("New Process from an argument", ), daemon=True)
    process.start()
    logging.info("Hi, from a Main Process")
