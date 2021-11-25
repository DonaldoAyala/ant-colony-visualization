import pygame
import os
import time
import Color as color
from Point import Point
from Cell import Cell


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
            if ant.forwardMode:
                pygame.draw.circle(self.window, color.red,
                               ant.position.tuple, ant.radius)
            else:
                pygame.draw.circle(self.window, color.green,
                               ant.position.tuple, ant.radius)

    def drawMap(self, map):
        for row in range(len(map.cells)):
            for col in range(len(map.cells[0])):
                if map.cells[row][col].type == 1:
                    pygame.draw.circle(self.window, color.green, (row, col), 1)
                elif map.cells[row][col].type == -1:
                    pygame.draw.rect(self.window, color.yellow, (row, col, 2, 2))
                elif map.cells[row][col].pheromoneLevel > 0.1:
                    pygame.draw.circle(self.window, color.gray, (row, col), 1)
                

    def start(self, saco):
        while(self.running):
            for event in pygame.event.get():
            	if event.type == pygame.QUIT:
            		self.running = False
            self.window.fill((0, 0, 0))
            self.drawMap(saco.map)
            self.drawAnts(saco.antColony.ants)

            click = pygame.mouse.get_pressed()[0]
            if click:
                position = pygame.mouse.get_pos()
                saco.map.setCell(Point(position[1], position[0]), Cell(1, pheromoneLevel=1, foodAmount=1))

            saco.antColony.updateAnts(saco.map)
            saco.map.evaporatePheromones(0.99)

            pygame.display.flip()

            time.sleep(0.08)
