

class Cell:
    def __init__(self, type, pheromonLevel = 1, foodAmount = 0):
        self.type = type
        self.foodAmount = foodAmount
        self.pheromonLevel = pheromonLevel


    def __str__(self):
        return str(self.type)