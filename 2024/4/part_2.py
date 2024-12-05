ALLOWED = ['MS', 'SM']

def search_for_x_mas(data, row, col):
	if (
		data[row][col] != 'A'
		or row == 0
		or col == 0
		or row + 1 == len(data)
		or col + 1 == len(data[0])
	):
		return False

	upper_left = data[row - 1][col - 1]
	upper_right = data[row - 1][col + 1]
	lower_left = data[row + 1][col - 1]
	lower_right = data[row + 1][col + 1]

	if (
		(upper_left + lower_right) in ALLOWED
		and (upper_right + lower_left) in ALLOWED
	):
		return True


def main():
	with open('input.txt') as f:
		data = [[c for c in l.strip()] for l in f.readlines()]

	running_sum = 0
	for row in range(len(data)):
		for col in range(len(data[0])):
			running_sum += 1 if search_for_x_mas(data, row, col) else 0

	print(running_sum)


if __name__ == '__main__':
	main()