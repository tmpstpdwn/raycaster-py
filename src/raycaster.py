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
        self.rays = []
        self.game = game
        self.player = self.game.player
        self.angle_bw = FOV/RAYS
        self.dist_proj_pln = (WINDOW_WIDTH/2)/tan(FOV/2 * (pi/180))

    # Cast rays in player FOV.  
    def cast_all_rays(self):
        self.rays = []
        start_angle = self.player.rotation_angle - FOV/2
        current_angle = self.player.rotation_angle - FOV/2
        while current_angle <= start_angle + FOV:
            angle_rad = current_angle * (pi/180)
            ray_dir = pygame.Vector2(cos(angle_rad), sin(angle_rad))
            ray = Ray(ray_dir, self.game)
            ray.cast()
            self.rays.append(ray)
            current_angle += self.angle_bw

    # Render after casting rays
    def render(self):
        pygame.draw.rect(self.game.screen, 'blue', ((0, 0), (WINDOW_WIDTH, WINDOW_HEIGHT/2)))
        pygame.draw.rect(self.game.screen, 'black', ((0, WINDOW_HEIGHT/2), (WINDOW_WIDTH, WINDOW_HEIGHT/2)))
        for x, ray in enumerate(self.rays):
            if ray.end_dist is None:
                continue
            wall_height = 64 / ray.end_dist * self.dist_proj_pln
            y = WINDOW_HEIGHT / 2 - wall_height / 2
            normalized_dist = ray.end_dist / 800
            brightness_factor = 1 - normalized_dist
            base_color = pygame.Color(210, 199, 152)
            shaded_color = pygame.Color(
                max(0, min(255, int(base_color.r * brightness_factor))),
                max(0, min(255, int(base_color.g * brightness_factor))),
                max(0, min(255, int(base_color.b * brightness_factor)))
            )
            pygame.draw.rect(self.game.screen, shaded_color, ((x * RES, y), (RES, wall_height)))

### END ###

