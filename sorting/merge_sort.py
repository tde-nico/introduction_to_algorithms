def merge(array, first, middle, last):
	i, j = first, middle + 1 
	merged = []
	while ((i <= middle) and (j <= last)):
		if (array[i] <= array[j]):
			merged.append(array[i])
			i += 1
		else:
			merged.append(array[j])
			j += 1
	while (i <= middle):
		merged.append(array[i])
		i += 1
	while (j <= last):
		merged.append(array[j])
		j += 1
	for i in range(len(merged)):
		array[first + i] = merged[i]

def merge_sort(array, first, last):
	if (first < last):
		middle = (first + last) // 2
		merge_sort(array, first, middle)
		merge_sort(array, middle + 1, last)
		merge(array, first, middle, last)

def merge_sort_iter(array):
	length = 1
	while length <= len(array) // 2:
		i = 0
		while i <= len(array) - 2 * length:
			merge(array, i, i + length, i + 2 * length - 1)
			i += 2 * length
		length *= 2
