
def maximumSubarray(nums):
	maxSum = 0

	# O(n^2) time complexity
	# for i in range(len(nums)):
		# curr_sum = 0
		# for j in nums[i:]:
		# 	curr_sum+=j
		# 	maxSum = curr_sum if maxSum < curr_sum else maxSum
	# return maxSum


	# O(n) Solution
	# l = r = curr_sum = 0
	# while r < len(nums):
	# 	curr_sum += nums[r]
	# 	maxSum = curr_sum if curr_sum > maxSum else maxSum
	# 	if curr_sum < 0:
	# 		curr_sum = 0
	# 		l = r
	# 	r+=1

	
	# or

	# O(n) alternative
	curr_sum = 0
	for n in nums:
		curr_sum = 0 if curr_sum < 0 else curr_sum
		curr_sum += n
		maxSum = curr_sum if curr_sum > maxSum else maxSum

	return maxSum





nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximumSubarray(nums))
