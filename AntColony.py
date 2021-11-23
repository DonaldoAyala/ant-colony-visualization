from Ant import Ant
from Point import Point

class AntColony:
    def __init__(self, antNumber = 10, nest = Point(0,0)):
        self.antNumber = antNumber
        self.ants = []
        for i in range(self.antNumber):
            self.ants.append(Ant(nest))
    
    def updateAnts(self, map):
        for ant in self.ants:
            ant.move(map)