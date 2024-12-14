import re
from sympy import symbols, linsolve, Eq

A_COST = 3
B_COST = 1
PART_2 = 10000000000000

def solve_system(a, b, target):
	x_a, y_a = a
	x_b, y_b = b
	target_x, target_y = target

	num_a, num_b = symbols('num_a num_b')
	eq1 = Eq(x_a * num_a + x_b * num_b, target_x)
	eq2 = Eq(y_a * num_a + y_b * num_b, target_y)
	solutions = linsolve((eq1, eq2), (num_a, num_b))
	return next(iter(solutions))


def main():
	with open('input.txt') as f:
		input = [[tuple([int(y) for y in re.findall(r"(\d+)", x)]) for x in line.split('\n')] for line in f.read().strip().split('\n\n')]

	p1, p2 = 0, 0
	for i, (a, b, target) in enumerate(input):
		solution = solve_system(a, b, target)
		if int(solution[0]) == solution[0] and int(solution[1]) == solution[1]: 
			p1 += solution[0] * A_COST + solution[1] * B_COST

		solution = solve_system(a, b, (target[0] + PART_2, target[1] + PART_2))
		if int(solution[0]) == solution[0] and int(solution[1]) == solution[1]: 
			p2 += solution[0] * A_COST + solution[1] * B_COST

	print(p1)
	print(p2)


if __name__ == '__main__':
	main()
