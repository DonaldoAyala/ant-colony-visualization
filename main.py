import pygame
from SACO import SACO
from Point import Point
from Visualizer import Visualizer

saco = SACO((100,100), 300, Point(0,0), [Point(5,5)])
visualizer = Visualizer((100,100), (255,255,255))

visualizer.start(saco)