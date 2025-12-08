import scipy, math


def main():
	with open('input.txt') as f:
		data = f.readlines()
		coords = [tuple([int(x) for x in line.strip().split(',')]) for line in data]

		distances = [
			(
				(a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2,
				a,
				b
			) for a in coords for b in coords if a > b
		]
		distances.sort(reverse=True)
		dset = scipy.cluster.hierarchy.DisjointSet(coords)

		i = 0
		while len(dset.subsets()) > 1:
			if i == 1000:
				print(math.prod(sorted([len(s) for s in dset.subsets()])[-3:]))

			_, a, b = distances.pop()
			dset.merge(a, b)
			i += 1

		print(a[0] * b[0])


if __name__ == '__main__':
	main()