"""TODO: qlearning stuff"""
import game_interaction as game
import object_finder as obj_finder
import ai_gamma_env
import random
import numpy as np


class ai_gamma:
	"""Gamma ai algorithm using Q Learning."""
	def ai_start(self):
		"""Start the ai. If making changes to Q_Table, training mode needs to be True"""
		self.training_mode = True
		self.env = ai_gamma_env.env()
		self.last_action = 0

		self.q_table = np.zeros([self.env.get_observation_space(),
								 self.env.get_action_space()])

		# file = open("Data/AiGammaQTable.txt",'r')
		# i = 0
		# for line in file.readlines():
		# 	strs = []
		# 	strs.append("")
		# 	for c in line:
		# 		if c == ' ':
		# 			strs.append("")
		# 		else:
		# 			strs[-1] += c
		# 	for s in range(len(strs) - 1):
		# 		self.q_table[i][s] = float(strs[s])
		# file.close()
		pass

	def ai_step(self, tilemap, dt):
		"""Docstring..."""
		player_pos = obj_finder.find_player( tilemap )
		# if obj_finder.get_tile( tilemap,player_pos.x,player_pos.y + 1 ) == \
		# 	obj_finder.TileEmpty or tilemap[0][0] != obj_finder.StateDead:
		# 	# Only update if we are touching the ground or dead.
		# 	pass
		tile_below = obj_finder.get_tile( tilemap,
			player_pos.x,player_pos.y + 1 )
		if self.training_mode and ( tile_below == obj_finder.TileWall \
			or tilemap[0][0] == obj_finder.StateDead ):
			# Alpha (learning rate) is how much we update q each step.
			alpha = 0.5
			# Gamma (discount factor) is how much weight is placed on future rewards.
			gamma = 0.2
			# Epsilon is propensity for exploration (only applies to learning).
			epsilon = 0.6

			# state = self.env.reset()

			# Initialize state.
			info = self.env.step(self.last_action, tilemap)
			state = info[0]
			reward = info[1]
			action = 0

			# Decide whether or not to try something new.
			if random.uniform(0.0, 1.0) < epsilon:
				action = self.env.get_sample_action()
			else:
				action = np.argmax(self.q_table[state])

			# Run step action.
			step_info = self.env.step(action, tilemap)
			next_state = step_info[0]
			# reward = step_info[1]

			# Modify Q_Table.
			old_value = self.q_table[state, self.last_action]
			next_max = np.max(self.q_table[next_state])

			new_value = ((1.0 - alpha) * old_value) + \
						(alpha * (reward + gamma * next_max))

			self.q_table[state, self.last_action] = new_value
			self.state = next_state

			self.last_action = action
			
			return( reward )
			pass
		elif tile_below == obj_finder.TileWall \
			or tilemap[0][0] == obj_finder.StateDead:
			info = self.env.step(0, tilemap)
			state = info[0]
			reward = info[1]
			action = np.argmax(self.q_table[state])
			self.env.step(action, tilemap)

			return( reward )
			pass
		pass

	def ai_lose( self,time ):
		"""Write the Q_table to a file."""
		file = open("Data/AiGammaQTable.txt",'w')
		for i in self.q_table:
			for j in i:
				file.write(str(j) + ' ')
			file.write('\n')
		file.close()
		pass
