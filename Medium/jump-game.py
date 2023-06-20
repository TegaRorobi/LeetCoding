
def canJump(nums:list[int]) -> bool:
	# O(n) time and O(n) space
	'''
	n = len(nums)
	dp = [False] * (n-1) + [True]

	for i in range(n-2, -1, -1):
		n_steps = nums[i]
		while n_steps > 0:
			if i+n_steps > n or i+n_steps < n and dp[i+n_steps]==True:
				dp[i] = True 
				break
			n_steps -= 1
	return dp[0]
	'''

	# O(n) time and O(1) space
	target = len(nums)-1
	for i in range(len(nums)-2, -1, -1):
		if i + nums[i] >= target:
			target = i
	return target == 0 


print(canJump([2, 3, 1, 1, 4]))
print(canJump([3, 2, 1, 0, 4]))
print(canJump([2, 5, 0, 0]))
