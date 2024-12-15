from collections import deque

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


def get_next(cur, direction):
	return (cur[0] + direction[0], cur[1] + direction[1])


def find_box_positions(grid, pos):
	cur = grid[pos[0]][pos[1]]
	assert cur in BOXES
	if cur == 'O':
		return [pos]

	return [pos, (pos[0], pos[1] - 1)] if cur == ']' else [pos, (pos[0], pos[1] + 1)]


def box_bfs(grid, pos, direction):
	cur_box = find_box_positions(grid, pos)
	fringe = deque(cur_box)
	seen = set(cur_box)
	points_to_move = []
	while len(fringe) != 0:
		point = fringe.popleft()
		points_to_move.append(point)

		next_pos = get_next(point, direction)
		next_entry = grid[next_pos[0]][next_pos[1]]
		if next_entry == WALL:
			return None
		elif next_entry in BOXES:
			colliding_box_points = find_box_positions(grid, next_pos)
			for colliding_box_point in colliding_box_points:
				if colliding_box_point not in seen:
					fringe.append(colliding_box_point)
					seen.add(colliding_box_point)

	return points_to_move


def simulate(grid, moves):
	position = find_start(grid)
	for move in moves:
		direction = DIRECTIONS[move]
		new_pos = get_next(position, direction)

		k = grid[new_pos[0]][new_pos[1]]
		if k == WALL:
			continue
		elif k in BOXES:
			points_to_move = box_bfs(grid, new_pos, direction)
			if points_to_move is None:
				continue

			for point in points_to_move[::-1]:
				placement = get_next(point, direction)
				grid[placement[0]][placement[1]], grid[point[0]][point[1]] = grid[point[0]][point[1]], '.'

		grid[new_pos[0]][new_pos[1]], grid[position[0]][position[1]] = '@', '.'
		position = new_pos


def main():
	with open('input.txt') as f:
		data = f.read()
		input = [line.strip().split() for line in data.split('\n\n')]
		
		moves = ''.join([move for line in input[1:] for move in line])
		grid1 = [list(line) for line in input[0]]
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

	simulate(grid1, moves)	
	simulate(grid2, moves)	

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