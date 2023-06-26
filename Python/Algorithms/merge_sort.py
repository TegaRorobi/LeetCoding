
# MERGE SORT algorithm
# O(nlogn) runtime complexity, O(n) space.
def mergeSort_recursive(array):
	if not array or len(array) == 1:
		return array
	mid = len(array)//2
	sub1 = mergeSort_recursive(array[:mid])
	sub2 = mergeSort_recursive(array[mid:])

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





def mergeSort_iterative(array):
	ans = [[i] for i in array]

	while len(ans) > 1:
		merged = []
		for i in range(0, len(ans), 2):
			combined = []
			sub1 = ans[i]
			sub2 = ans[i+1] if (i+1) < len(ans) else None

			while sub1 and sub2:
				if sub1[0] < sub2[0]:
					combined.append(sub1[0])
					sub1 = sub1[1:]
				else:
					combined.append(sub2[0])
					sub2 = sub2[1:]
			if sub1 or sub2:
				combined.extend(sub1 if sub1 else sub2)
			merged.append(combined)
		ans = merged
	return ans[0]






print(mergeSort_iterative([4, 2, 8, 3, 6, 9, 1, 7]))
print(mergeSort_iterative([10]))
print(mergeSort_iterative([700, 100, 400, 300, 900, 200, 800, 500, 600]))