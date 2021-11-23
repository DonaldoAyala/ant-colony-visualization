

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tuple = (x,y)

    

    def __add__(self, point):
        x = self.x + point.x
        y = self.y + point.y
        return Point(x, y)
    
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y