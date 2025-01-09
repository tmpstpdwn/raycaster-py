### IMPORTS ###

from settings import *
import pygame
from math import tan, atan2

### Ray CLASS ###

class Ray:

    # Init necessary variables.
    def __init__(self, direction, game):
        self.game = game
        self.player = self.game.player
        self.direction = direction
        self.end_dist = None

    # Check for horizontal intersection with the wall.
    def horizontal_intersection(self, alpha):
        if self.direction.y < 0:
            ya = -TILE_SIZE
            a_y = (self.player.rect.y//TILE_SIZE) * TILE_SIZE - 1
        elif self.direction.y > 0:
            ya = TILE_SIZE
            a_y = (self.player.rect.y//TILE_SIZE) * TILE_SIZE + TILE_SIZE
        else:
            return None

        xa = ya/tan(alpha)
        a_x = (a_y - self.player.rect.centery)/tan(alpha) + self.player.rect.centerx

        for i in range(20):
            if self.game.map.has_wall((a_x, a_y)):
                return a_x, a_y
            a_x += xa
            a_y += ya

        return None

    # Check for vertical intersection with the wall.
    def vertical_intersection(self, alpha):
        if self.direction.x < 0:
            xa = -TILE_SIZE
            b_x = (self.player.rect.x//TILE_SIZE) * TILE_SIZE - 1
        elif self.direction.x > 0:
            xa = TILE_SIZE
            b_x = (self.player.rect.x//TILE_SIZE) * TILE_SIZE + TILE_SIZE
        else:
            return None

        ya = xa * tan(alpha)
        b_y = self.player.rect.centery + (b_x - self.player.rect.centerx) * tan(alpha)

        for i in range(20):
            if self.game.map.has_wall((b_x, b_y)):
                return b_x, b_y
            b_x += xa
            b_y += ya

        return None

    # Compare vertical, horizontal intersection distances and return the smaller one.
    def intersection(self, alpha):
        horizontal_intersection = self.horizontal_intersection(alpha)
        vertical_intersection = self.vertical_intersection(alpha)
        player_center = self.player.rect.center
        if horizontal_intersection is None and vertical_intersection is None:
            return None
        if horizontal_intersection:
            hor_dist = (pygame.Vector2(horizontal_intersection) - pygame.Vector2(player_center)).magnitude()
        else:
            hor_dist = float('inf')
        if vertical_intersection:
            ver_dist = (pygame.Vector2(vertical_intersection) - pygame.Vector2(player_center)).magnitude()
        else:
            ver_dist = float('inf')
        if hor_dist < ver_dist:
            return horizontal_intersection, hor_dist
        else:
            return vertical_intersection, ver_dist

    # Cast a ray.
    def cast(self):
        alpha = atan2(self.direction.y, self.direction.x)
        intersection_data = self.intersection(alpha)
        if intersection_data is not None:
            self.end_point, self.end_dist = intersection_data

    # Render a ray after casting.
    def render(self):
        if self.end_point:
            pygame.draw.line(self.game.screen, 'green', self.player.rect.center, self.end_point)

### END ###
