import functools

@functools.cache
def process_row(row, index, remaining):
	if remaining == 0 or index >= len(row):
		return ""

	a = row[index] + process_row(row, index + 1, remaining - 1)
	b = process_row(row, index + 1, remaining)

	a_num = int(a) if a != '' else 0
	b_num = int(b) if b != '' else 0

	return a if a_num > b_num else b


def main():
	with open('input.txt') as f:
		data = f.readlines()
		
		ans = 0
		for row in data:
			ans += int(process_row(row.strip(), 0, 12))

	print(ans)


if __name__ == '__main__':
	main()