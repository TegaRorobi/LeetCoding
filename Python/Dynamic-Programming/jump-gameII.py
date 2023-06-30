
def jump(nums:list[int]) -> int:
	'Time complexity: O(n^2)'
	'Space complexity: O(n)'
	len_nums = len(nums)

	# having -1 as the value of an index in the dp array means that we 
	# can not get to the end if we jump to that index, hence it's the default
	dp = [-1] * (len_nums-1) + [0] 
	# since we will be adding 1 to the cached value from the subproblem, 
	# we might as well just use 0 as the base case.

	for i in range(len_nums-2, -1, -1):
		minJumpsToEnd = 10**4
		for j in range(i+1, min(len_nums, i+nums[i]+1)):
			if dp[j] != -1:
				minJumpsToEnd = dp[j] if dp[j] < minJumpsToEnd else minJumpsToEnd
		dp[i] = 1+minJumpsToEnd
	print(dp)
	return dp[0]


print(jump([2, 3, 1, 1, 4]))
print(jump([2, 5, 0, 0]))
