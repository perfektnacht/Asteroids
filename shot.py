import pygame

from constants import *
from circleshape import *
from shot import *

class Shot(CircleShape):

    def __init__ (self, x, y, radius, velocity):
        super().__init__(x,y,radius)
        self.radius = SHOT_RADIUS
        self.velocity = velocity
        self.position_x = x
        self.position_y = y

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 0)

    def collision(self, asteroid):
        distance = pygame.math.Vector2.distance_to(self.position,asteroid.position)
        check_distance = self.position + asteroid.position

        if distance <= self.radius + asteroid.radius:
            return True
        else:
            return False