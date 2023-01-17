import logging
import threading
from concurrent.futures import Future
import requests

logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')


def show_pokemon_name(response):
    if response.status_code == 200:
        response_json = response.json()
        name = response_json.get('forms')[0].get('name')
        logging.info(f"The pokemon name is: {name}")


def generate_requests(url):
    future = Future()
    thread_1 = threading.Thread(target=(
        lambda: future.set_result(requests.get(url))
    ))
    thread_1.start()
    return future


if __name__ == '__main__':
    future = generate_requests('https://pokeapi.co/api/v2/pokemon/1/')
    future.add_done_callback(
        lambda future:show_pokemon_name(future.result())
    )

    while not future.done():
        logging.info("Waiting for a result")
    else:
        logging.info("The future already has a value...!!")

