"""Find objects in the game window using tile map."""
import game_interaction as game
from color import color_t
from vec2 import vec2_t
from PIL import ImageGrab
import time

StateAlive = 5
StateDead = 3

TileEmpty = 0
TileWall = 1
TileSpike = 2
TileEnemy = 3
TilePlayer = 4
TileExplode = 6

colors = \
	[
		color_t(128 ,128 ,128), # Empty
		color_t(255, 255 , 0), # Wall
		color_t(211, 211, 211), # Spike
		color_t(255, 0, 0), # Enemy/Dead
		color_t(0, 0, 255), # Player
		color_t(0, 255, 0), # Alive
		color_t(0, 255, 255), # Enemy explode
	]

def match_color(col):
	"""Match the color of the tiles."""
	for i in range(len(colors)):
		if colors[i].equals(col):
			return(i)
	return(0)

def find_everything():
	"""Find everything in the tile map."""
	# t = time.perf_counter()
	image = ImageGrab.grab().load()
	window = game.get_window_info()
	color_arr = []

	for y in range(0, 10):
		color_arr.append([])
		for x in range(0, 30):
			col = image[x + window.left,y + window.top + 320]
			emplace_back = match_color(color_t(col[0], col[1], col[2]))
			color_arr[y].append(emplace_back)
	# print(time.perf_counter() - t)
	return(color_arr)

def find_player(colors):
	"""FInd the player using the tile map and colors."""
	for y in range(len(colors)):
		for x in range(len(colors[y])):
			if colors[y][x] == TilePlayer:
				return(vec2_t(x, y))
	return(vec2_t(-1, -1))

def find_explosion(colors):
	"""Find the explostions using the tile map and colors."""
	for y in range(len(colors)):
		for x in range(len(colors[y])):
			if colors[y][x] == TileExplode:
				return(vec2_t(x, y))
	return(vec2_t(-1, -1))

def get_tile(pixels, x, y):
	"""Get the tile on the tile maps."""
	if x < 0 or x >= 30 or y < 0 or y >= 10:
		return(TileEmpty)
	return(pixels[y][x])
