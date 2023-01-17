import logging
import threading
import requests

logging.basicConfig(level=logging.DEBUG,
                    format='%(threadName)s: %(message)s')

user = dict()


def generate_request(url, event):
    global user
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        user = response_json.get('results')[0]
        event.set()


def show_user_name(event):
    event.wait()
    name = user.get('name').get('first')
    logging.info(f"The user name is: {name}")


if __name__ == '__main__':
    event = threading.Event()
    thread_1 = threading.Thread(target=generate_request, args=("https://randomuser.me/api/", event))
    thread_2 = threading.Thread(target=show_user_name, args=(event, ))
    thread_1.start()
    thread_2.start()
