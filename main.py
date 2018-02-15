from implement import *

# Global Variable

my_state = intial_state(4, 4, 2)

class Node(object):
    def __init__(self):
        self.parent = None
        self.children = []
        self.action = None 
        self.state = None
        self.utility = None

    def add_child(self, node):
    	self.children.append(node)

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


# def tree_generator(current_state, player):

# 	possible_moves = move_generator(current_state, player)
# 	temp_depth = 0

# 	while temp_depth < 3:

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

	display_state(my_state)

	print(possible_states(my_state, "O"))

	# print(utility_generator("X", my_state))
	# print(terminal_test(my_state))