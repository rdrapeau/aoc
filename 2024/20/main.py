import heapq


directions = [
	(1, 0), (-1, 0), (0, 1), (0, -1)
]

BEST_COST = 9320


def has_path(grid, start, end):
	lowest_cost = {start: 0}
	queue = [(0, 0, start, [])]

	while len(queue) != 0:
		h_cost, cost, pos, path_so_far = heapq.heappop(queue)
		if pos == end:
			return cost, path_so_far

		if cost + 1 > BEST_COST:
			continue

		for d in directions:
			new_pos = (d[0] + pos[0], d[1] + pos[1])
			if new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[0] < len(grid) and new_pos[1] < len(grid[0]) and grid[new_pos[0]][new_pos[1]] != '#' and lowest_cost.get(new_pos, float('inf')) > cost + 1:
				heapq.heappush(queue, (cost + 1 + abs(new_pos[0] - end[0]) + abs(new_pos[1] - end[1]), cost + 1, new_pos, path_so_far + [new_pos]))
				lowest_cost[new_pos] = cost + 1

	return None, None


with open('input.txt') as f:
	data = f.read()
	grid = [list(x) for x in data.split('\n')]

	rows = len(grid)
	cols = len(grid[0])
	for row in range(rows):
		for col in range(cols):
			if grid[row][col] == 'S':
				start = (row, col)
			elif grid[row][col] == 'E':
				end = (row, col)
			else:
				continue

			grid[row][col] = '.'

	# cost, _ = has_path(grid, start, end)
	# print(cost)
	
	ghosts = set()
	for row in range(1, rows - 1):
		for col in range(1, cols - 1):
			if grid[row][col] != '#':
				continue

			for d in directions:
				new_pos = (row + d[0], col + d[1])
				if new_pos == rows or new_pos == 0 or col == cols or col == 0:
					continue

				if grid[new_pos[0]][new_pos[1]] == '#':
					continue

				ghosts.add(((row, col), new_pos))

	ans = 0
	# cost_saved = {}
	for i, ghost in enumerate(ghosts):
		print(i, len(ghosts))
		original_1, original_2 = grid[ghost[0][0]][ghost[0][1]], grid[ghost[1][0]][ghost[1][1]]
		grid[ghost[0][0]][ghost[0][1]], grid[ghost[1][0]][ghost[1][1]] = '.', original_2
		cost, path = has_path(grid, start, end)

		if cost is not None and cost <= BEST_COST and ghost[0] in path and ghost[1] in path and path.index(ghost[0]) < path.index(ghost[1]):
			ans += 1
			# cost_saved[BEST_COST - cost] = cost_saved.get(BEST_COST - cost, 0) + 1

		grid[ghost[0][0]][ghost[0][1]], grid[ghost[1][0]][ghost[1][1]] = original_1, original_2

	print(ans)
	print(cost_saved)
