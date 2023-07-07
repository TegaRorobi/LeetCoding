
def merge(intervals: list[list[int]]) -> list[list[int]]:
	res = []
	for interval in sorted(intervals, key=lambda x : x[0]):
		if res and res[-1][1] >= interval[0]:
			res[-1][1] = max(res[-1][1], interval[1])
		else:
			res.append(interval)
	return res


print(merge([[1,2], [3,5], [10,12], [4,7], [8,10]]))