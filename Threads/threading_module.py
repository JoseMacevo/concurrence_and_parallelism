import logging
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')


def new_task():
    current_thread = threading.current_thread()
    name = current_thread.name
    ident = threading.get_ident()
    logging.info(f"The current thread is: {current_thread} it's name is {name} and it's id is: {ident}")


if __name__ == '__main__':
    thread_1 = threading.Thread(target=new_task)
    thread_1.start()
    logging.info(f"The live threads are: {threading.enumerate()}")
    for thread in threading.enumerate():
        if thread == threading.main_thread():
            logging.info("We're in the MainThread")
        else:
            logging.info(thread)
