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


def main():
	with open('input.txt') as f:
		data = f.readlines()
		grid = [[c for c in line.strip()] for line in data]

		ans = 0
		prev = -1

		while prev != ans:
			prev = ans
			for row in range(len(grid)):
				for col in range(len(grid[0])):
					if grid[row][col] == '@' and check_adj(grid, row, col) < 4:
						grid[row][col] = 'X'
						ans += 1

	print(ans)


if __name__ == '__main__':
	main()