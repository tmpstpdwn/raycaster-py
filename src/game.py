### IMPORTS ###

from settings import WINDOW_WIDTH, WINDOW_HEIGHT
import pygame
from map import Map
from raycaster import RayCaster
from ray import Ray

### Game CLASS ###

class Game:

    # Init necessary game variables.
    def __init__(self):

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.map = Map(self)
        self.player = self.map.player
        self.raycaster = RayCaster(self)

    # Event loop to look for events.
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    # Refresh screen and update objects.
    def update(self, dt):
        self.screen.fill('black')
        self.player.update(dt)
        self.raycaster.cast_all_rays()

    # Draw things on to, and update the screen
    def draw(self):
        self.raycaster.render()
        pygame.display.update()

    # Run the game
    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            self.event_loop()
            self.update(dt)
            self.draw()

### END ###
