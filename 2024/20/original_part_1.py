import heapq


directions = [
	(1, 0), (-1, 0), (0, 1), (0, -1)
]

BEST_COST = 84


def has_path(grid, start, end):
	state = (start, 2, None, None)
	lowest_cost = {state[:2]: 0}
	queue = [(0, state)]

	cheats = set()
	while len(queue) != 0:
		cost, state = heapq.heappop(queue)
		pos, ghost_remaining, g1, g2 = state
		assert(ghost_remaining > 0 or (g1 is not None and g2 is not None))

		if pos == end and cost <= BEST_COST - 0:
			cheats.add((g1, g2))
			print(cheats)
			continue


		for d in directions:
			new_pos = (d[0] + pos[0], d[1] + pos[1])
			if new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[0] < len(grid) and new_pos[1] < len(grid[0]):
				if ghost_remaining == 1:
					g2 = new_pos

				if grid[new_pos[0]][new_pos[1]] == '#':
					if ghost_remaining <= 0:
						continue
					elif ghost_remaining == 2:
						g1 = new_pos

					new_state = (new_pos, ghost_remaining - 1, g1, g2)
				else:
					new_state = (new_pos, ghost_remaining if ghost_remaining == 2 else ghost_remaining - 1, g1, g2)
				
				if lowest_cost.get(new_state[:2], float('inf')) >= cost + 1:
					heapq.heappush(queue, (cost + 1, new_state))
					lowest_cost[new_state[:2]] = cost + 1

	return cheats


with open('small_input.txt') as f:
	data = f.read()
	data = [list(x) for x in data.split('\n')]

	rows = len(data)
	cols = len(data[0])
	for row in range(rows):
		for col in range(cols):
			if data[row][col] == 'S':
				start = (row, col)
			elif data[row][col] == 'E':
				end = (row, col)

	print(has_path(data, start, end))


