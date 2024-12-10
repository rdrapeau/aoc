import itertools
from collections import defaultdict

def in_bounds_and_add(grid, antinodes, row, col):
	if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]):
		antinodes.add((row, col))
		return True

	return False


def process_antenna_2(grid, antenna_positions):
	antinodes = set()
	for (row_1, col_1), (row_2, col_2) in itertools.combinations(antenna_positions, 2):
		row_distance = row_1 - row_2
		col_distance = col_1 - col_2

		keep_going = True
		i = 0
		while keep_going:
			res1 = in_bounds_and_add(grid, antinodes, row_1 + row_distance * i, col_1 + col_distance * i)
			res2 = in_bounds_and_add(grid, antinodes, row_2 - row_distance * i, col_2 - col_distance * i)
			keep_going = res1 or res2
			i += 1

	return antinodes


def process_antenna_1(grid, antenna_positions):
	antinodes = set()
	for (row_1, col_1), (row_2, col_2) in itertools.combinations(antenna_positions, 2):
		row_distance = row_1 - row_2
		col_distance = col_1 - col_2

		res1 = in_bounds_and_add(grid, antinodes, row_1 + row_distance, col_1 + col_distance)
		res2 = in_bounds_and_add(grid, antinodes, row_2 - row_distance, col_2 - col_distance)

	return antinodes


def find_antennas(grid):
	antennas = defaultdict(list)
	for i, row in enumerate(grid):
		for j, entry in enumerate(row):
			if entry != '.':
				antennas[entry].append((i, j))

	return antennas


def main():
	with open('input.txt') as f:
		grid = [[x for x in line.strip()] for line in f.readlines()]

	antennas = find_antennas(grid)

	all_antinodes = set.union(*[process_antenna_1(grid, antennas[antenna]) for antenna in antennas])
	print(len(all_antinodes))

	all_antinodes = set.union(*[process_antenna_2(grid, antennas[antenna]) for antenna in antennas])
	print(len(all_antinodes))


if __name__ == '__main__':
	main()