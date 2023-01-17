import sys
import time
import pygame
import requests
import threading

pygame.init()

width = 600
height = 600

TEXT = ''


def get_btc_price(url='https://api.bitso.com/v3/ticker/'):
    global TEXT
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            payload = response.json().get('payload')[0]
            price = float(payload.get('last'))
            euros = round(price * 0.043210, 2)
            TEXT = f"The Bitcoin current price is: {euros} Euros"
            time.sleep(1)


thread_1 = threading.Thread(target=get_btc_price, daemon=True)
thread_1.start()


surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Text")

white = (255, 255, 255)
red = (115, 38, 80)
black = (0, 0, 0)

font = pygame.font.SysFont('FiraCode Nerd Font', 24)

while True:
    text = font.render(TEXT, True, black)
    rect = text.get_rect()
    rect.center = (width // 2, height // 2)

    surface.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.blit(text, rect)
    pygame.display.update()
