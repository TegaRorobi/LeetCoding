
def maxProductBrute(nums: list[int]) -> int:
    # brute force, O(n^2) runtime complexity
    maxP = -(2*10**4)
    for i in range(len(nums)):
        curr_prod = nums[i]
        maxP = max(curr_prod, maxP)
        if curr_prod == 0:
            maxP = max(curr_prod, maxP)
            curr_prod = 1
        for j in range(i+1, len(nums)):
            if nums[j] == 0:
                maxP = 0 if maxP < 0 else maxP
                curr_prod = 1 
                continue
            curr_prod *= nums[j]
            maxP = curr_prod if curr_prod > maxP else maxP
    return maxP if len(nums)>1 else nums[0]

def maxProductTry2(nums:list[int]) -> int:
    dp = [1] * (len(nums) + 1)
    dp[-1] = nums[-1]
    for i in range(len(nums)-1, -1, -1):
        if dp[i+1] == 0:
            dp[i] == nums[i]
        else:
            dp[i] = max(nums[i], nums[i]*dp[i+1])
    print(dp)
    return max(dp[:-1])


# Working solution, O(n) runtime, O(n) space
def maxProduct2(nums:list[int]) -> int:
    if len(nums) == 1: return nums[0]
    dp = [[1, 1]] * len(nums)
    dp[-1] = nums[-1], nums[-1]
    for i in range(len(nums)-2, -1, -1):
        choices = nums[i], nums[i]*dp[i+1][0], nums[i]*dp[i+1][1]
        dp[i][0] = min(choices)
        dp[i][1] = max(choices)
    return max(list(zip(*dp))[1])


# O(n) runtime, O(1) space, reverse iteration with pointer indices
def maxProduct1(nums:list[int]) -> int:
    if len(nums) == 1: return nums[0]
    mini = maxi = maxP = nums[-1]
    
    for i in range(len(nums)-2, -1, -1):
        choices = nums[i], nums[i]*mini, nums[i]*maxi
        mini = min(choices)
        maxi = max(choices)
        maxP = max(maxP, maxi)
    return maxP


# O(n) runtime, O(1) space, forward iteration without indices
def maxProduct(nums:list[int]) -> int:
    if len(nums)==1:return nums[0]
    mini = maxi = maxP = nums[0]

    for n in nums[1:]:
        choices = n, n*mini, n*maxi
        mini = min(choices)
        maxi = max(choices)
        maxP = max(maxP, maxi)
    return maxP


print(maxProduct([2, 3, -2, 4]))
print(maxProduct([-2, 0, -1]))
print(maxProduct([0, 2]))
print(maxProduct([3, -1, 4]))
