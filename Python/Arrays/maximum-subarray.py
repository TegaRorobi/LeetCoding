
def maximumSubarray(nums):
	maxSum = 0

	# Brute force, O(n^2) time complexity, O(1) space
	# for i in range(len(nums)):
	# 	curr_sum = 0
	# 	for j in nums[i:]:
	# 		curr_sum+=j
	# 		maxSum = curr_sum if maxSum < curr_sum else maxSum
	# return maxSum

	# dynamic programming solution with dp array, O(n) time, (n) space
	# dp = [0]*len(nums) + [0]
	# for i in range(len(nums)-1, -1, -1):
	# 	dp[i] = max(nums[i], nums[i]+dp[i+1])
	# # print(dp)
	# return max(dp)

    # # dynamic programming solution without array, O(n) time, O(1) space
	# next_num = 0
	# for i in range(len(nums)-1, -1, -1):
	# 	curr_max = max(nums[i], nums[i]+next_num)
	# 	maxSum = max(maxSum, curr_max)
	# 	next_num=curr_max

	# Greedy approach, O(n) time, O(n) space
	curr_sum = 0
	for n in nums:
		curr_sum = 0 if curr_sum < 0 else curr_sum
		curr_sum += n
		maxSum = curr_sum if curr_sum > maxSum else maxSum


	return maxSum





nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximumSubarray(nums))
