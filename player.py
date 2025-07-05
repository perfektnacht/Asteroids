import pygame

from circleshape import CircleShape
from constants import *
from asteroid import *
from shot import *
from player import *

class Player(CircleShape):
    def __init__ (self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.shotTimer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        pygame.draw.polygon(screen, (255,255,255),self.triangle(),2)

    def rotate(self,dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)
        return self.rotation

    def update(self, dt, shots):
        keys = pygame.key.get_pressed()
        self.shotTimer -= dt

        if keys[pygame.K_a]:
            self.rotate((dt*-1))

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move((dt*-1))

        if self.shotTimer < 0:
            self.shotTimer = 0
        
        if keys[pygame.K_SPACE] and self.shotTimer <=0:
            self.shoot(shots)
            self.shotTimer = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        return self.position

    def shoot(self, shots):
        velocity = pygame.Vector2(0,1)
        velocity = velocity.rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot = Shot(self.position.x,self.position.y,SHOT_RADIUS,velocity)
        shots.append(shot)
        