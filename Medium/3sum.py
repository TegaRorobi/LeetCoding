

def threeSum(nums, target):
	nums.sort()
	ans = []
	for i, a in enumerate(nums):

		if i > 0 and a == nums[i-1]: 
			continue

		l, r = i+1, len(nums)-1
		while l < r:
			threesum = a + nums[l] + nums[r]
			if threesum < target:
				l+=1
			elif threesum > target:
				r-=1
			else:
				ans.append([a, nums[l], nums[r]])
				l+=1

				while nums[l] == nums[l-1]:
					l+=1


	return ans
print(threeSum([-1, 1, 2, 2, 3], 4))