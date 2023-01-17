import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG,
                    format="%(process)s %(processName)s  %(message)s")


def new_process():
    logging.info("Hi, I'm a new process")
    time.sleep(5)
    logging.info("End Process")


if __name__ == '__main__':
    process = multiprocessing.Process(target=new_process, name='Son Process ->')
    process.start()
    logging.info("Hi, from a main process")



    
    
