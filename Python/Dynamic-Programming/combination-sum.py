
def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
	# Brute force, O(n^m) runtime (where n=len(candidates), m=target)
	# res = []
	# def findCombinations(lst, running_sum, res):
	# 	if running_sum == target and lst not in res:
	# 		res.append(lst)
	# 	for n in candidates:
	# 		if n+running_sum == target:
	# 			arr = sorted(lst+[n])
	# 			if arr not in res:
	# 				res.append(arr)
	# 		elif n+running_sum < target:
	# 			findCombinations(lst+[n], running_sum+n, res)
	# 		else:
	# 			return
	# for n in candidates:
	# 	findCombinations([n], n, res)
	# return res


	# more optimized solution with dfs, O(2^n) runtime (where n=target)
	res = []
	def dfs(i, curr, total):
		if total == target:
			res.append(curr.copy())
			return
		if total > target or i >= len(candidates):
			return 

		# the case where we use the same candidate again
		curr.append(candidates[i])
		dfs(i, curr, total + candidates[i])

		# the case where we no longer use this candidate to avoid duplicates
		curr.pop()
		# we use only the next candidate in the array
		dfs(i+1, curr, total)

	dfs(0, [], 0)

	return res




print(combinationSum(candidates = [2,3,6,7], target = 7))
print(combinationSum(candidates = [2,3,5], target = 8))
print(combinationSum(candidates = [2], target = 1))
print(combinationSum(candidates = [2, 3, 4, 3], target = 7))