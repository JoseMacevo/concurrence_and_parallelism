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
    return requests.get(url)


def check_status_code(response, url):
    logging.info(f"The server response {url} is {response.status_code}")


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        results = executor.map(generate_request, URLS)
        for url, response in zip(URLS, results):
            if response.status_code == 200:
                check_status_code(response, url)

