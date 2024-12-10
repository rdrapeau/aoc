GUARDS = {
	'^': (-1, 0, '>'),
	'v': (1, 0, '<'),
	'>': (0, 1, 'v'),
	'<': (0, -1, '^')
}
OBSTACLE = '#'


def find_starting_position(map_data):
	for i, row in enumerate(map_data):
		for guard in GUARDS:
			if guard in row:
				guard_index = row.index(guard)
				return (i, guard_index, map_data[i][guard_index])


def traverse_map(map_data, starting_position):
	row, col, guard_direction = starting_position
	seen_positions = set([starting_position])
	while row >= 0 and col >= 0 and row < len(map_data) and col < len(map_data[0]):
		delta = GUARDS[guard_direction]
		next_row = row + delta[0]
		next_col = col + delta[1]
		if next_row < 0 or next_row >= len(map_data) or next_col < 0 or next_col >= len(map_data[0]):
			return False, seen_positions

		if map_data[next_row][next_col] == OBSTACLE:
			guard_direction = delta[2]
		else:
			row = next_row
			col = next_col

		next_position = (row, col, guard_direction)
		if next_position in seen_positions:
			return True, seen_positions
		else:
			seen_positions.add(next_position)

	return False, seen_positions


def find_unique_guard_positions(seen_positions):
	return len(set([(row, col) for row, col, _ in seen_positions]))


def find_num_cycles(map_data, seen_positions, starting_position):
	num_cycles = 0
	unique_positions_on_original_path = set([(row, col) for row, col, _ in seen_positions])
	for row, col in unique_positions_on_original_path:
		if map_data[row][col] == '.' and (row != starting_position[0] or col != starting_position[1]):
			map_data[row][col] = OBSTACLE
			has_loop, _ = traverse_map(map_data, starting_position)
			if has_loop:
				num_cycles += 1

			map_data[row][col] = '.'

	return num_cycles


def main():
	with open('input.txt') as f:
		map_data = [[c for c in row.strip()] for row in f.readlines()]


	starting_position = find_starting_position(map_data)
	map_data[starting_position[0]][starting_position[1]] = '.'
	
	# Part 1
	_, seen_positions = traverse_map(map_data, starting_position)
	print(find_unique_guard_positions(seen_positions))

	# Part 2
	print(find_num_cycles(map_data, seen_positions, starting_position))


if __name__ == '__main__':
	main()