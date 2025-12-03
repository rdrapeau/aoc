def process_row(row, index, selected, max_so_far):
	if len(selected) == 12:
		return max(max_so_far, int(''.join(selected)))

	for i in range(index, len(row)):
		selected.append(row[i])

		possible_max = int(''.join(selected + ['9'] * (12 - len(selected))))
		if possible_max > max_so_far:
			max_so_far = process_row(row, i + 1, selected, max_so_far)

		selected.pop()

	return max_so_far

# Takes about ~10 mins
def main():
	ans = 0

	with open('input.txt') as f:
		data = f.readlines()
		
		for row in data:
			ans += process_row(row.strip(), 0, [], -1)
			print(ans)

	print(ans)


if __name__ == '__main__':
	main()