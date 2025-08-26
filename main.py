import pygame
from constants import * # pyright: ignore

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=pygame.Color("black"))
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
