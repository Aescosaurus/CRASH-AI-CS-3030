import game_interaction as game
import time
import object_finder as obj_finder

window_name = "Cave Runner Actual Sharp Hustle"

def start():
	game.focus_window( window_name )
	time.sleep( 0.5 )
	game.click_start()
	print( obj_finder.find_player() )

start()
