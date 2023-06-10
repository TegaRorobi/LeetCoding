
# Time Complexity: O(n)
# Space Complexity: O(1)

def maxArea(height):
	# we initialize two pointers at the extreme ends of the array
	l, r = 0, len(height)-1
	curr_max = 0 

	while l < r:
		# now we compute the area with the distance between the pointers and the limiting height
		area = (r-l) * min(height[l], height[r])
		curr_max = max(curr_max, area)

		# here we want to update the left pointer if it is the limiting pointer
		if height[l] < height[r]:
			l += 1
		# here we also want to decrement the right pointer if it is the limiting pointer in 
		# hope of finding a larger value. In an additional else case with this case, 
		# where the values of both pointers are equal, we can move any of the pointers, 
		# and that can be condensed into simply an else clause instead of elif and else
		else:
			r-=1
	return curr_max


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))