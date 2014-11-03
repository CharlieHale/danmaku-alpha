from GameLogic import *
from GameObject import *

class Bullet(GameObject):
	def __init__(self,speed,image,pos,dimensions,action_dict):
		super(Bullet,self).__init__(speed,image,pos,dimensions,action_dict)
