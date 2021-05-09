import pygame
import os
import sys

from pygame.constants import QUIT
os.system('cls')


class PyGame:

    def __init__(self, scrn_width, scrn_height, win_caption):
        self.scrn_width = scrn_width
        self.scrn_height = scrn_height
        self.win_caption = win_caption
        pygame.init()
        self.win = pygame.display.set_mode(
            (self.scrn_width, self.scrn_height), pygame.RESIZABLE)
        pygame.display.set_caption(win_caption)

    def caption(self, win_caption):
        self.win_caption = win_caption
        pygame.display.set_caption(win_caption)

    def resize_window(self, scrn_width, scrn_height):
        self.scrn_width = scrn_width
        self.scrn_height = scrn_height
        self.win = pygame.display.set_mode(
            (self.scrn_width, self.scrn_height), pygame.RESIZABLE)

    def events(self):
        # print('quit')
        # print(len(list(pygame.events.get())))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


a = PyGame(600, 400, "My Caption")
pygame.time.delay(1000)

i = 0
while i < 3:
    i += 1
    a.caption('Joseph Fischetti')
    pygame.time.delay(2000)
    a.resize_window(1000, 800)
    print(a.scrn_width, a.scrn_height, a.win_caption)
    pygame.time.delay(2000)
    a.events()

print(i, 'quitquit')
pygame.quit()
sys.exit()
