def heapify(A, i, size):
	left = 2 * i + 1
	right = 2 * i + 2
	i_max = i
	if ((left < size) and (A[left] > A[i])):
		i_max = left
	if ((right <= size) and (A[right] > A[i_max])):
		i_max = right
	if (i_max != i):
		A[i], A[i_max]=A[i_max], A[i]
		heapify(A, i_max, size)

def build_heap(array):
	for i in reversed(range(len(array) // 2)):
		heapify(array, i, len(array))

def heap_sort(array):
	build_heap(array)
	for i in reversed(range(1, len(array))):
		array[0], array[i] = array[i], array[0]
		heapify(array, 0, i)
