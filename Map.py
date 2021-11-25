from Cell import Cell

# Cell types:
# Nest = -1
# Food = 1

class Map:
    def __init__(self, dimensions, nest, food):
        self.dimensions = dimensions
        self.width = dimensions[1]
        self.height = dimensions[0]
        self.cells = [[Cell(0, pheromoneLevel = 1) for i in range(self.width)] for i in range(self.height)]
        self.setCell(nest, Cell(-1))
        for point in food:
            self.setCell(point, Cell(1, foodAmount = 5))
        self.createCustomMap()
    
    def createCustomMap(self):
        test = [[0 for i in range(self.width)] for i in range(self.height)]
        r = 1
        c = 1
        for row in range(self.height):
            c = r
            r += 1
            for col in range(self.width):
                if row == col:
                    self.cells[row][col] = Cell(0, pheromoneLevel=0.1)
                else:
                    self.cells[row][col] = Cell(0, pheromoneLevel=0.1)
                test[row][col] = c
                c += 1

    def setCell(self, point, value):
        self.cells[point.y][point.x] = value

    def getCell(self, point):
        return self.cells[point.y][point.x]

    def getCellType(self, point):
        return self.cells[point.y][point.x].type

    def depositPheromones(self, point, depositedPheromones):
        self.cells[point.y][point.x].pheromoneLevel += depositedPheromones

    def isPointValid(self, point):
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def evaporatePheromones(self, evaporationFactor = 0.99):
        for row in self.cells:
            for cell in row:
                cell.evaporatePheromoneLevel(evaporationFactor)
        

    def print(self):
        for row in self.cells:
            for el in row:
                print(el, end= " ")
            print()

        


