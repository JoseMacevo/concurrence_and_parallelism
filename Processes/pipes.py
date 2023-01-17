import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG,
                    format='%(processName)s %(message)s')


class Publisher(multiprocessing.Process):
    def __init__(self, connection):
        self.connection = connection
        multiprocessing.Process.__init__(self)

    def run(self):
        logging.info("Hi, We're in the Publisher Process")
        for x in range(20):
            self.connection.send(f'Hi, from publisher method with the {x} value. ')
            time.sleep(0.5)
        self.connection.send(None)
        self.connection.close()
        logging.info("Closed connection for Publisher")


class Subscriber(multiprocessing.Process):
    def __init__(self, connection):
        self.is_alive = True
        self.connection = connection
        multiprocessing.Process.__init__(self)

    def run(self):
        logging.info("Hi, We're in the Subscriber Process")
        while self.is_alive:
            result = self.connection.recv()
            self.is_alive = result is not None
            logging.info(result)
        else:
            self.connection.close()
            logging.info("Closed connection for Subscriber")


if __name__ == '__main__':
    connection_1, connection_2 = multiprocessing.Pipe()
    publisher = Publisher(connection_1)
    subscriber = Subscriber(connection_2)
    publisher.start()
    subscriber.start()

