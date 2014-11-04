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
	bullet_hitbox = bullet_definition.get("hitbox",(1,1))

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
		bullet = Bullet(spawner.mediator,(speed*math.sin(rads),speed*math.cos(rads)),bullet_image,position,bullet_dimensions,bullet_hitbox,parameters.get("actions",{}))
		bullet.set_parent(spawner)
		bullet.set_tick_delay(delay)
		bullets.append(bullet)
	return bullets

def line_func(spawner,parameters):
	"""pattern_name = line ------- Standard parameters, plus:
		Position_x_offset
		Position_y_offset
		n_bullets
	"""
	bullets = []
	bullet_definition = BULLET_TYPE[parameters["bullet_type"]]
	bullet_image = pygame.image.load("../../graphics/{}".format(bullet_definition["image"]))
	bullet_dimensions = bullet_definition.get("dimensions")
	bullet_hitbox = bullet_definition.get("hitbox",(1,1))

	position_x_offset = parameters.get("position_x_offset",35)
	position_y_offset = parameters.get("position_y_offset",0)
	angle_offset = parameters.get("angle_offset",0)
	n_bullets = parameters.get("n_bullets",1)

	speed = parameters.get("bullet_speed",3.5)
	target = parameters.get("target","absolute")
	base_position = spawner.get_position(parameters.get("spawn_from","midbottom"))
	for n in range(n_bullets):
		offset = n - math.ceil(n_bullets / 2)
		pos = ((base_position[0] + offset * position_x_offset), (base_position[1] + offset * position_y_offset))
		frame_angle = get_frame_angle(target,spawner.mediator,pos,spawner)
		angle = frame_angle + offset * angle_offset
		angle = math.radians(angle)
		bullet = Bullet(spawner.mediator,(speed*math.sin(angle),speed*math.cos(angle)),bullet_image,pos,bullet_dimensions,bullet_hitbox,parameters.get("actions",{}))
		bullets.append(bullet)
	return bullets
		
ARC_FUNC = lambda spawner, parameters: arc_func(spawner,parameters)
LINE_FUNC = lambda spawner, parameters: line_func(spawner,parameters)

PATTERNS = { "arc" : ARC_FUNC, "line" : LINE_FUNC }

BULLET_TYPE = {"test" : {
			"image" : "test-bullet.png",
			"actions" : [],
			"dimensions" : (20,20),
			"hitbox" : (15,15),
			}
		}
