stage = {"spawnings" : [{
	"image" : "test-enemy.png",
	"type" : "enemy",
	"spawns_at" : 20,
	"invulnerable" : True,
	"velocity" : (0,0),
	"position" : (200, 200),
	"outer_size" : (20, 60),
	"hithox_size" : (20, 60),
	"actions" : { 
                "singles" : [ { "tick" : 6000, "action_type" : "destroy" }, { "tick" : 120, "action_type" : "velocity", "new_velocity" : (0,0) } ],
		"repeatings" : [
			{
				"tick-length" : 30,
				"begins-tick" : 20,
				"actions" : [
					{
						"tick" : 1,
						"action_type" : "spawn",
						"spawn" : {
							"spawn_type" : "bullet",
							"pattern_name" : "arc",
							"parameters" : {
								"angle_start" : -5,
								"angle_end" : 5,
								"angle_interval" : 5,
								"bullet_type" : "test",
								"bullet_speed" : 2.5,
								"delay" : 0,
								"target" : "player",
								"spawn_from" : "midbottom",
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
	"position" : (200, 400),
	"outer_size" : (20, 60),
	"hithox_size" : (20,60),
	"actions" : { 
                "singles" : [ { "tick" : 100, "action_type" : "destroy" } ],
		"repeatings" : [
			{
				"tick-length" : 72,
				"begins-tick" : 20,
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
								"angle_interval" : 15,
								"delay" : 1,
								"bullet_type" : "test",
								"bullet_speed" : 3,
								"spawn_from" : "midbottom",
							}
						}
					},
					
				]
			},
			{
				"tick-length" : 18,
				"begins-tick" : 46,
				"actions" : [
					{
						"tick" : 1,
						"action_type" : "spawn",
						"spawn" : {
							"spawn_type" : "bullet",
							"pattern_name" : "arc",
							"parameters" : {
								"angle_start" : 450,
								"angle_end" : 270,
								"angle_interval" : -15,
								"delay" : 1,
								"bullet_type" : "test",
								"bullet_speed" : 2,
								"spawn_from" : "midbottom",
							}
						}
					},
					
				]
			}
		]
	}
}]
}			

