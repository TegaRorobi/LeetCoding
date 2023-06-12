
# Time Complexity: O(2n-2) => O(n)
# Space Complexity: constant i.e O(1)
def robII(nums:list[int]) -> int:

	def get_max_rob(houses):
		rob1, rob2 = 0, 0 
		for house in houses:
			rob1, rob2 = rob2, max(house+rob1, rob2)
		return rob2

	# since the houses are now in a circle, we return the max loot from all the houses
	# starting from the first house excluding the last house, or we could skip the first 
	# house and then get the loot for all houses onwards. Afterwards, we return the max of 
	# both loots, thereby avoiding a sticky situation where we rob adjacent houses and get busted!
	# In the edge case where there is only one house, then we pass in empty arrays into the 
	# get_max_rob helper function, and we get no loot, so adding the first value in the array
	# which would then be the maximun takes care of this edge case quite neatly.
	return max(nums[0], get_max_rob(nums[:-1]), get_max_rob(nums[1:]))


print(robII([2, 3, 2]))