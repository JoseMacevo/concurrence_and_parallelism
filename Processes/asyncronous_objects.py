import time
import logging
from multiprocessing import Pool

logging.basicConfig(level=logging.DEBUG,
                    format='%(processName)s %(message)s')


def is_even(number):
    time.sleep(5)
    return number % 2 == 0


if __name__ == '__main__':
    with Pool(processes=2) as executor:
        apply_result = executor.apply_async(is_even, args=(10, ))
        logging.info("We're waiting until apply_result has a value")
        apply_result.wait(timeout=2)
        logging.info("apply_result has finished")
        logging.info(f"The result is: {apply_result.get(timeout=1)}")
        logging.info("Ending program")
