import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')


def database_connection():
    logging.info("Data base connection started....")
    time.sleep(2)


def web_server_query():
    logging.info("Web server query started....")
    time.sleep(2.5)


if __name__ == '__main__':
    thread_1 = threading.Thread(target=database_connection)
    thread_2 = threading.Thread(target=web_server_query)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    logging.info("Program ended, the threads has ended too....")
