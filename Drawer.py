import pygame
import os
import time
import Color as color

class Drawer:
	def __init__(self, width, height, color, caption):
		self.width = width
		self.height = height
		self.center_window()
		self.color = color
		self.caption = caption
		self.window = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption(self.caption)

	def print_text(self, text, position, font_size, color):
		my_font = pygame.font.SysFont('franklingothicmedium', font_size)
		local_text = my_font.render(text, True, color)
		self.window.blit(local_text, position +
		                 (len(text) * font_size + 5, font_size + 5))

	def center_window(self):
		os.environ['SDL_VIDEO_CENTERED'] = '0'

	def drawAnt(self, coin):
		pygame.draw.circle(self.window, color.yellow, coin.center, coin.radius)

	def drawMap(self, map):
		for row in range(len(map.cells)):
			for col in range(len(map.cells[0])):
				if map.cells[row][col].type == 1:
					pygame.draw.rect(self.window, color.green, (50, 50, 5, 5))
				elif map.cells[row][col].type == -1:
					pygame.draw.rect(self.window, color.yellow, (col, row, 5, 5))
		return 0

	def refresh(self, map, ants = []):
		self.window.fill(color.black)
		self.drawMap(map)
		pygame.display.update()
