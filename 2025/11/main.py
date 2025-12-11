import functools

def main():
	with open('input.txt') as f:
		data = f.readlines()
		g = {'out': []}
		for line in data:
			parsed = line.split(':')
			g[parsed[0].strip()] = parsed[1].strip().split()

	@functools.cache
	def count_paths(start, end):
		if start == end:
			return 1

		return sum(count_paths(neighbor, end) for neighbor in g[start])


	print(count_paths('you', 'out'))
	print(
		count_paths('svr', 'fft') * count_paths('fft', 'dac') * count_paths('dac', 'out')
		+ count_paths('svr', 'dac') * count_paths('dac', 'fft') * count_paths('fft', 'out')
	)


if __name__ == '__main__':
	main()