import time
import logging
from multiprocessing import Pool


logging.basicConfig(level=logging.DEBUG,
                    format='%(processName)s %(message)s')


def is_even(number):
    time.sleep(1)
    return number % 2 == 0


def show_results(results):
    logging.info(f"The result is: {results}")


if __name__ == '__main__':
    with Pool(processes=2) as executor:
        numbers = [number for number in range(1, 10)]

        #  list_result = executor.map(is_even,sunc, iterable)
        #  logging.info(f"The result is: {list_result}")
        #  map_result = executor.map_async(is_even, numbers, callback=show_results)
        #  logging.info("We're going to wait for the results...")
        #  map_result.wait(timeout=1)
        #  logging.info(f"The result is: {map_result.get()}")
        for element in executor.imap_unordered(is_even, numbers):
            logging.info(element)
