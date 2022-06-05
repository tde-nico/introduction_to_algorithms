def counting_sort(array):
	mx = max(array)
	length = len(array)
	count = [0] * (mx+1)
	for j in range(length):
		count[array[j]] += 1
	j = 0
	for i in range(mx):
		while (count[i] > 0):
			array[j] = i
			j += 1
			count[i] -= 1

def	counting_sort_with_data(array):
	mx = max(array)
	length = len(array)
	count = [0] * (mx+1)
	counted = [0] * length
	for j in range(length):
		count[array[j]] += 1
	for i in range(1, mx):
		count[i] += count[i - 1]
	for j in range(length, -1):
		counted[count[array[j]]] = array[j]
		count[array[j]] -= 1
	return counted
