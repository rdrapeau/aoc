
directions = [
	(1, 0),
	(0, 1),
	(-1, 0),
	(0, -1)
]


def find_neighbors(input, position):
	row, col = position
	height = input[row][col]

	neighbors = []
	for direction in directions:
		dr, dc = direction
		new_row, new_col = row + dr, col + dc
		if new_col >= 0 and new_row >= 0 and new_row < len(input) and new_col < len(input[0]) and input[new_row][new_col] == height + 1:
			neighbors.append((new_row, new_col))

	return neighbors


def walk_path(input, position):
	final_positions = set()
	queue = [position]
	seen = set([position])
	while len(queue) > 0:
		row, col = queue.pop()
		if input[row][col] == 9:
			final_positions.add((row, col))
		else:
			neighbors = find_neighbors(input, (row, col))
			for neighbor in neighbors:
				if neighbor not in seen:
					seen.add(neighbor)
					queue.append(neighbor)

	return final_positions


def dfs(input, position, destination, path_so_far):
	if position == destination:
		return 1

	score = 0
	neighbors = find_neighbors(input, position)
	for neighbor in neighbors:
		if neighbor not in path_so_far:
			path_so_far.add(neighbor)
			score += dfs(input, neighbor, destination, path_so_far)
			path_so_far.remove(neighbor)

	return score


def main():
	with open('input.txt') as f:
		input = [map(int, list(line.strip())) for line in f.readlines()]

	starting_pos = []
	for row in range(len(input)):
		for col in range(len(input[0])):
			if input[row][col] == 0:
				starting_pos.append((row, col))

	paths = {}
	for start in starting_pos:
		paths[start] = walk_path(input, start)

	score = 0

	for start in paths:
		for end in paths[start]:
			score += dfs(input, start, end, set([start]))

	print(score)

if __name__ == '__main__':
	main()