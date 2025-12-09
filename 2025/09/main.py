from shapely.geometry import Polygon, box


def main():
	with open('input.txt') as f:
		data = f.readlines()
		data = [tuple([int(x) for x in line.strip().split(',')]) for line in data]

		polygon = Polygon(data)
		areas = {}
		for p1 in data:
			for p2 in data:
				rect = box(
					min(p1[0], p2[0]),
					min(p1[1], p2[1]),
					max(p1[0], p2[0]),
					max(p1[1], p2[1])
				)
				if p1 != p2 and polygon.contains(rect):
					height = abs(p1[0] - p2[0]) + 1
					width = abs(p1[1] - p2[1]) + 1
					areas[(p1, p2)] = height * width

		print(max(areas.values()))


if __name__ == '__main__':
	main()