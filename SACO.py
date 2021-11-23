from AntColony import AntColony
from Map import Map
from Visualizer import Visualizer
import Color as color
import pygame

class SACO:
    def __init__(self, dimensions, numberOfAnts, nest, food):
        self.dimensions = dimensions
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.nest = nest
        self.food = food
        self.antColony = AntColony(numberOfAnts, self.nest)
        self.map = Map(self.dimensions, self.nest, self.food)        
        #self.drawer = Visualizer(self.dimensions, color.black, "Ant Colony Optimization")
