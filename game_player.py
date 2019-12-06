import game_interaction as game
import time
import object_finder as obj_finder

window_name = "Cave Runner Actual Sharp Hustle"

def start():
	print( game.get_window_info() )
	game.focus_window( window_name )
	time.sleep( 0.5 )
	game.click_at( 0,0 )
	# game.focus_window( window_name )
	# time.sleep( 0.5 )
	# game.click_start()
	# time.sleep( 0.5 )
	# print( obj_finder.find_everything() )

start()
