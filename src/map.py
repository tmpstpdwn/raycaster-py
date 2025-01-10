### IMPORTS ###

from settings import *
import pygame
from player import Player

### Map CLASS ###

class Map:

    # Init necessary variables.
    def __init__(self, game):
        self.game = game
        self.map1 = [
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '0'],
                ['0', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '0'],
                ['0', '_', '0', '_', '_', '0', '0', '_', '_', '_', '_', '_', '_', '_', '0', '0', '_', '_', '_', '0'],
                ['0', '_', '0', '_', '_', '0', '0', '_', '_', '_', '_', '_', '_', '0', '0', '0', '0', '_', '_', '0'],
                ['0', '_', '0', '0', '_', '_', '_', '_', '0', '0', '0', '_', '_', '0', '_', '_', '0', '_', '_', '0'],
                ['0', '_', '0', '0', '_', '_', '_', '_', '0', '_', '0', '_', '_', '0', '_', '_', '0', '_', '_', '0'],
                ['0', '_', '0', '0', '_', '_', '_', '_', '0', '_', '0', '_', '_', '0', '_', '_', '0', '_', '_', '0'],
                ['0', '_', '0', '0', '_', '_', '_', '_', '_', '_', '_', '_', '_', '0', '_', '_', '0', '_', '_', '0'],
                ['0', '_', '0', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '0'],
                ['0', '_', '0', '_', '_', '_', '_', '0', '_', '_', 'P', '_', '_', '_', '_', '_', '_', '_', '_', '0'],
                ['0', '_', '0', '_', '_', '0', '0', '0', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '0'],
                ['0', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '0'],
                ['0', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
                ]
        self.walls = []
        self.setup_map(self.map1)

    # Load the map into a dictionary.
    def load_map(self, map_array):
        map_data = {}
        for row, row_array in enumerate(map_array):
            for column, entity in enumerate(row_array):
                map_data[(row, column)] = entity
        return map_data
    
    # Setup map after loading.
    def setup_map(self, map_array):
        map_data = self.load_map(map_array)
        for row, column in map_data:
            entity = map_data[(row, column)]
            pos = (column * TILE_SIZE, row * TILE_SIZE)
            if entity == '0':
                self.walls.append((row, column))
            elif entity == 'P':
                self.player = Player(pos, self.game)
    
    # Check if there is a wall at (x, y).
    def has_wall(self, xy: tuple):
        x, y = xy
        return (y//TILE_SIZE, x//TILE_SIZE) in self.walls

### END ###
