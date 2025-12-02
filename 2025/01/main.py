
def process_line(position, line):
	is_left = line[0] == 'L'
	num_zeros = 0
	for i in range(1, int(line[1:]) + 1):
		position += (-1 if is_left else 1)
		if position == 100:
			position = 0
		elif position == -1:
			position = 99

		if position == 0:
			num_zeros += 1

	return position, num_zeros


def main():
	with open('input.txt') as f:
		data = f.read()
		lines = data.split('\n')
	
	position = 50
	ans = 0
	for line in lines:
		position, num_crossed_zero = process_line(position, line)
		ans += num_crossed_zero

	print(ans)


if __name__ == '__main__':
	main()