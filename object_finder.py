import game_interaction as game
from color import color_t
from vec2 import vec2_t

def find_player():
	for y in range( 0,10 ):
		for x in range( 0,30 ):
			if game.get_pixel( x,y + 320 ).equals( color_t( 0,0,255 ) ):
				return( vec2_t( x,y ) )
