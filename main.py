from implement import *

# Global Variable

my_state = intial_state(6, 6, 2)

def start_web():

	global my_state

	return my_state


if __name__ == '__main__':

	
	# tran_state = transition(my_state, (6,0), (0,0))

	# print(move_generator(my_state, "O"))

	display_state(my_state)

	for i in range(len(my_state)):
		for j in range(len(my_state[i])):
			if my_state[i][j] == "O":
				my_state[i][j] = "."

	print(terminal_test(my_state))