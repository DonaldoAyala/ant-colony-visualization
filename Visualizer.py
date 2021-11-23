import pygame
import os
import time
import Color as color


class Visualizer:
    def __init__(self, dimensions, color):
        pygame.init()
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.dimensions = dimensions
        self.color = color
        self.window = pygame.display.set_mode(dimensions)
        self.running = True

    def center_window(self):
        os.environ['SDL_VIDEO_CENTERED'] = '0'

    def drawAnts(self, ants):
        for ant in ants:
            print(ant.position)
            pygame.draw.circle(self.window, color.yellow,
                               ant.position.tuple, ant.radius)

    def drawMap(self, map):
        for row in range(len(map.cells)):
            for col in range(len(map.cells[0])):
                if map.cells[row][col].type == 1:
                    pygame.draw.rect(self.window, color.green, (50, 50, 5, 5))

        return 0

    def start(self, saco):
        while(self.running):
            for event in pygame.event.get():
            	if event.type == pygame.QUIT:
            		self.running = False
            self.window.fill((0, 0, 0))
            self.drawMap(saco.map)
            self.drawAnts(saco.antColony.ants)
            pygame.display.flip()
