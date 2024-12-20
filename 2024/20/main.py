from collections import deque
import copy

directions = [
	(1, 0), (-1, 0), (0, 1), (0, -1)
]

with open('input.txt') as f:
	grid = [list(x) for x in f.read().split('\n')]
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] == 'S':
				start = (row, col)
			elif grid[row][col] == 'E':
				end = (row, col)

	cost_index = {start: 0}
	q = deque([start])
	while len(q) != 0:
		pos = q.popleft()
		for d in directions:
			new_pos = (pos[0] + d[0], pos[1] + d[1])
			if grid[new_pos[0]][new_pos[1]] != '#' and new_pos not in cost_index:
				cost_index[new_pos] = cost_index[pos] + 1
				q.append(new_pos)

	p1, p2 = 0, 0
	for a in cost_index:
		for b in cost_index:
			distance_between = abs(a[0] - b[0]) + abs(a[1] - b[1])
			distance_saved = cost_index[a] - cost_index[b] - distance_between
			if distance_between <= 2 and distance_saved >= 100:
				p1 += 1
			
			if distance_between <= 20 and distance_saved >= 100:
				p2 += 1

	print(p1, p2)	