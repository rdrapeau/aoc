from functools import cache

@cache
def can_make(pattern):
	if len(pattern) == 0:
		return 1

	return sum(can_make(pattern[len(towel):]) for towel in towels if pattern.startswith(towel))


with open('input.txt') as f:
	data = f.read()
	data = data.split('\n\n')
	towels = data[0].split(', ')
	patterns = data[1].split('\n')

results = [can_make(pattern) for pattern in patterns]
print(sum(1 if x > 0 else 0 for x in results))
print(sum(results))
