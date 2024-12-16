import heapq


DIRECTIONS = {
	'E': (0, 1, ['N', 'S']),
	'W': (0, -1, ['N', 'S']),
	'N': (-1, 0, ['W', 'E']),
	'S': (1, 0, ['W', 'E'])
}

ROTATE_SCORE = 1000
MOVE_SCORE = 1


def astar(grid, start, end):
	to_explore = [start]
	lowest_cost = {}
	best_path_nodes = set()
	best_cost = None
	while len(to_explore) != 0:
		cur_cost, position, direction, path_so_far = heapq.heappop(to_explore)
		if position == end:
			if best_cost is None:
				best_cost = cur_cost

			if cur_cost == best_cost:
				best_path_nodes = best_path_nodes.union(path_so_far)

			continue

		next_direction = DIRECTIONS[direction]
		move_position = (
			cur_cost + MOVE_SCORE,
			(position[0] + next_direction[0], position[1] + next_direction[1]),
			direction,
			path_so_far + [(position[0] + next_direction[0], position[1] + next_direction[1])]
		)
		would_hit_wall = grid[move_position[1][0]][move_position[1][1]] == '#'
		direction_positions = [
			(
				cur_cost + ROTATE_SCORE,
				position,
				DIRECTIONS[direction][2][0],
				path_so_far
			),
			(
				cur_cost + ROTATE_SCORE,
				position,
				DIRECTIONS[direction][2][1],
				path_so_far
			)
		]

		possible_positions = [move_position] + direction_positions if not would_hit_wall else direction_positions
		for next_position in possible_positions:
			if (next_position[1], next_position[2]) in lowest_cost and lowest_cost[(next_position[1], next_position[2])] < next_position[0]:
				continue

			lowest_cost[(next_position[1], next_position[2])] = next_position[0]
			heapq.heappush(to_explore, next_position)

	return best_path_nodes, best_cost


def main():
	with open('input.txt') as f:
		data = f.read()
		grid = [list(line.strip()) for line in data.split('\n')]


	num_rows = len(grid)
	num_cols = len(grid[0])

	position = None
	end_position = None
	for row in range(num_rows):
		for col in range(num_cols):
			if grid[row][col] == 'S':
				position = (0, (row, col), 'E', [(row, col)])
			elif grid[row][col] == 'E':
				end_position = (row, col)


	best_path, cost = astar(grid, position, end_position)
	print(cost)
	print(len(best_path))


if __name__ == '__main__':
	main()