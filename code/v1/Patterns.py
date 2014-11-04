import pygame, math

from Bullet import *

def get_frame_angle(frame_str,mediator,position,spawner):
	if (frame_str == "absolute"):
		return 0
	if (frame_str == "player"):
		player_pos = mediator.get_player_position().center
		dx = position[0] - player_pos[0]
		dy = position[1] - player_pos[1]
		angle = math.atan2(dx,dy)
		angle_deg = math.degrees(angle)+180
		return angle_deg
		
def arc_func(spawner, parameters):
	"""pattern_name = arc ------- Standard parameters, plus:
		angle_start
		angle_end
		angle_interval
	"""
	bullets = []
	bullet_definition = BULLET_TYPE[parameters["bullet_type"]]
	bullet_image = pygame.image.load("../../graphics/{}".format(bullet_definition["image"]))
	bullet_dimensions = bullet_definition.get("dimensions")

	angle_start = parameters.get("angle_start",0)
	angle_end = parameters.get("angle_end",180)
	angle_interval = parameters.get("angle_interval",15)

	speed = parameters.get("bullet_speed",3.5)
	target = parameters.get("target","absolute")
	position = spawner.get_position(parameters.get("spawn_from","midbottom"))
	n_angles = ((angle_end - angle_start) / angle_interval) + 1

	frame_angle = get_frame_angle(target,spawner.mediator,position,spawner)

	for n in range(n_angles):
		angle = (angle_start + (n * angle_interval) + frame_angle)
		delay = parameters.get("delay",2) * n
		rads = math.radians(angle)
		bullet = Bullet(spawner.mediator,(speed*math.sin(rads),speed*math.cos(rads)),bullet_image,position,bullet_dimensions,parameters.get("actions",{}))
		bullet.set_parent(spawner)
		bullet.set_tick_delay(delay)
		bullets.append(bullet)
	return bullets

		
ARC_FUNC = lambda spawner, parameters: arc_func(spawner,parameters)

PATTERNS = { "arc" : ARC_FUNC }

BULLET_TYPE = {"test" : {
			"image" : "test-bullet.png",
			"actions" : [],
			"dimensions" : (20,20),
			}
		}
