def division(register, combo, literal_operand):
	numerator = register['A']
	denominator = 2 ** combo
	register['A'] = int(numerator // denominator)


def bitwise_xor(register, combo, literal_operand):
	register['B'] = register['B'] ^ literal_operand


def bst(register, combo, literal_operand):
	register['B'] = combo % 8 


def jnz(register, combo, literal_operand):
	if register['A'] != 0:
		return 'jump', literal_operand


def bxc(register, combo, literal_operand):
	register['B'] = register['B'] ^ register['C']


def out(register, combo, literal_operand):
	return 'out', combo % 8


def bdv(register, combo, literal_operand):
	numerator = register['A']
	denominator = 2 ** combo
	register['B'] = int(numerator // denominator)


def cdv(register, combo, literal_operand):
	numerator = register['A']
	denominator = 2 ** combo
	register['C'] = int(numerator // denominator)


OPCODE_FNS = [
	division,
	bitwise_xor,
	bst,
	jnz,
	bxc,
	out,
	bdv,
	cdv
]


def run_program(program, register):
	output = []
	i = 0
	while i < len(program) - 1:
		opcode = program[i]
		literal_operand = program[i + 1]
		if literal_operand <= 3:
			combo = literal_operand
		elif literal_operand == 4:
			combo = register['A']
		elif literal_operand == 5:
			combo = register['B']
		elif literal_operand == 6:
			combo = register['C']
		elif literal_operand == 7:
			combo = literal_operand

		result = OPCODE_FNS[opcode](register, combo, literal_operand)
		did_jump = False
		if result is not None:
			instruction, value = result
			if instruction == 'jump':
				i = value
				did_jump = True
			elif instruction == 'out':
				output.append(value)

		if not did_jump:
			i += 2

	return output


def find_program(program, index, a_value):
	# The program right shifts by 3 bits, which is essentially a divided by 8 every output. Once we find a value,
	# we simply multiply by 8 and then check for the next number until we've checked every output. Do this in 
	# reverse since the last value will be produced by a number < 8.
	if index == -1:
		return a_value

	target_program = program[index:]
	for i in range(8):
		next_a_value = a_value * 8 + i
		if run_program(program, {'A': next_a_value, 'B': 0, 'C': 0}) == target_program:
			result = find_program(program, index - 1, next_a_value)
			if result is not None:
				return result

	return None


def main():
	with open('input.txt') as f:
		data = f.read()
		parts = data.split('\n\n')

		register = {}
		for line in parts[0].split('\n'):
			register[line[9]] = int(line[12:])

		program = [int(x) for x in parts[1][8:].split(',')]

	p1_output = run_program(program, register)
	print(','.join([str(x) for x in p1_output]))
	print(find_program(program, len(program) - 1, 0))


if __name__ == '__main__':
	main()