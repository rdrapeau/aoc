def main():
	with open('input.txt') as f:
		data = f.read().split('\n')
		rows = [line for line in data[:-1]]
		operands = data[-1]
		ans = 0

		for i in range(len(operands)):
			if operands[i] not in ('+', '*'):
				continue

			nums = []
			j = i
			cur_num = None
			while j < len(operands) and cur_num != '':
				cur_num = ''.join(row[j].strip() for row in rows)
				if cur_num != '':
					nums.append(cur_num)

				j += 1

			ans += eval(operands[i].join(nums))

		print(ans)


if __name__ == '__main__':
	main()