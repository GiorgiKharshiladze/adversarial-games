from implement import *
from sys import maxsize as maximum

# Global Variable
MAX_VALUE = maximum
MIN_VALUE = -maximum

print(MIN_VALUE)
my_state = intial_state(4, 4, 2)

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