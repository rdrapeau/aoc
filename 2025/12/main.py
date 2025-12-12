def rotate_clockwise(m):
	return [''.join(list(reversed(col))) for col in zip(*m)]


def in_bounds(grid, row, col):
	return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[row])


def can_place_shape(grid, row, col, shape):
	for i in range(row, row + len(shape)):
		for j in range(col, col + len(shape[0])):
			if not in_bounds(grid, i, j) or (grid[i][j] == '#' and shape[i - row][j - col] == '#'):
				return False

	return True


def fill_shape(grid, row, col, shape, should_erase=False):
	for i in range(row, row + len(shape)):
		for j in range(col, col + len(shape[0])):
			if should_erase and shape[i - row][j - col] == '#':
				grid[i][j] = '.'
			elif not should_erase and shape[i - row][j - col] == '#':
				grid[i][j] = '#'


def can_fit(grid, remaining, presents):
	if max(remaining) == 0:
		return True

	next_present_index = None
	for i in range(len(remaining)):
		if remaining[i] > 0:
			next_present_index = i
			break

	for row in range(len(grid)):
		for col in range(len(grid[0])):
			for shape in presents[next_present_index]:
				if grid[row][col] == '.' and can_place_shape(grid, row, col, shape):
					fill_shape(grid, row, col, shape, should_erase=False)
					remaining[next_present_index] -= 1
					if can_fit(grid, remaining, presents):
						return True

					remaining[next_present_index] += 1
					fill_shape(grid, row, col, shape, should_erase=True)

	return False


def main():
	with open('input.txt') as f:
		data = f.read().split('\n\n')
		
	regions = {}
	for row in data[-1].split('\n'):
		line = row.split(':')
		regions[tuple(int(x) for x in line[0].split('x'))] = [int(x) for x in line[1].strip().split()]

	presents = []
	for row in data[:-1]:
		shape = row.split('\n')[1:]
		shape_90 = rotate_clockwise(shape)
		shape_180 = rotate_clockwise(shape_90)
		shape_270 = rotate_clockwise(shape_180)
		shape_rotations = [
			shape,
			shape_90,
			shape_180,
			shape_270
		]
		presents.append(shape_rotations)

	ans = 0 
	for region in regions:
		grid = [['.'] * region[1] for _ in range(region[0])]
		if can_fit(grid, regions[region], presents):
			ans += 1
			print(ans)

	print(ans)





if __name__ == '__main__':
	main()