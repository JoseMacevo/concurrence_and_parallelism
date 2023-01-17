import requests
import logging
from concurrent.futures import as_completed
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


def check_status_code(response, url):
    logging.info(f"The server response {url} is {response.status_code}")


def math_operation(number_1, number_2):
    return number_1 + number_2


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(generate_request, url) for url in URLS]

        for future in as_completed(futures):
            response, url = future.result()

            if response.status_code == 200:
                check_status_code(response, url)


