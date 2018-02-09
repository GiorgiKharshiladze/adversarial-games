from implement import *

# Global Variable

my_state = intial_state(6, 6, 4)

def start_web():

	global my_state

	return my_state


if __name__ == '__main__':

	
	# tran_state = transition(my_state, (6,0), (0,0))

	# print(move_generator(my_state, "O"))

	display_state(my_state)