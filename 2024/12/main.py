directions = [
	(1, 0),
	(0, 1),
	(-1, 0),
	(0, -1)
]

def find_neighbors(row, col):
	neighbors = []
	for direction in directions:
		dr, dc = direction
		new_row, new_col = row + dr, col + dc
		neighbors.append((new_row, new_col))

	return neighbors


def flood_fill(garden, row, col):
	queue = [(row, col)]
	garden_patch = set([(row, col)])
	perimeter_segments = set()
	while len(queue) > 0:
		(row, col) = queue.pop()
		for neighbor in find_neighbors(row, col):
			if (
				neighbor[1] >= 0 
				and neighbor[0] >= 0 
				and neighbor[0] < len(garden) 
				and neighbor[1] < len(garden[0]) 
				and garden[neighbor[0]][neighbor[1]] == garden[row][col]
			):
				if neighbor not in garden_patch:
					garden_patch.add(neighbor)
					queue.append(neighbor)
			else:
				perimeter_segments.add(((row, col), neighbor))

	segments = set()
	for (start, end) in perimeter_segments:
		keep = True
		for dr, dc in [(1, 0), (0, 1)]:
			n_start = (start[0] + dr, start[1] + dc)
			n_end = (end[0] + dr, end[1] + dc)
			if (n_start, n_end) in perimeter_segments:
				keep = False
		
		if keep:
			segments.add((start, end))

	return garden_patch, len(perimeter_segments), len(segments)


def main():
	with open('input.txt') as f:
		garden = [list(line.strip()) for line in f.readlines()]

	processed = set()
	p1, p2 = 0, 0
	for row in range(len(garden)):
		for col in range(len(garden[0])):
			if (row, col) in processed:
				continue

			patch, perimiter, num_sides = flood_fill(garden, row, col)
			p1 += len(patch) * perimiter
			p2 += len(patch) * num_sides
			processed = processed.union(patch)

	print(p1, p2)

if __name__ == '__main__':
	main()
