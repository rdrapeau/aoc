import heapq

def has_path(size, obstacles):
	obstacles = set(obstacles)
	start = (0, 0)
	lowest_cost = {start: 0}
	queue = [(0, start)]
	while len(queue) != 0:
		cost, pos = heapq.heappop(queue)
		if pos == (size - 1, size - 1):
			return True, cost

		for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
			new_pos = (d[0] + pos[0], d[1] + pos[1])
			if new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[0] < size and new_pos[1] < size and new_pos not in obstacles and lowest_cost.get(new_pos, float('inf')) > cost + 1:
				heapq.heappush(queue, (cost + 1, new_pos))
				lowest_cost[new_pos] = cost + 1

	return False, None


def binary_search(size, obstacles, left, right):
	lowest = float('inf')
	while left < right:
		mid = (left + right) // 2
		if has_path(size, obstacles[:mid + 1])[0]:
			left = mid + 1
		else:
			right = mid
			lowest = mid

	return lowest


def main():
	with open('input.txt') as f:
		data = f.readlines()
		data = [[int(a) for a in x.split(',')] for x in data]
		obstacles = [(b,a) for a,b in data]

	size = 71
	print(has_path(size, obstacles[:1024]))

	i = binary_search(size, obstacles, 0, len(obstacles))
	print(i, data[i])

if __name__ == '__main__':
	main()