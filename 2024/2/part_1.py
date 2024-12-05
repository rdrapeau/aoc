def process_report(report, can_remove_level):
	if len(report) <= 1:
		return True

	is_increasing = report[0] < report[1]
	for i in range(0, len(report) - 1):
		difference = report[i] - report[i + 1]
		if (
			abs(difference) > 3
			or difference == 0
			or (is_increasing and difference > 0)
			or (not is_increasing and difference < 0)
		):
			if can_remove_level:
				for j in range(-1, 2):
					first_part = report[:i + j] if i + j >= 0 else []
					report_with_level_removed = first_part + report[i + 1 + j:]
					is_safe_without_level = process_report(report_with_level_removed, can_remove_level=False)
					if is_safe_without_level:
						return True

			return False

	return True

def main():
	with open('part_1.csv') as f:
		data = [[int(entry) for entry in l.split()] for l in f.readlines()]

	num_safe_reports = 0
	for report in data:
		is_safe = process_report(report, can_remove_level=True)
		# is_safe_without_level_removal = process_report(report, can_remove_level=False)
		if is_safe:
			num_safe_reports += 1

	# 589
	print(num_safe_reports)

if __name__ == '__main__':
	main()