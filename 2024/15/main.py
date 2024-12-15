DIRECTIONS = {
	'^': (-1, 0),
	'>': (0, 1),
	'<': (0, -1),
	'v': (1, 0)
}
BOXES = {'O', '[', ']'}
WALL = '#'

def find_start(grid):
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] == '@':
				return (row, col)


def get_next(cur, direction, negate=False):
	return (cur[0] + direction[0], cur[1] + direction[1]) if not negate else (cur[0] - direction[0], cur[1] - direction[1])


def push_line_of_boxes(grid, new_pos, direction):
	cur_pos = new_pos
	while grid[cur_pos[0]][cur_pos[1]] != WALL and grid[cur_pos[0]][cur_pos[1]] in BOXES:
		cur_pos = get_next(cur_pos, direction)

	if grid[cur_pos[0]][cur_pos[1]] == WALL:
		return False

	while cur_pos != new_pos:
		next_pos = get_next(cur_pos, direction, negate=True)
		grid[cur_pos[0]][cur_pos[1]], grid[next_pos[0]][next_pos[1]] = grid[next_pos[0]][next_pos[1]], grid[cur_pos[0]][cur_pos[1]]
		cur_pos = next_pos

	return True


def find_box_pos(grid, pos):
	cur = grid[pos[0]][pos[1]]
	assert cur in {'[', ']'}
	return (pos, (pos[0], pos[1] - 1)) if cur == ']' else (pos, (pos[0], pos[1] + 1)) 


def box_bfs(grid, pos, direction):
	layers = []
	next_layer = set(find_box_pos(grid, pos))
	while len(next_layer) != 0:
		layers.append(next_layer)
		previous_layer = next_layer
		next_layer = set()
		for point in previous_layer:
			next_pos = get_next(point, direction)
			next_entry = grid[next_pos[0]][next_pos[1]]
			if next_entry == WALL:
				return None
			elif next_entry in BOXES:
				next_layer = next_layer.union(set(find_box_pos(grid, next_pos)))

	return layers


def p1_solve(grid, moves):
	position = find_start(grid)
	for move in moves:
		direction = DIRECTIONS[move]
		new_pos = get_next(position, direction)

		k = grid[new_pos[0]][new_pos[1]]
		if k == WALL:
			continue
		elif k in BOXES:
			did_push_successfully = push_line_of_boxes(grid, new_pos, direction)
			if not did_push_successfully:
				continue

		grid[position[0]][position[1]] = '.'
		grid[new_pos[0]][new_pos[1]] = '@'
		position = new_pos


def p2_solve(grid, moves):
	position = find_start(grid)
	for move in moves:
		direction = DIRECTIONS[move]
		new_pos = get_next(position, direction)

		k = grid[new_pos[0]][new_pos[1]]
		if k == WALL:
			continue
		elif k in BOXES:
			if move in ['<', '>']:
				did_push_successfully = push_line_of_boxes(grid, new_pos, direction)
				if not did_push_successfully:
					continue
			else:
				points_to_move = box_bfs(grid, new_pos, direction)
				if points_to_move is None:
					continue

				for layer in points_to_move[::-1]:
					for point in layer:
						 new_point = get_next(point, direction)
						 grid[new_point[0]][new_point[1]], grid[point[0]][point[1]] = grid[point[0]][point[1]], grid[new_point[0]][new_point[1]]

		grid[position[0]][position[1]] = '.'
		grid[new_pos[0]][new_pos[1]] = '@'
		position = new_pos


def main():
	with open('input.txt') as f:
		data = f.read()
		input = [line.strip().split() for line in data.split('\n\n')]
		
		moves = ''.join([move for line in input[1:] for move in line])
		grid1 = [[x for x in line] for line in input[0]]
		grid2 = []
		for row in grid1:
			row2 = []
			for item in row:
				if item == WALL:
					row2 += [WALL, WALL]
				elif item == '.':
					row2 += ['.', '.']
				elif item == 'O':
					row2 += ['[', ']']
				elif item == '@':
					row2 += ['@', '.']

			grid2.append(row2)

	p1_solve(grid1, moves)	
	p2_solve(grid2, moves)	

	p1, p2 = 0, 0
	for row in range(len(grid1)):
		for col in range(len(grid1[0])):
			if grid1[row][col] == 'O':
				p1 += 100 * row + col

	for row in range(len(grid2)):
		for col in range(len(grid2[0])):
			if grid2[row][col] == '[':
				p2 += 100 * row + col

	print(p1)
	print(p2)

if __name__ == '__main__':
	main()