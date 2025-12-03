import functools

@functools.cache
def process_row(row, index, remaining):
	if remaining == 0 or index >= len(row):
		return ""

	a = row[index] + process_row(row, index + 1, remaining - 1)
	b = process_row(row, index + 1, remaining)

	return max((len(a), a), (len(b), b))[1]


# Takes about ~10 mins
def main():
	with open('input.txt') as f:
		data = f.readlines()
		
		ans = 0
		for row in data:
			ans += int(process_row(row.strip(), 0, 12))
			print(ans)

	print(ans)


if __name__ == '__main__':
	main()