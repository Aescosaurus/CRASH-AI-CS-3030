import game_interaction as game
import time
import object_finder as obj_finder

window_name = "Cave Runner Actual Sharp Hustle"

def start():
	print( game.get_window_info() )
	game.focus_window( window_name )
	time.sleep( 0.5 )
	game.click_start()
	start_time = time.perf_counter()
	time.sleep( 0.5 )
	while update(): continue
	end_time = time.perf_counter()
	total_time = end_time - start_time
	return( total_time )

def update():
	# Do ai stuff here.

	time.sleep( 1.0 / 60.0 )
	return( True )

print( start() )