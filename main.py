from implement import *
from sys import maxsize as maximum

# Global Variable
MAX_VALUE = maximum
MIN_VALUE = -maximum

my_state = intial_state(5,5,2)

def start_web():

	global my_state

	return my_state

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

def playGame(current_state, player_turn):
	if terminal_test(current_state) != True:
		if player_turn == "X":
			origin = tree_generator(current_state, player_turn, "conqueror")
			updated_state = minimax(origin, 2, True)[1]
			display_state(updated_state)
			print (" ")
			print (conqueror("X", updated_state))
			print (" ")
			playGame(updated_state, "O")

		elif player_turn == "O":
			origin = tree_generator(current_state, player_turn, "evasive")
			updated_state = minimax(origin, 2, True)[1]
			display_state(updated_state)
			print (" ")
			print (evasive("O", updated_state))
			print (" ")
			playGame(updated_state, "X")
	else:
		print ("Game over")


if __name__ == '__main__':
	
	# tran_state = transition(my_state, player, (6,0), (0,0))

	# print(move_generator(my_state, "O"))

	# display_state(my_state)

	# for i in possible_states(my_state, "X"):
	# 	display_state(i)
	# 	print()




	# origin = tree_generator(my_state, "X")

	# print("BEST VALUE ", minimax(origin, 2, True)[0])
	# display_state(minimax(origin, 2, True)[1])

	playGame(my_state, "O")
	#print (utility_generator("X", new_state))




	# for i in origin.children:
	# 	print("Parent :", i.utility)
	# 	print("--------------------")
	# 	for j in i.children:
	# 		print("Child node:", j.utility)
	# 	print("====================")


	# print(utility_generator("X", my_state))
	# print(terminal_test(my_state))