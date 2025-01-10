### IMPORTS ###

from settings import SPEED, ROTATION_SPEED
import pygame
from math import pi, sin, cos
from random import randint

### Player CLASS ###

class Player:

    # Init necessary variables.
    def __init__(self, pos, game):
        self.game = game
        self.rect = pygame.Rect(pos, (10, 10))
        self.speed = SPEED
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
            self.movement('front', dt)
        elif keys[pygame.K_DOWN]:
            self.movement('back', dt)

    # Set the player in motion based on its updated direction.
    def movement(self, dir_of_move, dt):
        if dir_of_move == "back":
            direction = self.direction.copy() * -1
        else:
            direction = self.direction

        if direction.x < 0:
            next_x = self.rect.x + direction.x * self.speed * dt
        else:
            next_x = self.rect.right + direction.x * self.speed * dt

        if direction.y < 0:
            next_y = self.rect.y + direction.y * self.speed * dt
        else:
            next_y = self.rect.bottom + direction.y * self.speed * dt

        if not self.game.map.has_wall((next_x, self.rect.y)):
            self.rect.x += direction.x * self.speed * dt

        if not self.game.map.has_wall((self.rect.x, next_y)):
            self.rect.y += direction.y * self.speed * dt

    # Update the player.
    def update(self, dt):
        self.input(dt)

### END ###
