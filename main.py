import pygame
from SACO import SACO
from Point import Point
from Visualizer import Visualizer

saco = SACO((500,500), 100, Point(100,100), [Point(50,50)])
visualizer = Visualizer((500,500), (255,255,255))

visualizer.start(saco)