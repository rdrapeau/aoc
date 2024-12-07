def eval_equation(total, right_side):
	if len(right_side) == 1:
		return right_side[0] == total

	return (
		eval_equation(total, [right_side[0] + right_side[1]] + right_side[2:])
		or eval_equation(total, [right_side[0] * right_side[1]] + right_side[2:])
		or eval_equation(total, [int(str(right_side[0]) + str(right_side[1]))] + right_side[2:])
	)


def main():
	with open('input.txt') as f:
		data = [line.strip().split(':') for line in f.readlines()]
		equations = [(int(line[0]), [int(x) for x in line[1].split()]) for line in data]

	running_total = sum(equation[0] for equation in equations if eval_equation(equation[0], equation[1]))
	print(running_total)


if __name__ == '__main__':
	main()