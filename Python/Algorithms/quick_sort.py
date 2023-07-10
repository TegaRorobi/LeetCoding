

def quickSort(array: list[int]):
	if len(array) < 2:
		return array
	pivot = array[-1]
	j, i = -1, 0
	while i < len(array):
		if array[i] <= pivot:
			j += 1
			array[i], array[j] = array[j], array[i]
		i += 1

	return quickSort(array[:j]) + [pivot] + quickSort(array[j+1:])



def quickSort_iterative(array: list[int]):
	if not array:
		return []

	res = []
	stack = [array]
	while stack:
		lst = stack.pop()
		if not lst:
			continue
		if len(lst) == 1:
			res.append(lst[0])
			continue
		pivot = lst[-1]
		j, i = -1, 0
		while i < len(lst):
			if lst[i] <= pivot:
				j += 1
				lst[j], lst[i] = lst[i], lst[j]
			i += 1
		stack.append(lst[j+1:])
		stack.append([pivot])
		stack.append(lst[:j])
	return res 





print(quickSort([20, 7, 4, 19, 12, 17, 13, 6, 8, 11]))
print(quickSort_iterative([20, 7, 4, 19, 12, 17, 13, 6, 8, 11]))
print(quickSort_iterative([20, 19, 17, 13, 12, 11, 8, 7]))