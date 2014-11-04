from Mediator import *

import sys, pygame, math

class DanmakuGame(object):
	size = width, height = 500,700
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode(self.size)
		self.mediator = Mediator(self.size)
		self.clock = pygame.time.Clock()
		
	def mainLoop(self):
		import stage_1
		myfont = pygame.font.SysFont("monospace",15)
		stage = stage_1.stage
		self.mediator.set_stage(stage)

		while True:
			tick = self.mediator.get_tick()
			for event in pygame.event.get():
				if event.type == "pygame.QUIT": sys.exit

			self.mediator.controller_input(pygame.key.get_pressed())
			
			self.screen.fill((0,0,0))

			self.mediator.runTick()
			self.mediator.add_objects_to_screen(self.screen)
			label = myfont.render("{} FPS".format(int(self.clock.get_fps())),1,(255,255,0))
			self.screen.blit(label, (400,650))
			label = myfont.render("{} Objects".format(len(self.mediator.get_all_objects())),1,(255,255,0))
			self.screen.blit(label, (0,650))
			label = myfont.render("Tick: {}".format(tick),1,(255,255,0))
			self.screen.blit(label, (200,650))
			pygame.display.flip()
			self.clock.tick(60)
			
