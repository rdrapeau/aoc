from collections import deque


def validate_update(graph, update, with_correction=False):
	for j in range(len(update) - 1, 0, -1):
		cur = update[j]
		constraints = graph[cur]
		for i in range(0, j):
			next = update[i]
			if next in constraints:
				if with_correction:
					update[j], update[i] = update[i], update[j]
					return validate_update(graph, update, with_correction=True)
				else:
					return False

	return True if not with_correction else update


# def filter_graph_to_nodes_in_update(graph, update):
# 	filtered_graph = {}
# 	in_degrees = {node: 0 for node in update}
# 	for node in update:
# 		filtered_graph[node] = []
# 		for neighbor in graph[node]:
# 			if neighbor in update:
# 				filtered_graph[node].append(neighbor)
# 				in_degrees[neighbor] += 1

# 	return filtered_graph, in_degrees


# def correct_update(graph, update):
# 	filtered_graph, in_degrees = filter_graph_to_nodes_in_update(graph, update)
# 	queue = deque([node for node in in_degrees if in_degrees[node] == 0])

# 	corrected_update = []
# 	while len(queue) > 0:
# 		cur = queue.popleft()
# 		corrected_update.append(cur)

# 		for node in filtered_graph[cur]:
# 			in_degrees[node] -= 1
# 			if in_degrees[node] == 0:
# 				queue.append(node)

# 	return corrected_update


def validate_updates(graph, updates):
	running_total = 0
	new_update_running_total = 0
	invalid_updates = []

	for update in updates:
		is_valid = validate_update(graph, update)
		if is_valid:
			running_total += update[len(update) // 2]
		else:
			new_update = validate_update(graph, update, with_correction=True)
			new_update_running_total += new_update[len(new_update) // 2]

	return running_total, new_update_running_total


def main():
	with open('input.txt') as f:
		data = f.readlines()

	graph = {}
	updates = []
	for row in data:
		if '|' in row:
			prev, cur = row.split('|')
			prev, cur = int(prev), int(cur)

			if prev not in graph:
				graph[prev] = []
			if cur not in graph:
				graph[cur] = []

			graph[prev].append(cur)
		elif ',' in row:
			updates.append([int(x) for x in row.split(',')])
		else:
			continue

	print(validate_updates(graph, updates))

if __name__ == '__main__':
	main()