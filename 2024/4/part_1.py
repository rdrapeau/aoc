WORD = 'XMAS'
WORD_LENGTH = len(WORD)

VALID_DIRECTIONS = [
	(0, 1),   # Right
	(0, -1),  # Left
	(1, 0),   # Down
	(-1, 0),  # Up
	(1, 1),   # Diagonal Down-Right
	(1, -1),  # Diagonal Down-Left
	(-1, 1),  # Diagonal Up-Right
	(-1, -1)  # Diagonal Up-Left
]

def check_for_word(data, row, col, row_change, col_change):
	for i in range(WORD_LENGTH):
		new_row = row + i * row_change
		new_col = col + i * col_change
		if (
			new_row < 0
			or new_col < 0
			or new_row >= len(data)
			or new_col >= len(data[0])
			or data[new_row][new_col] != WORD[i]
		):
			return False

	return True


def find_all_occurences(data, row, col):
	if data[row][col] != WORD[0]:
		return 0

	found_count = 0
	for row_change, col_change in VALID_DIRECTIONS:
		found_count += 1 if check_for_word(data, row, col, row_change, col_change) else 0

	return found_count


def main():
	with open('input.txt') as f:
		data = [[c for c in l.strip()] for l in f.readlines()]

	running_sum = 0
	for row in range(len(data)):
		for col in range(len(data[0])):
			running_sum += find_all_occurences(data, row, col)

	print(running_sum)


if __name__ == '__main__':
	main()