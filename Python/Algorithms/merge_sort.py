
# Implementing the merge sort algorithm
def mergeSort(array):
	if not array or len(array) == 1:
		return array

	sub1 = mergeSort(array[:(len(array)//2)])
	sub2 = mergeSort(array[(len(array)//2):])

	merged = []
	while sub1 and sub2:
		if sub1[0] < sub2[0]:
			merged.append(sub1[0])
			sub1 = sub1[1:]
		else:
			merged.append(sub2[0])
			sub2 = sub2[1:]
	if sub1 or sub2:
		merged.extend(sub1 if sub1 else sub2)
	return merged


print(mergeSort([4, 2, 8, 3, 6, 9, 1, 7]))
print(mergeSort([10]))
print(mergeSort([100, 400, 300, 900, 200, 800, 500, 600]))