import numpy as np

def main():
	paired_locations = np.loadtxt('part_1.csv')
	sorted_locations = np.sort(paired_locations, axis=0)
	total_difference = np.sum(np.abs(sorted_locations[:, 0] - sorted_locations[:, 1]))

	# 1189304
	print(total_difference)


if __name__ == '__main__':
	main()