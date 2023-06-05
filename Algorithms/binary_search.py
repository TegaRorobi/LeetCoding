
def binarySearch(nums, target):
    l, r = 0, len(nums)-1

    while l<=r:
        midpoint = (l+r)//2

        if target > nums[midpoint]:
            l = midpoint+1 
        elif target < nums[midpoint]:
            r = midpoint-1
        else:
            return midpoint 



nums = [43, 45, 54, 56, 61, 69, 72, 77, 82, 99, 103, 106, 111]
target = 77

print(binarySearch(nums, target))
