# Part 1
def intial_state(rows, cols, row_pieces):

	state = []

	if row_pieces > rows or row_pieces % 2 != 0:

		raise Exception("Invalid number of Row Pieces")

	for i in range(rows):
		state.append([])

		for j in range(cols):
			state[i].append(".")

	row_piece = row_pieces // 2

	for i in range(row_piece):

		for j in range(len(state[i])):
			state[i][j] = "X"
			reversed_list = state[::-1]
			reversed_list[i][j] = "O"

	return state


def display_state(state):

	for row in state:
		print(''.join(row))

from copy import deepcopy
def transition(state, player, start, finish):

	i_end = finish[0]
	j_end = finish[1]

	our_state = deepcopy(state)

	for i in range(len(state)):
		for j in range(len(state[i])):
			if (i, j) == start:
				our_state[i][j] = "."
				our_state[i_end][j_end] = player

	return our_state

def terminal_test(state):

	x_count = 0
	o_count = 0
	winner = ""


	for i in range(len(state)):
		for j in range(len(state[i])):

			if i == 0:
				if state[i][j] == "O":
					winner = "O"

			if i == len(state):
				if state[i][j] == "X":
					winner = "X"

			if state[i][j] == "X":
				x_count += 1
			if state[i][j] == "O":
				o_count += 1

	if x_count == 0:
		winner = "O"
	elif o_count == 0:
		winner = "X"

	return "The winner is: " + winner


def directions(state, player, position):

	i = position[0]
	j = position[1]

	my_moves = []

	if player == "X" and i < len(state)-1:

		# Right
		if j > 0 and state[i+1][j-1] != "X":
			my_moves.append((i+1, j-1))
		# Forward
		if state[i+1][j] != "X":
			my_moves.append((i+1, j))
		# Left
		if j < len(state[i])-1 and state[i+1][j+1] != "X":
			my_moves.append((i+1, j+1))

	elif player == "O" and i != 0:

		# Left
		if j > 0 and state[i-1][j-1] != "O":
			my_moves.append((i-1, j-1))
		# Forward
		if state[i-1][j] != "O":
			my_moves.append((i-1, j))
		# Right
		if j < len(state[i])-1 and state[i-1][j+1] != "O":
			my_moves.append((i-1, j+1))

	return my_moves


def move_generator(state, player):

	all_moves = {}

	for i in range(len(state)):
		for j in range(len(state[i])):
			if state[i][j] == player:
				all_moves[(i, j)] = directions(state, player, (i, j))

	return all_moves

# Part 2
from random import random

class Node(object):
    def __init__(self, state, utility):
        self.parent = None
        self.children = []
        self.action = None 
        self.state = state
        self.utility = utility
        self.size = 0

    def add_child(self, node):
    	self.children.append(node)
    	node.parent = self
    	self.size += 1

    def is_root(self):
    	if self.parent == None:
    		return True
    	else:
    		return False

    def is_leaf(self):
    	if self.child == []:
    		return True
    	else:
    		return False

def utility_generator(player, current_state):

	if player == "X":
		return count_pieces("X", current_state) + random()
	elif player == "O":
		return count_pieces("O", current_state) + random()

def count_pieces(player, current_state):
	counter = 0
	for i in range(len(current_state)):
		for j in range(len(current_state[i])):
			if current_state[i][j] == player:
				counter += 1
	return counter


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