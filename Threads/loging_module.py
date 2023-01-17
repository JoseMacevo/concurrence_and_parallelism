import logging

'''
Message types and levels:

Debug -> 10
Info -> 20
Warning -> 30
Error -> 40 
Critical -> 50

'''
logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s %(threadName)s',
                    )


def my_messages():
    logging.debug("This is a DEBUG type message ")
    logging.info("This is a INFO type message")
    logging.warning("This is a WARNING type message")
    logging.error("This is an ERROR type message")
    logging.critical("This is a CRITICAL type message")


if __name__ == '__main__':
    my_messages()
