import logging
import threading
import requests

logging.basicConfig(level=logging.DEBUG,
                    format='%(threadName)s %(message)s')


def get_random_user(response_json):
    random_name = response_json.get('results')[0].get('name').get('first')
    logging.info(f"The name of the user is: {random_name}")


def get_pokemon_name(response_json):
    name = response_json.get('forms')[0].get('name')
    logging.info(f"The pokemon name is; {name}")


def error():
    logging.error("Isn't possible complete this operation......")


def generate_requests(url, success_callback, error_callback):
    response = requests.get(url)
    if response.status_code == 200:
        success_callback(response.json())
    else:
        error_callback()


if __name__ == '__main__':
    thread_1 = threading.Thread(target=generate_requests, kwargs={
        'url': 'https://pokeapi.co/api/v2/pokemon/1/',
        'success_callback': get_pokemon_name,
        'error_callback': error

    })

    thread_2 = threading.Thread(target=generate_requests, kwargs={
        'url': 'https://randomuser.me/api',
        'success_callback': get_random_user,
        'error_callback': error
    })
    thread_1.start()
    thread_2.start()
