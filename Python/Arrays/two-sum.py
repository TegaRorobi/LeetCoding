
def twoSum(nums:list[int], target:int) -> list[int]:
	hashmap = {}
	for i, n in enumerate(nums):
		if n in hashmap:
			return hashmap[n], i 
		hashmap[target-n] = i

print(twoSum([1, 2, 3, 4], 5))