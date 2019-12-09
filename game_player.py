import game_interaction as game
import time
import object_finder as obj_finder
import threading
import ai_gamma

window_name = "Cave Runner Actual Sharp Hustle"
ai = ai_gamma.ai_gamma()

def start():
	# print( game.get_window_info())
	game.focus_window(window_name)
	time.sleep(0.2)
	game.click_start()
	game.click_start()

	ai.ai_start()

	start_time = time.perf_counter()
	time.sleep(0.2)
	dt_start = time.perf_counter()
	dt = 0.0
	while update(dt):
		dt = time.perf_counter() - dt_start
		dt_start = time.perf_counter()
	end_time = time.perf_counter()

	total_time = end_time - start_time
	return(total_time)

def update(dt):
	thread = threading.Thread(target = time.sleep,
		args = [1.0 / 12.0])
	thread.start()

	pixels = obj_finder.find_everything()
	# try:
	# 	ai.ai_step( pixels,dt )
	# except:
	# 	pass
	ai.ai_step(pixels, dt)

	thread.join()

	if pixels[0][0] == obj_finder.StateAlive:
		return(True)
	else:
		ai.ai_lose()
		return(False)

for i in range(500):
	print(start())
# times = []
# for i in range( 100 ):
# 	times.append( start() )
#
# text = ""
# for t in times:
# 	text += str( t )
# 	text += '\n'
#
# file = open( "Data/AiAlpha.txt",'w' )
# file.write( text )
# file.close()
