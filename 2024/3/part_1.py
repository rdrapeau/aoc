import re

def main():
	with open('input.txt') as f:
		data = f.read()

	entries = re.finditer("(do\(\)|mul\((\d{1,3}),(\d{1,3})\)|don't\(\))", data)
	running_sum = 0
	is_on = True
	for entry in entries:
		groups = entry.groups()
		if groups[0] == "do()" or groups[0] == "don't()":
			is_on = groups[0] == "do()"
		elif is_on:
			running_sum += int(groups[1]) * int(groups[2])

	# Part 1: 173785482
	# Part 2: 83158140
	print(running_sum)


if __name__ == '__main__':
	main()