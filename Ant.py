import Point
import numpy as np
import random as rand

class Ant:
    def __init__(self, point):
        self.position = point
        self.forwardMode = True
        self.memory = [point]
        self.pathCost = 1e9
        # Movements are the directions in which ants can move
        # up, up-right, right, down-right, down, down-left, left, up-left
        self.movements = [Point(0,-1),Point(1,-1),Point(1,0),Point(1,1),Point(0,1),Point(-1,1),Point(-1,0),Point(-1,-1)]
    
    def move(self, map):
        # Get the sum of the neighbors except predecesor
        neighborSum = 0
        for movement in self.movements:
            next = movement + self.point
            if next == self.memory[-1]:
                continue
            neighborSum += map.getValue(next)
        # Calculate probabilities of going to each neighbor
        weights = [0]*8
        for i in range(len(self.movements)):
            next = self.movements[i] + self.point
            if next == self.memory[-1]:
                weights[i] = 0
                continue
            weights[i] = map.getValue(next) / neighborSum
        # Select a move based on weights
        self.position = self.position + rand.choices(self.movements, weights)


