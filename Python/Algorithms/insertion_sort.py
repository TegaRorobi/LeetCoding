
# INSERTION SORT
# O(n^2) runtime, O(1) space
def insertion_sort(array):
	for i in range(len(array)):
		for j in range(i+1):
			if array[j]>=array[i]:
				tmp = array[i]
				for k in range(j, i+1):
					array[k], tmp = tmp, array[k]
				break
	return array


print(insertion_sort([4, 2, 8, 3, 6, 9, 1, 7]))
print(insertion_sort([10]))
print(insertion_sort([700, 100, 400, 300, 900, 200, 800, 500, 600]))
print(insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))