import random
import object_finder as obj_finder
import game_interaction as game

class env:
	def __init__( self ):
		self.reset()

	def step( self,action,tilemap ):
		player_pos = obj_finder.find_player( tilemap )
		# for y in range( player_pos.y - 1,player_pos.y + 2 ):
		# 	for x in range( player_pos.x + 1,player_pos.x + 4 ):
		# 		self.data[y * 2 + x] = ( tilemap[y][x] == TileEmpty ) if 0 else 1
		data = []
		for y in range( player_pos.y - 1,player_pos.y + 1 ):
			for x in range( player_pos.x + 1,player_pos.x + 3 ):
				data.append( ( x,y ) )
		print( data )

		reward = 0
		done = False
		if tilemap[0][0] == obj_finder.StateDead:
			reward -= 10
			done = True
		else:
			reward += 1

		if action == 0:
			# Reward here maybe?
			pass
		elif action == 1:
			game.press_jump()
		elif action == 2:
			game.press_dash()

		return( ( self.calc_state(),reward,done ) )

	def reset( self ):
		self.data = []
		for i in range( 2 * 3 ):
			self.data.append( 0 )
		return( self.calc_state() )

	def calc_state( self ):
		s = ""
		for item in self.data:
			s += str( item )
		return( int( s,2 ) )

	def get_action_space( self ):
		return( 3 ) # Wait, jump, dash.

	def get_observation_space( self ):
		return( 2 ** 6 )
	
	def get_sample_action( self ):
		return( random.randint( 0,2 ) )