L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]

def longest_run(seq):
	current_run = []
	longest_run = []

	for item in seq:
		if current_run == []:
			# first run
			current_run.append(item)
		elif item > current_run[-1]:
			# increasing
			current_run.append(item)
		elif longest_run and item < longest_run[-1]:
			# decr
			longest_run.append(item)
		elif len(longest_run) < len(current_run):
			longest_run = current_run
		else:
			continue
	return longest_run
