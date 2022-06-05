def selection_sort(array):
	for i in range(len(array) - 1):
		m = i
		for j in range(i + 1, len(array)):
			if (array[j] < array[m]):
				m = j
			array[m], array[i] = array[i], array[m]
