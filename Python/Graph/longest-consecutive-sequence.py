# Medium

# O(n) runtime, O(n) space
def longestConsecutive(nums):
	lcs = 1
	# we'll take advantage of constant lookup time in a set
	nums_set = set(nums)
	for n in nums:
		if n-1 not in nums_set:
			len_seq = 1
			while n+1 in nums_set:
				n += 1
				len_seq += 1
			lcs = max(lcs, len_seq)
	return lcs
print(longestConsecutive([100, 4, 200, 1, 3, 2, 8, 5]))