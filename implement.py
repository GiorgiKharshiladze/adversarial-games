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

def transition(state, start, finish):

	i_end = finish[0]
	j_end = finish[1]

	for i in range(len(state)):
		for j in range(len(state[i])):
			if (i, j) == start:
				state[i_end][j_end] = state[i][j]
				state[i][j] = "."

	return state


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
			all_moves[(i, j)] = directions(state, player, (i, j))

	return all_moves