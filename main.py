from implement import *
from sys import maxsize as maximum
from rules import rows, cols, row_pieces, starter

# Global Variable
MAX_VALUE = maximum
MIN_VALUE = -maximum

all_moves = []
my_state = intial_state(rows, cols, row_pieces)

def start_web():

	global my_state

	return my_state

def end_web():
	
	return playWeb(my_state, starter, "combine", "conqueror")

def myMove(state_old, state_new, player):
	change = []
	for i in range(len(state_old)):
		for j in range(len(state_old[i])):
			if state_old[i][j] != state_new[i][j]:
				change.append([i, j])

	if player == "O": # because it gives from, to move inverted
		change = change[::-1]

	return change

def minimax(node, depth, max_player):

	if depth == 0:
		return node.utility, node.state

	if max_player:

		best_value = MIN_VALUE
		for i in node.children:
			my_value = minimax(i, depth-1, False)[0]
			if best_value < my_value:
				best_value = my_value
				my_node = i

		return best_value, my_node.state

	else:

		best_value = MAX_VALUE
		for i in node.children:
			my_value = minimax(i, depth-1, True)[0]
			if best_value > my_value:
				best_value = my_value
				my_node = i

		return best_value, my_node.state

def playWeb(current_state, player_turn, X_strategy, O_strategy):
	if terminal_test(current_state) != True:
		if player_turn == "X":
			origin = tree_generator(current_state, player_turn, X_strategy)
			updated_state = minimax(origin, 2, True)[1]
			all_moves.append(myMove(current_state, updated_state, player_turn))
			playWeb(updated_state, "O", X_strategy, O_strategy)

		elif player_turn == "O":
			origin = tree_generator(current_state, player_turn, O_strategy)
			updated_state = minimax(origin, 2, True)[1]
			all_moves.append(myMove(current_state, updated_state, player_turn))
			playWeb(updated_state, "X", X_strategy, O_strategy)

	return all_moves

def playGame(current_state, player_turn, X_strategy, O_strategy):
	if terminal_test(current_state) != True:
		if player_turn == "X":
			origin = tree_generator(current_state, player_turn, X_strategy)
			updated_state = minimax(origin, 2, True)[1]
			all_moves.append(myMove(current_state, updated_state, player_turn))
			display_state(updated_state)
			print (" ")
			print (getUtility(X_strategy, "X", updated_state))
			print (" ")
			playGame(updated_state, "O", X_strategy, O_strategy)

		elif player_turn == "O":
			origin = tree_generator(current_state, player_turn, O_strategy)
			updated_state = minimax(origin, 2, True)[1]
			all_moves.append(myMove(current_state, updated_state, player_turn))
			display_state(updated_state)
			print (" ")
			print (getUtility(O_strategy, "O", updated_state))
			print (" ")
			playGame(updated_state, "X", X_strategy, O_strategy)
	else:
		print("Game Over!")


	return all_moves

if __name__ == '__main__':

	# print(terminal_test(my_state))

	# print(block("X", my_state))

	playGame(my_state, starter, "enhanced", "conqueror")

