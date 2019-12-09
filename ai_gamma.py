"""TODO: qlearning stuff"""
import game_interaction as game
import object_finder as obj_finder
import ai_gamma_env
import random
import numpy as np


class ai_gamma:
	"""Docstring..."""
	def ai_start(self):
		"""Docstring..."""
		self.training_mode = True
		self.env = ai_gamma_env.env()

		self.q_table = np.zeros([self.env.get_observation_space(),
								 self.env.get_action_space()])

		file = open("Data/AiGammaQTable.txt",'r')
		i = 0
		for line in file.readlines():
			strs = []
			strs.append("")
			for c in line:
				if c == ' ':
					strs.append("")
				else:
					strs[-1] += c
			for s in range(len(strs) - 1):
				self.q_table[i][s] = float(strs[s])
		file.close()
		pass

	def ai_step(self, tilemap, dt):
		"""Docstring..."""
		if self.training_mode:
			# Alpha (learning rate) is how much we update q each step.
			alpha = 0.5
			# Gamma (discount factor) is how much weight is placed on future rewards.
			gamma = 0.2
			# Epsilon is propensity for exploration (only applies to learning).
			epsilon = 0.6

			# state = self.env.reset()
			state = self.env.step(0, tilemap)[0]
			reward = 0.0

			if random.uniform(0.0, 1.0) < epsilon:
				action = self.env.get_sample_action()
			else:
				action = np.argmax(self.q_table[state])

			step_info = self.env.step(action, tilemap)
			next_state = step_info[0]
			reward = step_info[1]

			old_value = self.q_table[state, action]
			next_max = np.max(self.q_table[next_state])

			new_value = ((1.0 - alpha) * old_value) + \
						(alpha * (reward + gamma * next_max))

			self.q_table[state, action] = new_value

			# print("aaaa", old_value, new_value)

			self.state = next_state
			pass
		else:
			pass
		pass

	def ai_lose( self ):
		"""print(self.q_table)"""
		file = open("Data/AiGammaQTable.txt",'w')
		for i in self.q_table:
			for j in i:
				file.write(str(j) + ' ')
			file.write('\n')
		file.close()
		pass
