import z3
from collections import deque
import re

def solve(target, switches):
	start = (0, target.replace('#', '.'))
	q = deque()
	q.append(start)
	seen = set()
	while len(q) > 0:
		cost, machine = q.popleft()
		if machine == target:
			return cost

		for option in switches:
			new_machine = list(machine)
			for flip in option:
				new_machine[flip] = '.' if new_machine[flip] == '#' else '#'

			new_machine = ''.join(new_machine)
			if new_machine not in seen:
				q.append((cost + 1, new_machine))
				seen.add(new_machine)

	raise Exception('impossible')


def solve_z3(target, switches):
    opt = z3.Optimize()
    max_presses = max(target)
    num_switches = len(switches)
    presses = [z3.Int(f"switch_{i}") for i in range(num_switches)]
    for j in range(num_switches):
        opt.add(presses[j] >= 0)
        opt.add(presses[j] <= max_presses)

    for joltage_index in range(len(target)):
        num_presses = [presses[j] for j, switch in enumerate(switches) if joltage_index in switch]
        opt.add(z3.Sum(num_presses) == target[joltage_index])

    total_presses = z3.Sum(presses)
    opt.minimize(total_presses)
    opt.check()
    model = opt.model()
    sol = [model[presses[i]].as_long() for i in range(num_switches)]
    return sum(sol)


def main():
	with open('input.txt') as f:
		data = f.readlines()
		all_machines = []
		all_switches = []
		all_joltages = []
		for line in data:
			pattern = r"\[(.*)\] (.*) \{(.*)\}"
			m = re.search(pattern, line)
			all_machines.append(m.group(1))
			all_switches.append([[int(y) for y in x[1:-1].split(',')] for x in m.group(2).split()])
			all_joltages.append([int(x) for x in m.group(3).split(',')])

	ans_p1 = 0
	ans_p2 = 0
	for i in range(len(all_machines)):
		ans_p1 += solve(all_machines[i], all_switches[i])
		ans_p2 += solve_z3(all_joltages[i], all_switches[i])

	print(ans_p1, ans_p2)


if __name__ == '__main__':
	main()