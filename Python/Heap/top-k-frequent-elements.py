
# my first solution without any libraries
def topKFrequent(nums, k: int):
	if k == len(nums):
		return nums
	hashmap = {n:0 for n in nums}
	for n in nums:
		hashmap[n] += 1
	return sorted(hashmap.keys(), key=hashmap.get)[-k:]
	

def topKFrequent2(nums, k: int):
	if k == len(nums):
		return nums

	from collections import Counter
	hashmap = Counter(nums)

	from heapq import nlargest
	return nlargest(k, hashmap.keys(), key=hashmap.get)


print(topKFrequent2([1,1, 1, 2, 2,3], 2))