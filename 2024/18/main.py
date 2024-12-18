import heapq

directions = [
	(1, 0), (0, 1), (-1, 0), (0, -1)
]

def has_path(grid, size):
	start = (0, 0)
	lowest_cost = {start: 0}
	queue = [(0, start)]
	while len(queue) != 0:
		cost, pos = heapq.heappop(queue)
		if pos == (size - 1, size - 1):
			return True, cost

		for d in directions:
			new_pos = (d[0] + pos[0], d[1] + pos[1])
			if new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[0] < size and new_pos[1] < size and grid[new_pos[0]][new_pos[1]] != '#' and lowest_cost.get(new_pos, float('inf')) > cost + 1:
				heapq.heappush(queue, (cost + 1, new_pos))
				lowest_cost[new_pos] = cost + 1

	return False, None


def main():
	with open('input.txt') as f:
		data = f.readlines()
		data = [[int(a) for a in x.split(',')] for x in data]
		data = [(b,a) for a,b in data]

	size = 71
	grid = [['.' for _ in range(size)] for _ in range(size)]
	for row,col in data[:1024]:
		grid[row][col] = '#'

	print(has_path(grid, size)[1])

	for row,col in data[1024:]:
		grid[row][col] = '#'
		if not has_path(grid, size)[0]:
			print(col,row)
			break


if __name__ == '__main__':
	main()