
def findDuplicate(nums:list[int]) -> int:
	tortoise = nums[0]
	hare = nums[0]
	while True:
		print(tortoise, hare)
		tortoise = nums[tortoise]
		hare = nums[nums[hare]]
		if tortoise == hare:
			break
	ptr1, ptr2 = nums[0], tortoise
	while ptr1 != ptr2:
		ptr1 = nums[ptr1]
		ptr2 = nums[ptr2]
	return ptr1

print(findDuplicate([1, 3, 4, 2, 2]))
print(findDuplicate([3, 1, 3, 4, 2]))