# def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
# 	res = []
# 	def dfs(i, curr, total):
		
# 		if total == target:
# 			comb = sorted(curr)
# 			if comb not in res:
# 				res.append(comb)
# 			return
# 		if total > target or i >= len(candidates):
# 			return

# 		# the i pointer shifts and we add the candidate at index i
# 		# curr.append(candidates[i])
# 		dfs(i+1, curr+[candidates[i]], total+candidates[i])

# 		# the i pointer still shifts but we don't add that candidate
# 		# curr.pop()
# 		dfs(i+1, curr, total)

# 	dfs(0, [], 0)
# 	return res

def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
	res = []
	candidates.sort()

	def backtrack(curr, rem, idx):
		# print(curr, rem, idx)
		if rem == 0:
			if curr not in res:
				res.append(curr)
		else:
			for i in range(idx, len(candidates)):
				if i > idx and candidates[idx] == candidates[idx-1]:
					return
				if rem-candidates[i] < 0:
					break
				backtrack(curr+[candidates[i]], rem-candidates[i], i+1)
			
	backtrack([], target, 0)
	return res

print(combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
print(combinationSum2(candidates = [2, 2, 2, 5, 1], target = 5))
print(combinationSum2(candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], target=27))
