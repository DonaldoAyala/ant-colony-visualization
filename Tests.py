import pygame
from SACO import SACO
from Point import Point
from Visualizer import Visualizer
from Ant import Ant
from Map import Map

ant = Ant(Point(1,1))

map = Map((10,10), Point(2,2), [Point(9,9)])

for i in range(10):
    ant.move(map)

