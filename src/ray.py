### IMPORTS ###

from settings import TILE_SIZE
import pygame
from math import tan, atan2

### Ray CLASS ###

class Ray:

    # Init necessary variables.
    def __init__(self, game):
        self.game = game
        self.player = self.game.player
        self.end_dist = None

    # Check for horizontal intersection with the wall.
    def horizontal_intersection(self, alpha, direction):
        if direction.y < 0:
            ya = -TILE_SIZE
            a_y = (self.player.rect.y//TILE_SIZE) * TILE_SIZE - 1
        elif direction.y > 0:
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
    def vertical_intersection(self, alpha, direction):
        if direction.x < 0:
            xa = -TILE_SIZE
            b_x = (self.player.rect.x//TILE_SIZE) * TILE_SIZE - 1
        elif direction.x > 0:
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
    def intersection(self, alpha, direction):
        horizontal_intersection = self.horizontal_intersection(alpha, direction)
        vertical_intersection = self.vertical_intersection(alpha, direction)
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
            return hor_dist
        else:
            return ver_dist

    # Cast a ray.
    def cast(self, direction):
        alpha = atan2(direction.y, direction.x)
        end_dist = self.intersection(alpha, direction)
        if end_dist is not None:
            self.end_dist = end_dist

### END ###
