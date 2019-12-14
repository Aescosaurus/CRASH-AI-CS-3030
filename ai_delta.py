import game_interaction as game
import object_finder as obj_finder
from ai_gamma import ai_gamma
import ai_gamma_env
import random
import os.path

class ai_delta:
	def __init__( self ):
		self.evolution_mode = True
		init_ai = ai_gamma()
		init_ai.ai_start()

		file_name = "Data/AiDeltaBest.txt"

		if os.path.exists( os.path.join( os.getcwd(),file_name ) ):
			self.load_file( init_ai,file_name )
		else:
			for i in range( len( init_ai.q_table ) ):
				for j in range( len( init_ai.q_table[0] ) ):
					init_ai.q_table[i][j] = random.uniform( 0.0,1.0 )
		
		print( "Set up initial ai." )
		if self.evolution_mode:
			gen_size = 3 # From 5.
			gen_deviation = 0.2
			self.ais = []
			self.rewards = []
			for i in range( gen_size ):
				self.ais.append( ai_gamma() )
				self.ais[-1].ai_start()
				self.ais[-1].training_mode = False
				self.deviate( self.ais[-1],gen_deviation )
				# self.rewards.append( 0 )

			print( "Generation initialized.  Size: {}. Genetic Diversity: {}"
				.format( gen_size,gen_deviation ) )
			
			self.cur_ai = -1
		else:
			print( "Enter path of the ai to be loaded: ",end = "" )
			ai_path = input()
			self.load_file( init_ai,ai_path )
			self.ais = []
			self.ais.append( init_ai )
			self.cur_ai = 0
			print( "Ai loaded from file." )
			pass
		pass

	def deviate( self,ai,deviation ):
		for i in range( len( ai.q_table ) ):
			for j in range( len( ai.q_table[0] ) ):
				ai.q_table[i][j] += random.uniform( -deviation,deviation )

	def load_file( self,init_ai,file_name ):
		file = open( file_name,'r' )
		i = 0
		for line in file.readlines():
			strs = []
			strs.append( "" )
			for c in line:
				if c == ' ':
					strs.append( "" )
				else:
					strs[-1] += c
			for s in range( len( strs ) - 1 ):
				init_ai.q_table[i][s] = float( strs[s] )
		file.close()

	def ai_start( self ):
		if self.evolution_mode:
			self.cur_ai += 1
			if self.cur_ai >= len( self.ais ):
				best = -1.0
				pos = 0
				for i in range( len( self.rewards ) ):
					if self.rewards[i] >= best:
						best = self.rewards[i]
						pos = i

				print( "Best ai: ai {} with a score of {}."
					.format( pos,best ) )

				file = open( "Data/AiDeltaBest.txt",'w' )
				for i in self.ais[pos].q_table:
					for j in i:
						file.write( str( j ) + ' ' )
					file.write( '\n' )
				file.close()

				print( "Saved best ai to Data/AiDeltaBest.txt." )

				self.__init__()
			else:
				print( "Running ai " + str( self.cur_ai ) )
		pass

	def ai_step( self,tilemap,dt ):
		self.ais[self.cur_ai].ai_step( tilemap,dt )
		pass

	def ai_lose( self,time ):
		if self.evolution_mode:
			# Some safety checks to make sure we don't break later.
			if time > 0.6 and len( self.rewards ) < 3:
				self.rewards.append( time )
		else:
			pass
		pass
