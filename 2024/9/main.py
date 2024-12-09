
def reconstruct_disk(input_string):
	reconstructed_disk = []
	file_sizes = {}
	blank_sizes = {}
	id_num = -1
	for i in range(len(input_string)):
		item = input_string[i]
		if i % 2 == 0:
			file_sizes[len(reconstructed_disk)] = item
			id_num += 1
		else:
			blank_sizes[len(reconstructed_disk)] = item

		for j in range(item):
			reconstructed_disk.append('.' if i % 2 == 1 else id_num)

	return reconstructed_disk, file_sizes, blank_sizes


def compact_disk_part_1(reconstructed_disk, file_sizes, blank_sizes):
	left = 0
	right = len(reconstructed_disk) - 1
	while left < right:
		if reconstructed_disk[left] != '.':
			left += 1
		elif reconstructed_disk[right] == '.':
			right -= 1
		elif reconstructed_disk[right] != '.':
			reconstructed_disk[left], reconstructed_disk[right] = reconstructed_disk[right], reconstructed_disk[left]
			left += 1
			right -= 1


def compact_disk_part_2(reconstructed_disk, file_sizes, blank_sizes):
	index_with_file_size = sorted([(i, file_sizes[i]) for i in file_sizes], reverse=True)
	index_with_blank_size = sorted([(i, blank_sizes[i]) for i in blank_sizes])

	for i in range(len(index_with_file_size)):
		(index, size) = index_with_file_size[i]
		for j in range(len(index_with_blank_size)):
			blank_index, blank_size = index_with_blank_size[j]
			if blank_index >= index:
				break

			if blank_size >= size:
				for k in range(size):
					reconstructed_disk[blank_index + k], reconstructed_disk[index + k] = reconstructed_disk[index + k], reconstructed_disk[blank_index + k]

				index_with_blank_size[j] = (blank_index + size, blank_size - size)
				break


def main():
	with open('input.txt') as f:
		input_string = [int(i) for i in f.read().strip()]

	reconstructed_disk, file_sizes, blank_sizes = reconstruct_disk(input_string)

	# compact_disk_part_1(reconstructed_disk, file_sizes, blank_sizes)
	compact_disk_part_2(reconstructed_disk, file_sizes, blank_sizes)
	print(sum(i * num for i, num in enumerate(reconstructed_disk) if num != '.'))


if __name__ == '__main__':
	main()