import pygame
from constants import *
from player import Player # pyright: ignore

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable) 
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=pygame.Color("black"))

        for sprite in drawable:
           sprite.draw(screen)

        updateable.update(dt)
        dt = clock.tick(60) / 1000
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
