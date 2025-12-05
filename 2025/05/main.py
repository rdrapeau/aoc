def main():
	with open('input.txt') as f:
		data = f.read().split('\n\n')
		ranges = [[int(b) for b in a.split('-')] for a in data[0].split('\n')]
		produce = data[1].split('\n')

		ranges.sort()
		combined = []
		i = 0
		while i < len(ranges):
			start, cur_end = ranges[i]
			j = i + 1
			while j < len(ranges) and ranges[j][0] <= cur_end:
				cur_end = max(cur_end, ranges[j][1])
				j += 1

			combined.append((start, cur_end))
			i = j

		ans = 0
		for a, b in combined:
			ans += b - a + 1

		print(ans)


if __name__ == '__main__':
	main()