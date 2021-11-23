from Cell import Cell

class Map:
    def __init__(self, dimensions, nest, food):
        self.dimensions = dimensions
        self.width = dimensions[1]
        self.height = dimensions[0]
        self.cells = [[Cell(0, pheromonLevel = 1) for i in range(self.width)] for i in range(self.height)]
        self.setCell(nest, Cell(-1))
        for point in food:
            self.setCell(point, Cell(1, foodAmount = 5))
            
    def setCell(self, point, value):
        self.cells[point.y][point.x] = value

    def getCell(self, point):
        return self.cells[point.y][point.x]

    def isPointValid(self, point):
        return 0 <= point.x <= self.width and 0 <= point.y <= self.height

    def print(self):
        for row in self.cells:
            for el in row:
                print(el, end= " ")
            print()

        


