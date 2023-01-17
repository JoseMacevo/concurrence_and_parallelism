import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG,
                    format='%(processName)s %(message)s')


def get_value(namespace):
    while namespace.easycode is None:
        time.sleep(0.5)
        logging.info("EasyCode doesn't have any value..")
    else:
        logging.info(namespace.easycode)
        logging.info(namespace.new_variable_proof)


def set_value(namespace):
    time.sleep(4)
    namespace.easycode = "Online School.."
    namespace.new_variable_proof = True


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    namespace = manager.Namespace()
    namespace.easycode = None
    process_1 = multiprocessing.Process(target=get_value, args=(namespace,))
    process_2 = multiprocessing.Process(target=set_value, args=(namespace, ))
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()

