import game_interaction as game
import object_finder as obj_finder
import ai_gamma_env
import random
import numpy as np

# TODO: qlearning stuff
class ai_gamma:
	def ai_start( self ):
		self.training_mode = True
		self.env = ai_gamma_env.env()

		# TODO: Load existing qtable from file.
		self.q_table = np.zeros( [ self.env.get_observation_space(),
			self.env.get_action_space() ] )
		pass

	def ai_step( self,tilemap,dt ):
		if self.training_mode:
			# Alpha (learning rate) is how much we update q each step.
			alpha = 0.5
			# Gamma (discount factor) is how much weight is placed on future rewards.
			gamma = 0.9
			# Epsilon is propensity for exploration (only applies to learning).
			epsilon = 0.6

			state = self.env.reset()
			reward = 0.0

			if random.uniform( 0.0,1.0 ) < epsilon:
				action = self.env.get_sample_action()
			else:
				action = np.argmax( q_table[state] )

			step_info = self.env.step( action,tilemap )
			next_state = step_info[0]
			reward = step_info[1]

			old_value = self.q_table[state,action]
			next_max = np.max( q_table[next_state] )

			new_value = ( ( 1.0 - alpha ) * old_value ) + \
				( alpha * ( reward + gamma * next_max ) )
			q_table[state,action] = new_value

			self.state = next_state
			pass
		else:
			pass
		pass

	def ai_lose( self ):
		file = open( "Data/AiGammaQTable.txt",'w' )
		for i in self.q_table:
			for j in i:
				file.write( str( j ) + ' ' )
			file.write( '\n' )
		file.close()
		pass