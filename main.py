from implement import *
from sys import maxsize as maximum

# Global Variable
MAX_VALUE = maximum
MIN_VALUE = -maximum

my_state = intial_state(6, 6, 2)
all_moves = []

def start_web():

	global my_state

	return my_state

def end_web():
	
	return playWeb(my_state, "O")

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
			best_value = max(best_value, my_value)

		return best_value, i.state

	else:

		best_value = MAX_VALUE
		for i in node.children:
			my_value = minimax(i, depth-1, True)[0]
			best_value = min(best_value, my_value)

		return best_value, i.state

def playWeb(current_state, player_turn):
	if terminal_test(current_state) != True:
		if player_turn == "X":
			origin = tree_generator(current_state, player_turn, "conqueror")
			updated_state = minimax(origin, 2, True)[1]
			all_moves.append(myMove(current_state, updated_state, player_turn))
			playWeb(updated_state, "O")

		elif player_turn == "O":
			origin = tree_generator(current_state, player_turn, "evasive")
			updated_state = minimax(origin, 2, True)[1]
			all_moves.append(myMove(current_state, updated_state, player_turn))
			playWeb(updated_state, "X")

	return all_moves

def playGame(current_state, player_turn):
	if terminal_test(current_state) != True:
		if player_turn == "X":
			origin = tree_generator(current_state, player_turn, "conqueror")
			updated_state = minimax(origin, 2, True)[1]
			all_moves.append(myMove(current_state, updated_state, player_turn))
			display_state(updated_state)
			print (" ")
			print (conqueror("X", updated_state))
			print (" ")
			playGame(updated_state, "O")

		elif player_turn == "O":
			origin = tree_generator(current_state, player_turn, "evasive")
			updated_state = minimax(origin, 2, True)[1]
			all_moves.append(myMove(current_state, updated_state, player_turn))
			display_state(updated_state)
			print (" ")
			print (evasive("O", updated_state))
			print (" ")
			playGame(updated_state, "X")
	else:
		print("Game Over!")

	return all_moves


if __name__ == '__main__':

	# next_state = possible_states(my_state, "O")[0]

	# display_state(my_state)
	# print()
	# display_state(next_state)

	# myMove(my_state, next_state, "O")

	# tran_state = transition(my_state, player, (6,0), (0,0))

	# print(move_generator(my_state, "O"))

	# display_state(my_state)

	# for i in possible_states(my_state, "X"):
	# 	display_state(i)
	# 	print()

	# for i in tree_generator(my_state, "X", "evasive").children:
	# 	for j in i.children:
	# 		print(j.size)


	# origin = tree_generator(my_state, "X")

	# print("BEST VALUE ", minimax(origin, 2, True)[0])
	# display_state(minimax(origin, 2, True)[1])

	print(playGame(my_state, "O"))
	#print (utility_generator("X", new_state))


	# print(utility_generator("X", my_state))
	# print(terminal_test(my_state))