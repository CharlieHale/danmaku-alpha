stage = {"spawnings" : [{
	"image" : "test-enemy.png",
	"type" : "enemy",
	"spawns_at" : 20,
	"invulnerable" : True,
	"velocity" : (0,0),
	"position" : (200, 60),
	"outer_size" : (20, 60),
	"hithox_size" : (20,60),
	"actions" : { 
                "singles" : [ { "tick" : 1000, "action_type" : "destroy" } ],
		"repeatings" : [
			{
				"tick-length" : 30,
				"actions" : [
					{
						"tick" : 1,
						"action_type" : "spawn",
						"spawn" : {
							"spawn_type" : "bullet",
							"pattern_name" : "arc",
							"parameters" : {
								"angle_start" : 270,
								"angle_end" : 450,
								"angle_interval" : 30,
								"bullet_type" : "test",
								"bullet_speed" : 5,
							}
						}
			
					}
				]
			}
		]
	}
},
{
	"image" : "test-enemy.png",
	"type" : "enemy",
	"spawns_at" : 100,
	"invulnerable" : True,
	"velocity" : (0,0),
	"position" : (300, 600),
	"outer_size" : (20, 60),
	"hithox_size" : (20,60),
	"actions" : { 
                "singles" : [ { "tick" : 1000, "action_type" : "destroy" } ],
		"repeatings" : [
			{
				"tick-length" : 25,
				"actions" : [
					{
						"tick" : 1,
						"action_type" : "spawn",
						"spawn" : {
							"spawn_type" : "bullet",
							"pattern_name" : "arc",
							"parameters" : {
								"angle_start" : 90,
								"angle_end" : 270,
								"angle_interval" : 30,
								"bullet_type" : "test",
								"bullet_speed" : 5,
							}
						}
			
					}
				]
			}
		]
	}
}]
}			

