from GameLogic import *
import pygame

class GameObject(object):
	def __init__(self,mediator,speed,image,pos,dimensions,action_dict):
		rect_pos = pygame.Rect(0,0,dimensions[0],dimensions[1])
		rect_pos.center = pos
		self.mediator = mediator
		self.speed = speed
		self.dimensions = dimensions
		self.image = image
		self.pos = rect_pos
		self.action_dict = action_dict
		self.tick_delay = 0
		self.tick_made = 0
		self.parent = None

	def set_tick_made(self,tick):
		self.tick_made = tick

	def get_tick_made(self):
		return self.tick_made

	def set_tick_delay(self,n_ticks):
		self.tick_delay = n_ticks

	def get_position(self,posstring):
		return getattr(self.get_rect(), posstring)
	
	def decrement_tick_delay(self):
		self.tick_delay -= 1
		if (self.tick_delay <= 0):
			return True
		else:
			return False
	
	def set_parent(self,parent):
		self.parent = parent

	def move(self):
		self.pos = (self.pos[0] + self.speed[0], self.pos[1] + self.speed[1])

	def get_rect(self):
		return pygame.Rect(int(self.pos[0]),int(self.pos[1]),self.dimensions[0],self.dimensions[1])

	def get_image(self):
		return self.image

	def actions(self,tick):
		return []

	def set_velocity(self,vel):
		self.speed = vel
