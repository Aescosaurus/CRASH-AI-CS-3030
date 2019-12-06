import game_interaction as game
import object_finder as obj_finder
import time

class ai_alpha_1:
	def ai_start( self ):
		self.timer = 0.0
		self.timer2 = 0.0
		pass

	def ai_step( self,dt ):
		tilemap = obj_finder.find_everything()
		self.timer += dt
		self.timer2 += dt
		if self.timer >= 1.0:
			self.timer = 0.0
			game.press_jump()
		if self.timer2 >= 3.0:
			self.timer2 = 0.0
			game.press_dash()
