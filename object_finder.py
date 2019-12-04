import game_interaction as game
from color import color_t
import threading
import queue

def find_player():
	def check_pixels( queue,width ):
		print( width )
		while True:
			item = queue.get()
			if item == -1:
				print( "Thread done!" )
				break
				
			for x in range( width ):
				if x % 100 == 0:
					print( x )
				if game.get_pixel( x,item ) == color_t( 159,60,200 ):
					print( "Found it! " + str( x ) + " " + str( y ) )
			
			print( "Done checking row " + str( item ) )
			
	window_rect = game.get_window_info()
	
	q = queue.Queue()
	
	for y in range( window_rect.get_height() ):
		q.put( y )
	
	print( "Done setting up queue!" )
	threads = []
	for i in range( 2 ):
		q.put( -1 )
		threads.append( threading.Thread( target = check_pixels,
			args = [ q,window_rect.get_width() ]) )
		threads[-1].start()
	
	print( "Done setting up threads!" )
	
	for thread in threads:
		thread.join()
	
	print( "Done!" )