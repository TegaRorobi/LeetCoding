
# BUBBLE SORT algorithm
# O(n^2) runtime complexity, O(1) space, modifies the array in-place
def bubble_sort(array):
	done = False
	while not done:
		done = True 
		for i in range(len(array)-1):
			if array[i] > array[i+1]:
				temp = array[i+1]
				array[i+1] = array[i]
				array[i] = temp 
				done = False
	return array

print(bubble_sort([4, 2, 8, 3, 6, 9, 1, 7]))
print(bubble_sort([10]))
print(bubble_sort([700, 100, 400, 300, 900, 200, 800, 500, 600]))
print(bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
