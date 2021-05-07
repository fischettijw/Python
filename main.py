#  https://www.youtube.com/watch?v=jO6qQDNa2UY
import pygame

LIGHT_GRAY = (231, 231, 231)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Pygame Game")


def draw_window():
    WIN.fill(LIGHT_GRAY)
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
