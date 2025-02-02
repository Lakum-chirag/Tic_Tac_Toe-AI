import math
import random

class Player():
	def __init__(self,letter):
		self.letter = letter

	def get_move(self,game):
		pass

class HumanPlayer(Player):
	def __init__(self,letter):
		super().__init__(letter)

	def get_move(self,game):
		valid_square = False
		val = None

		while not valid_square:
			square = input(self.letter + 's Input Move(0-9) :')
			try:
				val = int(square)
				print(val)
				if val not in game.available_moves():
					raise ValueError
				valid_square = True
			except ValueError:
				print('Inavlid Input Try Again!!')
		return val

class RandomComputerPlayer(Player):
	def __init__(self,letter):
		super().__init__(letter)

	def get_move(self,game):
		square = random.choice(game.available_moves())
		return square

class SmartComputerPlayer(Player):
	def __init__(self,letter):
		super().__init__(letter)

	def get_move(self,game):
		if len(game.available_moves()) == 9:
			square = random.choice(game.available_moves())
		else:
			square = self.minmax(game,self.letter)['position']
		return square

	def minmax(self,state,player):
		max_player = self.letter
		other_player = 'O' if player == 'X' else 'X'

		if state.current_winner == other_player:
			return {'position':None,'score':1 * (state.num_empty_squres() + 1) 
			if other_player == max_player else -1 * (state.num_empty_squres() +1)}
		elif not state.empty_squres():
			return {'position' : None,'score' : 0}

		if player == max_player:
			best = {'position' : None,'score':-math.inf}
		else:
			best = {'position' : None,'score':math.inf}

		for possible_moves in state.available_moves():
			state.make_move(possible_moves,player)
			sim_score = self.minmax(state,other_player)

			state.board[possible_moves] = ' '
			state.current_winner = None
			sim_score['position'] = possible_moves

			if player == max_player:
				if sim_score['score'] > best['score']:
					best = sim_score
			else:
				if sim_score['score'] < best['score']:
					best = sim_score
		return best