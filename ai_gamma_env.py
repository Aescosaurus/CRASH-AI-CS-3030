import random
import object_finder as obj_finder
import game_interaction as game
from vec2 import vec2_t

class env:
	def __init__( self ):
		self.reset()

	def step( self,action,tilemap ):
		player_pos = obj_finder.find_player( tilemap )

		self.data = []
		for y in range( player_pos.y - 1,player_pos.y + 2 ):
			for x in range( player_pos.x + 1,player_pos.x + 3 ):
				if obj_finder.get_tile( tilemap,x,y ) == obj_finder.TileEmpty:
					self.data.append( 0 )
				elif obj_finder.get_tile( tilemap,x,y ) == obj_finder.TileWall:
					self.data.append( 1 )
				else:
					self.data.append( 2 ) # 2 = obstacle / kill u.

		reward = 0
		done = False
		if tilemap[0][0] == obj_finder.StateDead:
			reward -= 10
			done = True
		else:
			reward += 1

		if obj_finder.find_explosion( tilemap ).not_equal( vec2_t( -1,-1 ) ):
			reward += 5

		if action == 0:
			reward += 1
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
		return( int( s,3 ) )

	def get_action_space( self ):
		return( 3 ) # Wait, jump, dash.

	def get_observation_space( self ):
		return( 728 + 1 ) # 222222 ternary to decimal.
	
	def get_sample_action( self ):
		return( random.randint( 0,2 ) )