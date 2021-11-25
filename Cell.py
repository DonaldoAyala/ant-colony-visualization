from Point import Point

class Cell:
    def __init__(self, type, pheromoneLevel = 1, foodAmount = 0):
        self.type = type
        self.foodAmount = foodAmount
        self.pheromoneLevel = pheromoneLevel

    def evaporatePheromoneLevel(self, factor):
        # Minimum level of pheromones in a cell is 1
        self.pheromoneLevel = max(self.pheromoneLevel * factor, 0.1)

    def __str__(self):
        return str(self.type)