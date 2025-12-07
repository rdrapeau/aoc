import functools	

def main():
	with open('input.txt') as f:
		data = f.readlines()
		grid = [list(line.strip()) for line in data]

		@functools.cache
		def calculate_paths(row, col):
			if row == len(grid):
				return 1

			if grid[row][col] == '.':
				return calculate_paths(row + 1, col)
			
			return calculate_paths(row + 1, col - 1) + calculate_paths(row + 1, col + 1)


		ans = calculate_paths(1, grid[0].index('S'))
		print(ans)


if __name__ == '__main__':
	main()