import game_interaction as game
from color import color_t
from vec2 import vec2_t
from PIL import ImageGrab

StateAlive = 5
StateDead = 3

TileEmpty = 0
TileWall = 1
TileSpike = 2
TileEnemy = 3
TilePlayer = 4

colors = \
	[
		color_t( 128,128,128 ), # Empty
		color_t( 255,255,0 ), # Wall
		color_t( 211,211,211 ), # Spike
		color_t( 255,0,0 ), # Enemy/Dead
		color_t( 0,0,255 ), # Player
		color_t( 0,255,0 ), # Alive
	]

def match_color( col ):
	for i in range( len( colors ) ):
		if colors[i].equals( col ):
			return( i )
	return( 0 )

def check_state():
	return( match_color( game.get_pixel( 0,320 ) ) )

def find_everything():
	image = ImageGrab.grab().load()
	window = game.get_window_info()
	color_arr = []

	for y in range( 0,10 ):
		color_arr.append( [] )
		for x in range( 0,30 ):
			col = image[x + window.left,y + window.top + 320]
			emplace_back = match_color( color_t( col[0],col[1],col[2] ) )
			color_arr[y].append( emplace_back )
	return( color_arr )
