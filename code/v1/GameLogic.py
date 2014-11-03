from Mediator import *

import sys, pygame, math

class DanmakuGame(object):
	size = width, height = 400,800
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode(self.size)
		self.mediator = Mediator(self.size)
		self.clock = pygame.time.Clock()
		
	def mainLoop(self):
		import stage_1
		stage = stage_1.stage
		self.mediator.set_stage(stage)

		while True:
			tick = self.mediator.get_tick()
			for event in pygame.event.get():
				if event.type == "pygame.QUIT": sys.exit
			
			self.screen.fill((0,0,0))

			self.mediator.runTick()
			self.mediator.add_objects_to_screen(self.screen)
			pygame.display.flip()
			self.clock.tick(60)
			print("TICK: {}, FPS: {}".format(self.mediator.get_tick(),self.clock.get_fps()))
