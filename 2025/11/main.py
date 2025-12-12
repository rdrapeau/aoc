import functools

def main():
	with open('input.txt') as f:
		data = f.readlines()
		g = {'out': []}
		for line in data:
			parsed = line.split(':')
			g[parsed[0].strip()] = parsed[1].strip().split()

	@functools.cache
	def count_paths(start, end, seen_fft, seen_dac):
		if start == end and seen_fft and seen_dac:
			return 1

		return sum(
			count_paths(
				neighbor,
				end,
				seen_fft or start == 'fft',
				seen_dac or start == 'dac'
			)
			for neighbor in g[start]
		)

	print(count_paths('you', 'out', True, True))
	print(count_paths('svr', 'out', False, False))


if __name__ == '__main__':
	main()