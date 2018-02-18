from implement import *
from sys import maxsize as maximum

# Global Variable
MAX_VALUE = maximum
MIN_VALUE = -maximum

print(MIN_VALUE)
my_state = intial_state(4, 4, 2)


def tree_generator(current_state, player):

	root = Node(deepcopy(current_state), None)
	current_node = root

	for j in possible_states(current_state, player):
		current_node.add_child(Node(j, utility_generator(player, j)))


	for k in current_node.children:
		for l in possible_states(k.state, player):
			k.add_child(Node(l, utility_generator(player, l)))

	return root


def possible_states(current_state, player):

	every_state = []
	one_state = []

	possible_moves = move_generator(current_state, player)

	for i in possible_moves.keys():
		if len(possible_moves[i]) != 0:
			for j in possible_moves[i]:
				one_state = transition(current_state, player, i, j)
				every_state.append(one_state)

	return every_state

def start_web():

	global my_state

	return my_state


if __name__ == '__main__':

	
	# tran_state = transition(my_state, player, (6,0), (0,0))

	# print(move_generator(my_state, "O"))

	# display_state(my_state)

	# print(possible_states(my_state, "O"))

	for i in tree_generator(my_state, "X").children:
		print(i.utility)

	# print(utility_generator("X", my_state))
	# print(terminal_test(my_state))