
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
	left, right = [], []
	s, e = newInterval[0], newInterval[1]
	START, END = 0, 1 
	for cur_interval in intervals:
		# this means the newInterval doesn't overlap with this interval and it is to the left
		if cur_interval[END] < s:
			left.append(cur_interval)

		# this means the newInterval doesn't overlap with this interval and it is to the right
		elif cur_interval[START] > e:
			right.append(cur_interval)

		# the two intervals overlap, so we take the largest bounds, left and right.
		else:
			s = min(s, cur_interval[START])
			e = max(e, cur_interval[END])
	return left + [[s, e]] + right



"an alternative method to solving this problem by Stephen Pochmann"
"A lot more elegant, but more expensive and kind of slower"
def insert2(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
	left = [i for i in intervals if i[1] < newInterval[0]]
	right = [i for i in intervals if i[0] > newInterval[1]]
	s = min(newInterval[0], intervals[len(left)][0])
	e = max(newInterval[1], intervals[~len(right)][1])
	return left + [[s, e]] + right



print(insert2(intervals = [[1,3], [6,9]], newInterval = [2,5]))
print(insert2(intervals = [[1,2], [3,5], [8,10], [12,16]], newInterval = [6,7]))
print(insert2(intervals = [[1,2], [3,5], [6,7], [8,10], [12,16]], newInterval = [4,8]))
