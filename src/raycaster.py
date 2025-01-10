### IMPORTS ###

from settings import *
import pygame
from math import pi, cos, sin, tan
from ray import Ray
from random import choice

### RayCaster CLASS ###

class RayCaster:

    # Init necessary variables.
    def __init__(self, game):
        self.game = game
        self.player = self.game.player
        self.rays = [Ray(self.game) for i in range(RAYS)]

    # Cast rays in player FOV.  
    def cast_all_rays(self):
        current_angle = self.player.rotation_angle - FOV/2
        for ray in self.rays:
            angle_rad = current_angle * (pi/180)
            ray.cast(pygame.Vector2(cos(angle_rad), sin(angle_rad)))
            if ray.end_dist:
                beta = angle_rad - (self.player.rotation_angle * (pi/180))
                ray.end_dist = ray.end_dist * cos(beta)
            current_angle += ANGLE_BW

    # Render after casting rays
    def render(self):
        pygame.draw.rect(self.game.screen, 'blue', ((0, 0), (WINDOW_WIDTH, WINDOW_HEIGHT/2)))
        pygame.draw.rect(self.game.screen, 'black', ((0, WINDOW_HEIGHT/2), (WINDOW_WIDTH, WINDOW_HEIGHT/2)))
        for x, ray in enumerate(self.rays):
            if ray.end_dist is None:
                continue
            wall_height = DIST_CONST / ray.end_dist
            y = (WINDOW_HEIGHT / 2) - (wall_height / 2)
            normalized_dist = ray.end_dist / 800
            brightness_factor = 1 - normalized_dist
            base_color = pygame.Color(210, 199, 152)
            shaded_color = pygame.Color(
                max(0, min(255, int(base_color.r * brightness_factor))),
                max(0, min(255, int(base_color.g * brightness_factor))),
                max(0, min(255, int(base_color.b * brightness_factor)))
            )
            pygame.draw.rect(self.game.screen, shaded_color, ((x * RES, y), (RES, wall_height)))
            ray.end_dist = None

### END ###

