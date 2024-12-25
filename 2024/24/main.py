import re
import copy
import itertools
from collections import defaultdict

def get_output(variables, variable_start):
	res = []
	for i in range(len(variables)):
		k = variable_start + str(i) if i >= 10 else variable_start + '0' + str(i)
		if k in variables:
			res.append(str(variables[k]))
		else:
			break

	binary = ''.join(res)[::-1]
	return int(binary, 2), binary


def simulate_wires(variables, eqns, swaps={}):
	has_more = True
	while has_more:
		has_more = False
		for v1, op, v2, v3 in parsed_eqns:
			output_variable = swaps.get(v3, v3)
			if v1 not in variables or v2 not in variables:
				has_more = True
				continue
			elif output_variable in variables:
				continue
			
			v1 = variables[v1]
			v2 = variables[v2]
			if op == 'OR':
				result = v1 | v2
			elif op == 'AND':
				result = v1 & v2
			elif op == 'XOR':
				result = v1 ^ v2

			variables[output_variable] = result


def num_bits_wrong(expected_z, z_bin):
	assert len(expected_z) == len(z_bin)
	num_bits_wrong = 0
	print('Expected:', expected_z)
	print('Found   :', z_bin)
	expected_z = expected_z[::-1]
	z_bin = z_bin[::-1]
	error_bits = []
	for i in range(len(expected_z)):
		if expected_z[i] != z_bin[i]:
			num_bits_wrong += 1
			bit = 'z' + (str(i) if i >= 10 else '0' + str(i))
			error_bits.append(bit)

	return num_bits_wrong


with open('input.txt') as f:
	data = f.read().split('\n\n')
	variables = {a[0]: int(a[1]) for a in [tuple(x.strip().split(': ')) for x in data[0].split('\n')]}
	original_variables = copy.deepcopy(variables)
	eqns = data[1].split('\n')
	parsed_eqns = []
	edges = defaultdict(list)
	inverse_edges = defaultdict(list)
	for eqn in eqns:
		m = re.search("(.*) (OR|XOR|AND) (.*) -> (.*)", eqn)
		v1, op, v2, v3 = m.group(1), m.group(2), m.group(3), m.group(4)
		edges[v1].append((v3, op))
		edges[v2].append((v3, op))
		inverse_edges[v3].append((v1, op))
		inverse_edges[v3].append((v2, op))
		parsed_eqns.append((v1, op, v2, v3))

# bad_nodes = set()
# for node in inverse_edges:
# 	if node.startswith('z'):
# 		upstream = inverse_edges[node]
# 		if node != 'z45' and (len(upstream) != 2 or upstream[0][1] != 'XOR' or upstream[1][1] != 'XOR'):
# 			bad_nodes.add(node)
# 			print(node)

# for node in edges:
# 	if not node.startswith('z'):
# 		downstreams = inverse_edges[node]
# 		if any(x[0].startswith('z') for x in downstreams):
# 			assert(len(downstreams) == 2)

# 		for downstream in downstreams:
# 			if downstream[0][0] not in ['x', 'y', 'z'] and downstream[1] == 'XOR':
# 				print(node, downstream)
# 				bad_nodes.add(node)

swaps = {
	'z06': 'fkp',
	'fkp': 'z06',

	'ngr': 'z11',
	'z11': 'ngr',

	'z31': 'mfm',
	'mfm': 'z31',

	'bpt': 'krj',
	'krj': 'bpt',
}

variables = copy.deepcopy(original_variables)
simulate_wires(variables, parsed_eqns, swaps=swaps)
x_dec, x_bin = get_output(variables, 'x')
y_dec, y_bin = get_output(variables, 'y')
z_dec, z_bin = get_output(variables, 'z')
expected_z = bin(x_dec + y_dec)[2:]
baseline = num_bits_wrong(expected_z, z_bin)
print(baseline)