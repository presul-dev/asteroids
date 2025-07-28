from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt