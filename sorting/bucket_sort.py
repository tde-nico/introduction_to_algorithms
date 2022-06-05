from insertion_sort import insertion_sort

def bucket_sort(array):
	mx = max(array)
	size = mx / len(array)
	bucket, final = [], []
	for x in range(len(array)):
		bucket.append([])
	for i in range(len(array)):
		j = int (array[i] / size)
		if j != len (array):
			bucket[j].append(array[i])
		else:
			bucket[len(array) - 1].append(array[i])
	for z in range(len(array)):
		insertion_sort(bucket[z])
	for x in range(len (array)):
		final = final + bucket[x]
	return final
