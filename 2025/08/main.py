def dist(x, y):
	return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2


def main():
	with open('input.txt') as f:
		data = f.readlines()
		coords = [tuple([int(x) for x in line.strip().split(',')]) for line in data]

		distances = sorted([(dist(a, b), a, b) for i, a in enumerate(coords) for j, b in enumerate(coords) if i > j])
		circuits = {x:i for i, x in enumerate(coords)}

		for i in range(len(distances)):
			_, a, b = distances[i]

			new_min = min([circuits[a], circuits[b]])
			old = [circuits[a], circuits[b]]
			for node in circuits:
				if circuits[node] in old:
					circuits[node] = new_min

			if min(circuits.values()) == max(circuits.values()):
				print(a[0] * b[0])
				break


if __name__ == '__main__':
	main()