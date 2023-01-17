import os
import time
import logging
import multiprocessing


logging.basicConfig(level=logging.DEBUG,
                    format='%(process)s %(processName)s %(message)s')


def new_process(message):
    logging.info("Hi, I'm a new process")
    time.sleep(5)
    logging.info(message)
    logging.info("End process")


if __name__ == '__main__':
    process = multiprocessing.Process(target=new_process, name='Son process -> ',
                                      args=("Hi, a message from an argument", ))
    process.start()
    process.join()
    logging.info("Hi, from a main process")



