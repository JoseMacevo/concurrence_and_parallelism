import requests
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG,
                    format='%(threadName)s: %(message)s')
URLS = [
    'https://codigofacilito.com/',
    'https://twitter.com/home',
    'https://google.com',
    'https://es.stackoverflow.com/',
    'https://stackoverflow.com/',
    'https://about.gitlab.com/',
    'https://github.com',
    'https://www.youtube.com'

]


def generate_request(url):
    return requests.get(url), url


def check_status_code(response):
    logging.info(f"The server response {response[1]} is: {response[0].status_code}")


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(generate_request, url) for url in URLS]
        for future in futures:
            future.add_done_callback(
                lambda future: check_status_code(future.result())
            )
