def is_valid(grid, p1, p2):
	max_c = max(p1[1], p2[1])
	min_c = min(p1[1], p2[1])
	max_r = max(p1[0], p2[0])
	min_r = min(p1[0], p2[0])

	for row in range(min_r, max_r + 1):
		for col in range(min_c, max_c + 1):
			if grid[row][col] == 0:
				return False

	return True


def main():
	with open('small_input.txt') as f:
		data = f.readlines()
		data = [line.strip().split(',') for line in data]
		data = [tuple([int(x[0]), int(x[1])]) for x in data]

		mh = max([x[0] for x in data]) + 1
		mw = max([x[1] for x in data]) + 1

		grid = [[0] * mw for _ in range(mh)]

		for i, (row, col) in enumerate(data):
			if i + 1 == len(data):
				next_row, next_col = data[0]
			else:
				next_row, next_col = data[i + 1]

			grid[row][col] = 1
			grid[next_row][next_col] = 1

			if row == next_row:
				for c in range(min(col, next_col) + 1, max(col, next_col)):
					grid[row][c] = 1
			elif col == next_col:
				for r in range(min(row, next_row) + 1, max(row, next_row)):
					grid[r][col] = 1
			else:
				raise 'Error'

		fill_point = (4, 4)
		q = [fill_point]
		while len(q) >= 1:
			p = q.pop()
			grid[p[0]][p[1]] = 1

			for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				r = p[0] + dr
				c = p[1] + dc
				if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r]) and grid[r][c] == 0:
					q.append((r, c))

		areas = {}
		for p1 in data:
			for p2 in data:
				if p1 != p2 and is_valid(grid, p1, p2):
					height = abs(p1[0] - p2[0]) + 1
					width = abs(p1[1] - p2[1]) + 1
					areas[(p1, p2)] = height * width

		print(max(areas.values()))


if __name__ == '__main__':
	main()