from collections import deque
from itertools import permutations


def bfs(edges, start, end):
	seen = {}
	state = (0, start, [])
	q = deque([state])
	
	lowest_cost = None
	all_paths = set([])
	while len(q) != 0:
		cost, pos, path = q.popleft()
		if pos == end and (lowest_cost is None or cost == lowest_cost):
			all_paths.add(''.join(path))
			lowest_cost = cost
			continue

		for move, neighbor in edges[pos]:
			if neighbor not in seen or seen[neighbor] >= cost + 1:
				state = (cost + 1, neighbor, path + [move])
				q.append(state)
				seen[neighbor] = cost + 1

	return all_paths


cache = {}
def get_length(moves, all_possible_paths, cur_depth, max_limit):
	c_key = (moves, cur_depth)
	if c_key in cache:
		return cache[c_key]

	length = 0
	cur_pos = 'A' if cur_depth == 0 else 'a'
	for move in moves:
		possible_moves = all_possible_paths[cur_pos][move]
		if cur_depth == max_limit:
			length += len(possible_moves[0])
		else:
			length += min([get_length(possible_move, all_possible_paths, cur_depth + 1, max_limit) for possible_move in possible_moves])

		cur_pos = move

	cache[c_key] = length
	return length


with open('input.txt') as f:
	codes = [x.strip() for x in f.readlines()]

num_pad = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A']
dir_pad = ['^', '<', '>', 'v', 'a']

edges = {
	'0': [('^', '2'), ('>', 'A')],
	'1': [('^', '4'), ('>', '2')],
	'2': [('^', '5'), ('>', '3'), ('v', '0'), ('<', '1')],
	'3': [('^', '6'), ('<', '2'), ('v', 'A')],
	'4': [('^', '7'), ('>', '5'), ('v', '1')],
	'5': [('^', '8'), ('>', '6'), ('v', '2'), ('<', '4')],
	'6': [('^', '9'), ('<', '5'), ('v', '3')],
	'7': [('>', '8'), ('v', '4')],
	'8': [('>', '9'), ('v', '5'), ('<', '7')],
	'9': [('v', '6'), ('<', '8')],
	'A': [('^', '3'), ('<', '0')],
	'^': [('>', 'a'), ('v', 'v')],
	'v': [('<', '<'), ('>', '>'), ('^', '^')],
	'>': [('<', 'v'), ('^', 'a')],
	'<': [('>', 'v')],
	'a': [('v', '>'), ('<', '^')]
}

all_possible_paths = {}
for a in num_pad:
	all_possible_paths[a] = {}
	for b in num_pad:
		if a == b:
			all_possible_paths[a][b] = ['a']
		else:
			all_possible_paths[a][b] = [x + 'a' for x in bfs(edges, a, b)]

for a in dir_pad:
	all_possible_paths[a] = {}
	for b in dir_pad:
		if a == b:
			all_possible_paths[a][b] = ['a']
		else:
			all_possible_paths[a][b] = [x + 'a' for x in bfs(edges, a, b)]

res = 0
for code in codes:
	move_length = get_length(code, all_possible_paths, 0, 25)
	res += int(code[:3]) * move_length

print(res)