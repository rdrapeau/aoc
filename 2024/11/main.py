from functools import cache

def blink_once(stone):
	if stone == 0:
		return [1]
	elif len(str(stone)) % 2 == 0:
		tmp = str(stone)
		return [int(tmp[:len(tmp) // 2]), int(tmp[len(tmp) // 2:])]
	else:
		return [stone * 2024]

@cache
def simulate_stone(stone, steps_remaining):
	if steps_remaining == 1:
		return len(blink_once(stone))
	else:
		after_blink = blink_once(stone)
		return sum(simulate_stone(stone, steps_remaining - 1) for stone in after_blink)


def main():
	with open('input.txt') as f:
		stones = [int(x) for x in f.read().strip().split()]

	print(sum(simulate_stone(stone, 75) for stone in stones))


if __name__ == '__main__':
	main()
