from GameLogic import *
from GameObject import *
from Player import *
from Bullet import *
from Spawner import * 
import Patterns

import sys, pygame, math

class Mediator(object):
	def __init__(self,size):
		self.enemy_bullets = []
		self.pending_enemy_bullets = []
		self.enemies = []
		self.tick = 0
		self.size = size

	def set_stage(self,stage_dict):
		self.stage = stage_dict

	def runTick(self):
		self.tick += 1
		self.stage_stuff()
		self.actions()
		self.move_bullets()
		self.check_bound_bullets()

	def stage_stuff(self):
		for s in self.stage.get("spawnings"):
			if (self.get_tick() == s.get("spawns_at",0)):
				self.spawn_from_dict(s)

	def actions(self):
		tick = self.get_tick()
		for obj in self.get_all_objects():
			actions = obj.actions(tick)
			if len(actions) > 0: 
				for a in actions:
					self.perform_action(a,obj)

	def perform_action(self,action,obj):
		if action.get("action_type") == "spawn":
			if action.get("spawn").get("spawn_type") == "bullet":
				spawn = action.get("spawn")
				pattern = Patterns.PATTERNS.get(spawn.get("pattern_name"))
				bullets = pattern(obj,spawn.get("parameters"))
				self.add_enemy_bullets(bullets)
		if action.get("action_type") == "destroy":
			self.destroy_object(obj)

				

	def spawn_from_dict(self,spawn):
		image = pygame.image.load("../../graphics/{}".format(spawn["image"]))
		if spawn["type"] == "enemy":
			s = Spawner(spawn["velocity"],image,spawn["position"],spawn["outer_size"],spawn["actions"])
			s.set_tick_made(self.get_tick())
			self.add_enemy(s)
		
	def add_enemy_bullets(self,bullets):
		for b in bullets:
			if True:
				self.enemy_bullets.append(b)
			else:
				self.pending_enemy_bullets.append(b)

	def add_enemy(self,enemy):
		self.enemies.append(enemy)

	def get_tick(self):
		return self.tick

	def destroy_object(self,obj):
		if type(obj) is Bullet:
			self.enemy_bullets.remove(obj)
		elif type(obj) is Spawner:
			self.enemies.remove(obj)

	def move_bullets(self):
		for b in self.enemy_bullets:
			b.move()

	def get_all_objects(self):
		objs = []
		objs += self.enemy_bullets
		objs += self.enemies
		return objs

	def add_objects_to_screen(self,screen):
		for b in self.get_all_objects():
			screen.blit(b.get_image(),b.get_rect())

	def check_bound_bullets(self):
		for b in self.enemy_bullets:
			if self.out_of_field(b):
				self.destroy_object(b)

	def out_of_field(self,b):
		if b.pos[0] < -50 or b.pos[1] < -50 or b.pos[0] > self.size[0]+50 or b.pos[1] > self.size[1]+50:
			return True
		return False
