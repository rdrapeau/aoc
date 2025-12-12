import functools, heapq

# @functools.cache

DIRS = [
	(1, 0),
	(-1, 0),
	(0, 1),
	(0, -1),
	(1, 1),
	(1, -1),
	(-1, 1),
	(-1, -1)
]

def check_adj(grid, row, col):
	count = 0
	for d in DIRS:
		drow = row + d[0]
		dcol = col + d[1]

		if drow >=0 and dcol >= 0 and drow < len(grid) and dcol < len(grid[drow]):
			if grid[drow][dcol] == '@':
				count += 1

	return count


def dijkstra():
	start = None
	start_cost = 0

	target = None

	q = [(start_cost, start)]
	seen = set([start])

	while len(q) > 0:
		(cur, cur_cost) = heapq.heappop(q)
		if cur == target:
			return cur_cost

		# Generate neighbors and add to q with heapq.heappush(q, (cur_cost + x, next))
