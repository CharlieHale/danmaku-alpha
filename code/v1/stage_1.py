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
                "singles" : [ { "tick" : 100, "action_type" : "destroy" }, { "tick" : 120, "action_type" : "velocity", "new_velocity" : (0,0) } ],
		"repeatings" : [
			{
				"tick-length" : 50,
				"begins-tick" : 20,
				"actions" : [
					{
						"tick" : 1,
						"action_type" : "spawn",
						"spawn" : {
							"spawn_type" : "bullet",
							"pattern_name" : "arc",
							"parameters" : {
								"angle_start" : 180,
								"angle_end" : 270,
								"angle_interval" : 5,
								"bullet_type" : "test",
								"bullet_speed" : 2.5,
								"delay" : 0,
								"target" : "absolute",
								"spawn_from" : "midbottom",
								"actions" : { "repeatings" : [{"tick-length" : 5, "actions" : [{"tick" : 1, "action_type" : "velocity", "d_velocity": (0.05,0.05) }]}] }
							}
						}
                                        },
						{
						"tick" : 26,
						"action_type" : "spawn",
						"spawn" : {
							"spawn_type" : "bullet",
							"pattern_name" : "arc",
							"parameters" : {
								"angle_start" : 90,
								"angle_end" : 180,
								"angle_interval" : 5,
								"bullet_type" : "test",
								"bullet_speed" : 2.5,
								"delay" : 0,
								"target" : "absolute",
								"spawn_from" : "midbottom",
								"actions" : { "repeatings" : [{"tick-length" : 5, "actions" : [{"tick" : 1, "action_type" : "velocity", "d_velocity": (-0.05,0.05) }]}] }
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
                "singles" : [ { "tick" : 10000, "action_type" : "destroy" } ],
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
							"pattern_name" : "line",
							"parameters" : {
								"n_bullets" : 5,
								"position_x_offset" : 35,
								"angle_offset" : 2,
								"target" : "player",
								"bullet_type" : "test",
								"bullet_speed" : 3,
								"spawn_from" : "midbottom",
							}
						}
					},
					
				]
			},
		]
	}
}]
}			

