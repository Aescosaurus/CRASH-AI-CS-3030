"""Focuses on the game window, plays game with supplied ai algorithm."""
import game_interaction as game
import time
import object_finder as obj_finder
import threading
import ai_gamma

# Set initial game window and ai values.
window_name = "Cave Runner Actual Sharp Hustle"
ai = ai_gamma.ai_gamma()

def start():
	"""Focus on the game window, track time, and perform update loop."""
	game.focus_window(window_name)
	time.sleep(0.2)
	game.click_start()
	game.click_start()

	# Start the ai.
	ai.ai_start()

	# Start tracking the run time.
	start_time = time.perf_counter()
	time.sleep(0.2)
	dt_start = time.perf_counter()
	dt = 0.0

	# Loop while the game is running.
	while update(dt):
		dt = time.perf_counter() - dt_start
		dt_start = time.perf_counter()
	end_time = time.perf_counter()

	# Return time.
	total_time = end_time - start_time
	return(total_time)

def update(dt):
	"""Update while the game is running."""

	# Start a thread.
	thread = threading.Thread(target = time.sleep,
		args = [1.0 / 12.0])
	thread.start()

	# Find the pixels in the tile map.
	pixels = obj_finder.find_everything()

	# Perform ai step actions.
	ai.ai_step(pixels, dt)

	# Wait for the thread to end.
	thread.join()

	# Check if alive.
	if pixels[0][0] == obj_finder.StateAlive:
		return(True)
	else:
		# If not alive, call ai.lose().
		ai.ai_lose()
		return(False)

def start_playing():
	"""Start playing for range(x) amount of iterations."""
	for i in range(500):
		print(start())

if __name__ == '__main__':
	start_playing()
	# write_times_to_file()

def write_times_to_file():
	times = []
	for i in range( 100 ):
		times.append( start() )

	text = ""
	for t in times:
		text += str( t )
		text += '\n'

	file = open( "Data/AiAlpha.txt",'w' )
	file.write( text )
	file.close()
