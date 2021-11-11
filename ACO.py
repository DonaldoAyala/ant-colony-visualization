from Map import Map
from Point import Point
from Cell import Cell

height = 10
width = 10

nest = [Point(5,5)]
food = [Point(0,0)]

map = Map((height, width), nest, food)
map.print()

