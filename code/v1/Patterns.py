import pygame, math

from Bullet import *

def arc_func(spawner, parameters):
	bullets = []
	bullet_definition = BULLET_TYPE[parameters["bullet_type"]]
	bullet_image = pygame.image.load("../../graphics/{}".format(bullet_definition["image"]))
	speed = parameters.get("bullet_speed",3.5)
	for angle in range(parameters.get("angle_start",0),parameters.get("angle_end",180),parameters.get("angle_interval",15)):
		rads = math.radians(angle)
		bullet = Bullet((speed*math.sin(rads),speed*math.cos(rads)),bullet_image,spawner.pos,(20,20),bullet_definition["actions"])
		bullet.set_parent(spawner)
		bullets.append(bullet)
	return bullets
		
ARC_FUNC = lambda spawner, parameters: arc_func(spawner,parameters)

PATTERNS = { "arc" : ARC_FUNC }

BULLET_TYPE = {"test" : {
			"image" : "test-bullet.png",
			"actions" : []
			}
		}
