
def productExceptSelf(nums:list[int]) -> list[int]:
	n = len(nums)
	res = [1]*n
	pre = 1
	post = 1
	for i in range(n):
		res[i] *= pre 
		pre *= nums[i]

		res[n-i-1] *= post 
		post *= nums[n-i-1]
	return res 

print(productExceptSelf([1, 2, 3, 4]))

