# import math, numpy as np, functools, heapq
# from shapely.geometry import Polygon, box
from collections import deque
import re


def solve(target, switch, joltage):
	start = (0, target.replace('#', '.'))
	q = deque()
	q.append(start)
	while len(q) > 0:
		cost, machine = q.popleft()
		if machine == target:
			return cost

		for option in switch:
			new_machine = list(machine)
			for flip in option:
				new_machine[flip] = '.' if new_machine[flip] == '#' else '#'

			q.append((cost + 1, ''.join(new_machine)))

	return -10000


def solve_2(target, switch, target_joltage):
	start = (0, [0] * len(target))
	q = deque()
	q.append(start)
	seen = set()
	while len(q) > 0:
		cost, cur_levels = q.popleft()
		if cur_levels == target_joltage:
			return cost

		for option in switch:
			new_levels = list(cur_levels)
			for flip in option:
				new_levels[flip] += 1
			
			k = ''.join([str(x) for x in new_levels])
			if k not in seen:
				q.append((cost + 1, new_levels))
				seen.add(k)

	return -10000


def main():
	with open('input.txt') as f:
		data = f.readlines()
		machines = []
		switches = []
		joltages = []
		for line in data:
			pattern = r"\[(.*)\] (.*) \{(.*)\}"
			m = re.search(pattern, line)
			machines.append(m.group(1))
			switches.append([[int(y) for y in x[1:-1].split(',')] for x in m.group(2).split()])
			joltages.append([int(x) for x in m.group(3).split(',')])

	ans = 0
	for i in range(len(machines)):
		ans += solve_2(machines[i], switches[i], joltages[i])
		print(i)

	print(ans)


if __name__ == '__main__':
	main()