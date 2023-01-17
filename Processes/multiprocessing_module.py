import os
import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')


if __name__ == '__main__':
    current_process = multiprocessing.current_process()
    pid = current_process.pid
    logging.info(f"The current process is: {current_process}, and it's id is: {pid}")

