def is_valid(num):
	for i in range(1, len(num)):
		current = num[:i]
		repeat = current
		while len(repeat) < len(num):
			repeat += current
			if repeat == num:
				return False

	return True


def main():
	with open('input.txt') as f:
		data = f.read()
		data = data.split(',')

	ans = 0
	for item in data:
		nums = item.split('-')

		for num in range(int(nums[0]), int(nums[1]) + 1):
			if not is_valid(str(num)):
				ans += num

	print(ans)


if __name__ == '__main__':
	main()