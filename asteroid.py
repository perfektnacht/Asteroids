import pygame
import random

from constants import *
from circleshape import *
from asteroidfield import *

class Asteroid(CircleShape):

    def __init__ (self, x, y, radius, field):
        super().__init__(x,y,radius)
        self.field = field

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            randomAngle = random.uniform(20,50)
            new_velocity1 = self.velocity.rotate(randomAngle) * 1.2
            new_velocity2 = self.velocity.rotate(-randomAngle) * 1.2
            self.field.spawn(new_radius, self.position, new_velocity1)
            self.field.spawn(new_radius, self.position, new_velocity2)