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


def dfs(input, position, path_so_far):
	row, col = position
	if input[row][col] == 9:
		return set([(row, col)]), 1

	ends, rating = set(), 0
	neighbors = find_neighbors(input, position)
	for neighbor in neighbors:
		if neighbor not in path_so_far:
			path_so_far.add(neighbor)
			new_ends, new_rating = dfs(input, neighbor, path_so_far)
			rating += new_rating
			ends = ends.union(new_ends)
			path_so_far.remove(neighbor)

	return ends, rating


def main():
	with open('input.txt') as f:
		input = [map(int, list(line.strip())) for line in f.readlines()]

	starting_pos = [(row, col) for row, row_arr in enumerate(input) for col, value in enumerate(row_arr) if value == 0]

	p1, p2 = 0, 0
	for start in starting_pos:
		ends, rating = dfs(input, start, set([start]))
		p1 += len(ends)
		p2 += rating

	print(p1)
	print(p2)

if __name__ == '__main__':
	main()