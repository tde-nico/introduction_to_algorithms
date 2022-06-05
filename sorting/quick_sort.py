def split(array, first, last):
	pivot = array[first]
	i = first - 1
	j = last + 1
	while True:
		while array[j] <= pivot:
			j = j - 1 
		while array[i] >= pivot:
			i = i + 1
		if (i < j): 
			array[i], array[j] = array[i], array[j]
		else:
			return j

def quick_sort(array, first, last):
	if (first < last):
		middle = split(array, first, last)
		quick_sort(array, first, middle)
		quick_sort(array, middle + 1, last)
