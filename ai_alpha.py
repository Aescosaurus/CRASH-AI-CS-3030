"""Basic hardcoded ai, is quite dull and performs about as well as a below average player."""
import game_interaction as game
import object_finder as obj_finder
import time


class ai_alpha:
	"""Docstring..."""
	def ai_start(self):
		self.timer = 0.0
		pass

	def ai_step(self, tilemap, dt):
		"""Docstring..."""
		player_pos = obj_finder.find_player(tilemap)

		if tilemap[player_pos.y][player_pos.x + 1] == obj_finder.TileWall:
			self.timer += dt
			if player_pos.x < 12 or self.timer >= 0.6:
				self.timer = 0.0
				game.press_dash()
		if tilemap[player_pos.y + 1][player_pos.x + 1] == obj_finder.TileEmpty or \
			tilemap[player_pos.y + 1][player_pos.x + 3] == obj_finder.TileEmpty:
			game.press_jump()
		pass

	def ai_lose( self,time ):
		"""Docstring..."""
		pass
