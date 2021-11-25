import numpy as np
import random as rand
from Point import Point

class Ant:
    def __init__(self, point):
        self.position = point
        self.forwardMode = True
        self.memory = [point]
        self.pathCost = 1e9
        # Movements are the directions in which ants can move
        # up, up-right, right, down-right, down, down-left, left, up-left
        self.movements = [Point(0,-1),Point(1,-1),Point(1,0),Point(1,1),Point(0,1),Point(-1,1),Point(-1,0),Point(-1,-1)]
        self.radius = 1
        self.pheromoneLevel = 1
        self.lastMovement = None
    
    def move(self, map):
        if self.forwardMode:
            # Get the sum of the neighbors except predecesor
            neighborSum = 0
            for movement in self.movements:
                next = movement + self.position
                if not map.isPointValid(next) or len(self.memory) == 0 or next == self.memory[-1]:
                    continue
                neighborSum += map.getCell(next).pheromoneLevel ** 2
            # Calculate probabilities of going to each neighbor
            weights = [0]*8
            for i in range(len(self.movements)):
                next = self.movements[i] + self.position
                if not map.isPointValid(next) or len(self.memory) == 0 or next == self.memory[-1]:
                    weights[i] = 0
                    continue
                weights[i] = (map.getCell(next).pheromoneLevel)**2 / neighborSum
            # Favoring forward movements
            if self.lastMovement is not None:
                lastMoveIndex = self.movements.index(self.lastMovement * -1)
                weights[(lastMoveIndex + 1) % len(weights)] *= 0.0001
                weights[(lastMoveIndex - 1) % len(weights)] *= 0.0001
                weights[(lastMoveIndex + 2) % len(weights)] *= 0.001
                weights[(lastMoveIndex - 2) % len(weights)] *= 0.001
                
            # Save the current position in the memory
            self.memory.append(self.position)
            # Select a move based on weights
            self.lastMovement = rand.choices(self.movements, weights)[0]
            self.position = self.position + self.lastMovement

            if map.getCellType(self.position) == 1: # Found food
                self.forwardMode = False
                # Calculate the amount of pheromones depending on the distance
                self.pheromoneLevel = 1000 / (len(self.memory))
        else:
            #map.depositPheromones(self.position, self.pheromoneLevel)
            map.depositPheromones(self.position, self.pheromoneLevel)

            if (len(self.memory) > 0):
                self.position = self.memory[-1]
                self.memory.pop()
            else:
                self.forwardMode = True
                self.memory.append(self.position)
            
