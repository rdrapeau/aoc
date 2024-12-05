import numpy as np

def main():
	paired_locations = np.loadtxt('part_1.csv')
	unique, counts = np.unique(paired_locations[:, 1], return_counts=True)
	right_index = dict(zip(unique, counts))
	total = np.sum([right_index.get(num, 0) * num for num in paired_locations[:, 0]])

	# 24349736
	print(total)


if __name__ == '__main__':
	main()