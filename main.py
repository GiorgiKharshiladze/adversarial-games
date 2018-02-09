def intial_state(rows, cols, row_pieces):

	state = []

	if row_pieces > rows or row_pieces % 2 != 0:

		raise Exception("Invalid number of Row Pieces")

	for i in range(0,rows):
		state.append([])

		for j in range(0, cols):
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



display_state(intial_state(8, 8, 4))