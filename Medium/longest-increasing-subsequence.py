
# my original solution on reading the problem
def longestIncreasingSubsequence(nums):
	longest_so_far = 0
	for pos, start in enumerate(nums):
		longest = 0 
		last_seq_num = -2147483647
		for num in nums[pos:]:
			if num > last_seq_num:
				longest += 1
				last_seq_num = num
		longest_so_far = max(longest, longest_so_far)
	return longest_so_far



# this was my solution after listening to neetcode's algorithm

# this solution is pretty close to neetcode's solution except that I 
# was using while loops and changing variables instead of a for loop 
# and a crafted range and that I added the longest subsequence length at 
# positions after a current position to a list and then got the max of that
# before registering it as the max of that position (which probably increased my time complexity)
# instead of registering the max of that position on the go.
def lengthOfLIS(nums:list[int]) -> int: 
	LIS_stack = [1] * len(nums)


	idx = len(nums)-1
	while idx >= 0:

		targets = []

		i = idx + 1
		while i < len(nums):
			if nums[i] > nums[idx]:
				# at first I forgot to add 1+ to LIS_stack[i] and then I watched him code 
				# it and then saw my mistake and was happy that my solution was a little 
				# less crappy and I successfully coded most of the algorithm.
				targets.append(1+LIS_stack[i]) 
			i+=1

		targets.append(1)
		LIS_stack[idx] = max(targets)

		# print(idx, targets, LIS_stack)

		idx -= 1
	return max(LIS_stack)




#here's neetcode's solution i comprehended and wrote out.

# Time Complexity: O(n^2)
# Space Complexity: O(n)
def lengthOfLIS2(nums:list[int]) -> int: 
	LIS = [1] * len(nums) 

	for i in range(len(nums)-1, -1, -1):
		for j in range(i+1, len(nums)):
			if nums[j] > nums[i]:
				LIS[i] = max(LIS[i], 1+LIS[j])
	return max(LIS)


def lengthOfLIS3(nums:list[int]) -> int:
	from bisect import bisect_left
	stack = [nums.pop(0)]

	for n in nums:
		if n > stack[-1]:
			stack.append(n)
		else:
			stack[bisect_left(stack, n)] = n
		print(stack, n)
	return len(stack)


print(lengthOfLIS3([5, 7, -2, 0, -1, 8, 1, 2, 4])) # [-2, -1, 1, 2, 4]
# print(lengthOfLIS2([7, 7, 7, 7, 7, 7, 7])) # this fails the condition where nums[j] > nums[i]