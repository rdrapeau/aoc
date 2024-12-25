with open('input.txt') as f:
	data = f.read().split('\n\n')
	locks = []
	keys = []

	for entry in data:
		entry_parsed = entry.split('\n')
		is_lock = all(x == '#' for x in entry_parsed[0])
		entry_counts = []
		for col in range(len(entry_parsed[0])):
			col_c = 0
			for row in range(len(entry_parsed)):
				if entry_parsed[row][col] == '#':
					col_c += 1

			entry_counts.append(col_c - 1)

		if is_lock:
			locks.append(entry_counts)
		else:
			keys.append(entry_counts)

p1 = 0
for lock in locks:
	for key in keys:
		fits = True
		for i in range(len(lock)):
			if lock[i] + key[i] > 5:
				fits = False

		if fits:
			p1 += 1

print(p1)

