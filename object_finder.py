import game_interaction as game
from color import color_t
from vec2 import vec2_t
from PIL import ImageGrab

def find_player():
	for y in range( 0,10 ):
		for x in range( 0,30 ):
			if game.get_pixel( x,y + 320 ).equals( color_t( 0,0,255 ) ):
				return( vec2_t( x,y ) )

def find_everything():
	image = ImageGrab.grab().load()
	window = game.get_window_info()
	color_arr = []
	colors = \
		[
			color_t( 128,128,128 ), # Empty
			color_t( 255,255,0 ), # Wall
			color_t( 211,211,211 ), # Spike
			color_t( 255,0,0 ), # Enemy/Loss
			color_t( 0,0,255 ), # Player
			color_t( 0,255,0 ), # Win
		]

	for y in range( 0,10 ):
		for x in range( 0,30 ):
			print( vec2_t( x + window.left,y + window.top + 320 ) )
			col = image[x + window.left,y + window.top + 320]
			emplace_back = 0
			print( col )
			for i in range( len( colors ) ):
				if colors[i].equals( color_t( col[0],col[1],col[2] ) ):
					emplace_back = i
					break
			color_arr.append( emplace_back )
	return( color_arr )
