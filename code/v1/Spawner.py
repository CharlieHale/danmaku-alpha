from GameObject import *

class Spawner(GameObject):
	def __init__(self,speed,image,pos,dimensions,action_dict):
		super(Spawner,self).__init__(speed,image,pos,dimensions,action_dict)

	def actions(self,tick):
		actions_activated = []
		for r in self.action_dict.get("repeatings",[]):
			pattern_tick = tick % r.get("tick-length")
			for a in r.get("actions",[]):
				if a.get("tick") == pattern_tick:
					actions_activated.append(a)
		
		for s in self.action_dict.get("singles",[]):
			tick_since = tick - self.tick_made
			if s.get("tick") == tick_since:
				actions_activated.append(s)

		return actions_activated
			
			