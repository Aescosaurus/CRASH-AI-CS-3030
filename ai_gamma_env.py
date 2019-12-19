"""Docstring..."""
import random
import object_finder as obj_finder
import game_interaction as game
from vec2 import vec2_t

class env:
	"""Docstring..."""

	def __init__(self):
		"""Docstring..."""
		# self.reset()
		self.x_range = range( 1,7,2 )
		self.y_range = range( -1,4,2 )
		self.data = []
		for y in self.y_range:
			for x in self.x_range:
				self.data.append( 0 )

	def step(self, action, tilemap):
		"""Docstring..."""
		player_pos = obj_finder.find_player(tilemap)

		self.data = []
		# for y in range(player_pos.y - 1,player_pos.y + 2):
		# 	for x in range(player_pos.x + 1,player_pos.x + 3):
		# 		if obj_finder.get_tile(tilemap, x, y) == obj_finder.TileEmpty:
		# 			self.data.append(0)
		# 		elif obj_finder.get_tile(tilemap, x, y) == obj_finder.TileWall:
		# 			self.data.append(1)
		# 		else:
		# 			self.data.append(2) # 2 = obstacle / kill u.

		# self.data.append(int(float(player_pos.x) * (9.0 / 30.0)))
		# self.data.append(int(float(player_pos.y) * (9.0 / 10.0)))

		# Add proper data into array.
		for y in self.y_range:
			for x in self.x_range:
				tile = obj_finder.get_tile( tilemap,
					x + player_pos.x,y + player_pos.y )
				if tile == obj_finder.TileEmpty:
					self.data.append( 0 )
				elif tile == obj_finder.TileWall:
					self.data.append( 1 )
				else:
					self.data.append( 2 )

		reward = 0
		done = False
		if tilemap[0][0] == obj_finder.StateDead:
			reward -= 10
			done = True
		else:
			reward += 1

		if obj_finder.find_explosion(tilemap).not_equal(vec2_t(-1, -1)):
			reward += 5

		if action == 0:
			# reward += 1
			pass
		elif action == 1:
			reward += 1
			game.press_jump()
		elif action == 2:
			game.press_dash()

		return((self.calc_state(), reward, done))

	def calc_state(self):
		"""Docstring..."""
		s = ""
		for i in self.data:
			s += str( i )

		return( int( s,3 ) )

	def get_action_space(self):
		"""Wait, jump, dash."""
		return(3)

	def get_observation_space(self):
		"""222222 ternary to decimal."""
		# return(3 ** 6 + 1)
		return( 3 ** len( self.data ) + 1 )

	def get_sample_action(self):
		"""Docstring..."""
		return(random.randint(0, 2))
