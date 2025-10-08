import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
         
    def draw(self, screen):
        pygame.draw.circle(screen, color=pygame.Color("red"), center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            randangle = random.uniform(10, 60)
            rightblock = self.velocity.rotate(randangle)
            leftblock = self.velocity.rotate(-randangle)
            blockradius = self.radius - ASTEROID_MIN_RADIUS
            rightAst = Asteroid(self.position[0], self.position[1], blockradius)
            leftAst = Asteroid(self.position[0], self.position[1], blockradius)
            rightAst.velocity =rightblock *1.2
            leftAst.velocity = leftblock *1.2

