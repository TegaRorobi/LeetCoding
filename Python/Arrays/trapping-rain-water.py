# HARD


# the actual solution
def trap(heights: list[int]) -> int:
	if len(heights) < 3:
		return 0
	volume = 0
	l = 0
	r  = len(heights)-1
	lmax = heights[l]
	rmax = heights[r]
	while l < r:
		if lmax < rmax:
			l += 1
			lmax = max(heights[l], lmax)
			volume += lmax-heights[l]
		else:
			r -= 1
			rmax = max(heights[r], rmax)
			volume += rmax-heights[r]
	return volume


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trap([1, 0, 2, 0, 1, 3, 0, 1, 0, 4]))
print(trap([1, 0, 3, 0, 2]))
