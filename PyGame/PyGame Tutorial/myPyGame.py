import pygame
import copy

PG_Rect = copy.copy(pygame.draw.rect)
# win = PG_DplyMode((scrn_width, scrn_height))
PG_DplyMode = copy.copy(pygame.display.set_mode)
PG_Init = copy.copy(pygame.init)
PG_Caption = copy.copy(pygame.display.set_caption)
PG_Delay = copy.copy(pygame.time.delay)
PG_KeyPressed = copy.copy(pygame.key.get_pressed)
PG_GetEvents = copy.copy(pygame.event.get)
PG_K_LEFT = pygame.K_LEFT
PG_K_RIGHT = pygame.K_RIGHT
PG_K_UP = pygame.K_UP
PG_K_DOWN = pygame.K_DOWN
PG_K_SPACE = pygame.K_SPACE
PG_DplyUpdate = pygame.display.update
PG_ImgLoad = pygame.image.load
PG_Quit = pygame.QUIT
