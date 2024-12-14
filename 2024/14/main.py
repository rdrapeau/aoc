from PIL import Image, ImageDraw


def simulate_step(grid, cur_pos, velocity, num_rows, num_cols):
	velocity_row, velocity_col = velocity
	new_pos_row = (cur_pos[0] + velocity_row) % num_rows
	new_pos_col = (cur_pos[1] + velocity_col) % num_cols
	return (new_pos_row, new_pos_col)

def simulate_all_robots(grid, robot_index, num_rows, num_cols):
	for row in range(num_rows):
		for col in range(num_cols):
			cell_state = grid[(row, col)]
			to_remove = set()
			for robot_id in cell_state[1]:
				velocity, can_move = robot_index[robot_id]
				if not can_move or velocity == (0, 0):
					continue

				new_pos = simulate_step(grid, (row, col), velocity, num_rows, num_cols)

				cell_state[0] -= 1
				to_remove.add(robot_id)

				grid[new_pos][0] += 1
				grid[new_pos][1].add(robot_id)
				robot_index[robot_id] = (velocity, False)

			grid[(row, col)] = [cell_state[0], cell_state[1].difference(to_remove)]


def render_image(grid, num_rows, num_cols, iteration):
    image = Image.new("RGB", (num_cols, num_rows), "black")
    draw = ImageDraw.Draw(image)
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[(row, col)][0] != 0:
                draw.rectangle([(col, row), (col, row)], fill="white")

    image.save(str(iteration) + '.png')


def main():
	with open('input.txt') as f:
		input = [line.strip().split() for line in f.readlines()]

	robots = [tuple([tuple([int(y) for y in x.split('=')[1].split(',')][::-1]) for x in line]) for line in input]
	num_rows, num_cols = 103, 101
	# num_rows, num_cols = 7, 11
	grid = {}
	for row in range(num_rows):
		for col in range(num_cols):
			grid[(row, col)] = [0, set()]

	robot_index = {}
	for i, (pos, velocity) in enumerate(robots):
		cur = grid[pos]
		cur[0] += 1 
		cur[1].add(i)
		robot_index[i] = (velocity, True)

	results = []
	for step in range(10000):
		simulate_all_robots(grid, robot_index, num_rows, num_cols)
		for robot_id in robot_index:
			velocity, _ = robot_index[robot_id]
			robot_index[robot_id] = (velocity, True)

		if step == 8167:
			render_image(grid, num_rows, num_cols, step)

		percent_full = sum(1 if grid[pos][0] > 0 else 0 for pos in grid) / (num_rows * num_cols)
		results.append((percent_full, step))

	results.sort(reverse=True)
	print(results[:10])

	q1, q2, q3, q4 = [], [], [], []
	half_rows = num_rows / 2
	half_cols = num_cols / 2
	for row in range(num_rows):
		for col in range(num_cols):
			if row == 51 or col == 50:
				continue

			if row <= half_rows and col <= half_cols and grid[(row, col)][0] > 0:
				q1.append(grid[(row, col)][0])
			elif row >= half_rows and col <= half_cols and grid[(row, col)][0] > 0:
				q3.append(grid[(row, col)][0])
			elif row <= half_rows and col >= half_cols and grid[(row, col)][0] > 0:
				q2.append(grid[(row, col)][0])
			elif row >= half_rows and col >= half_cols and grid[(row, col)][0] > 0:
				q4.append(grid[(row, col)][0])

	p1 = sum(q1) * sum(q2) * sum(q3) * sum(q4)
	print(p1)

if __name__ == '__main__':
	main()