import game_interaction as game
import time
import object_finder as obj_finder
import threading
import ai_alpha_1

window_name = "Cave Runner Actual Sharp Hustle"
ai1 = ai_alpha_1.ai_alpha_1()

def start():
	# print( game.get_window_info() )
	game.focus_window( window_name )
	time.sleep( 0.5 )
	game.click_start()

	ai1.ai_start()

	start_time = time.perf_counter()
	time.sleep( 0.5 )
	dt_start = time.perf_counter()
	dt = 0.0
	while update( dt ):
		dt = time.perf_counter() - dt_start
		dt_start = time.perf_counter()
	end_time = time.perf_counter()

	total_time = end_time - start_time
	return( total_time )

def update( dt ):
	thread = threading.Thread( target = time.sleep,
		args = [ 1.0 / 12.0 ] )
	thread.start()
	
	ai1.ai_step( dt )

	thread.join()
	return( True )

print( start() )