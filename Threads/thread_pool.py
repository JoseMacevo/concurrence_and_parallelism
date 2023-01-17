import time
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG,
                    format='%(threadName)s: %(message)s')


def math_operation(number_1, number_2):
    time.sleep(1)
    result = number_1 + number_2
    logging.info(f"{number_1} + {number_2} = {result}")


if __name__ == '__main__':
      executor = ThreadPoolExecutor(max_workers=3, thread_name_prefix='jositos')
      executor.submit(math_operation, 10, 20)
      executor.submit(math_operation, 40, 50)
      executor.submit(math_operation, 60, 32)
      executor.submit(math_operation, 60, 200)

      
