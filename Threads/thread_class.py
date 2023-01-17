import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='%(threadName)s: %(message)s')


class EasyThread(threading.Thread):
    def __init__(self, name, daemon):
        threading.Thread.__init__(self, name=name, daemon=daemon)

    def run(self) -> None:
        while True:
            logging.info("We put here all tasks to executing concurrently")
            time.sleep(1)


if __name__ == '__main__':
    thread_1 = EasyThread("EasyThread ->", daemon=True)
    thread_1.start()
    time.sleep(3)
    logging.info("Ended program....!!")
