import scipy


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

		while len(dset.subsets()) > 1:
			_, a, b = distances.pop()
			dset.merge(a, b)

		print(a[0] * b[0])


if __name__ == '__main__':
	main()