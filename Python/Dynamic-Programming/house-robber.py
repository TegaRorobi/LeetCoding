
# Time Complexity : O(n)
# Space Complexity : O(1)
def rob(nums:list[int]) -> int:
	rob1, rob2 = 0, 0 
	for n in nums:
		rob1, rob2 = rob2, max(n+rob1, rob2) 
	return rob2



print(rob([2, 3, 10, 4, 2, 10]))