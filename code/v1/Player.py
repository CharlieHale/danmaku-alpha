from GameLogic import *
from GameObject import *

import pygame, math

SPEED_REGULAR = 3
SPEED_FOCUSED = 1.5

class Player(GameObject):
	def __init__(self,mediator):
		super(Player, self).__init__(mediator,(0,0), pygame.image.load("../../graphics/test-player.png"),(200,200),(25,50),(2,2),{})
		self.focused = False

	def move(self):
		self.pos = (self.pos[0] + self.speed[0], self.pos[1] + self.speed[1])
		rect = self.get_rect()
		size = self.mediator.size
		if rect.bottom > size[1]:
			rect.bottom = size[1]
		if rect.top < 0:
			rect.top = 0
		if rect.right > size[0]:
			rect.right = size[0]
		if rect.left < 0:
			rect.left = 0

		self.pos = (rect[0],rect[1])
		

	def controller_input(self,input_array):
		self.focused = input_array[pygame.K_RSHIFT] or input_array[pygame.K_LSHIFT]
		x = 0
		y = 0
		if input_array[pygame.K_RIGHT]:
			x += 1
		if input_array[pygame.K_LEFT]:
			x -= 1
		if input_array[pygame.K_UP]:
			y -= 1
		if input_array[pygame.K_DOWN]:
			y += 1

		self.speed = self.get_speeds(x,y,self.focused)
		
		
	def get_speeds(self,x,y,focused):
		speed = SPEED_FOCUSED if focused else SPEED_REGULAR
		if x == 0:
			return (0,y*speed)
		if y == 0:
			return (x*speed,0)
		speed = speed * math.cos(45)
		return (x*speed,y*speed)
