### IMPORTS ###

from settings import*
import pygame
from math import pi, sin, cos
from random import randint

### Player CLASS ###

class Player:

    # Init necessary variables.
    def __init__(self, pos, game):
        self.game = game
        self.image = pygame.Surface((10, 10))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 300
        self.rotation_angle = randint(0, 360)
        self.direction = pygame.math.Vector2(0, 0)

    # Get input and set direction.
    def input(self, dt):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rotation_angle += ROTATION_SPEED * dt
        elif keys[pygame.K_LEFT]:
            self.rotation_angle -= ROTATION_SPEED * dt

        self.rotation_angle %= 360
        angle_rad = self.rotation_angle * (pi/180)
        self.direction.update(cos(angle_rad), sin(angle_rad))

        if keys[pygame.K_UP]:
            self.movement(dt)

    # Set the player in motion based on its updated direction.
    def movement(self, dt):
        if self.direction.x < 0:
            next_x = self.rect.x + self.direction.x * self.speed * dt
        else:
            next_x = self.rect.right + self.direction.x * self.speed * dt

        if self.direction.y < 0:
            next_y = self.rect.y + self.direction.y * self.speed * dt
        else:
            next_y = self.rect.bottom + self.direction.y * self.speed * dt

        if not self.game.map.has_wall((next_x, self.rect.y)):
            self.rect.x += self.direction.x * self.speed * dt

        if not self.game.map.has_wall((self.rect.x, next_y)):
            self.rect.y += self.direction.y * self.speed * dt

    # Update the player.
    def update(self, dt):
        self.input(dt)

### END ###
