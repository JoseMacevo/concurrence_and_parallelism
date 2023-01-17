import time
import logging
from concurrent.futures import Future

logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')


def callback_future(future):
    logging.info("Hi, I'm a callback that will be executed while the future has no value..!! ")
    logging.info(f"The future is: {future.result()}")


if __name__ == '__main__':
    future = Future()
    future.add_done_callback(callback_future)
    future.add_done_callback(
        lambda future: logging.info("Hi, I'm a lambda function...")
    )
    logging.info("We're starting a complex task")
    time.sleep(2)
    logging.info("Task ending....")
    logging.info("We are going to assign a value to future...")
    future.set_result('EasyCode')
    logging.info('The future already has a value')
