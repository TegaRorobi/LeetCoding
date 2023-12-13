
"""
Problem statement:
------------------
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words,
if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


Approach:
---------
For this solution, I'll create a dp array, which I'll iterate over in reverse. This is done like so, because I'll be using a 
dynamic programming approach. The smaller problem is getting the minimum number of jumps from a location closer to the target.
If I have that, I can get the minimum number of jumps from a farther place by calculating all my possible jump locations, 
and jump to the spot that has the least number of jumps to the end by adding one jump (from the current position). Continuing 
in this simple fashion, the answer would be the value of the dp array at the first index.

Complexity:
-----------
Time: O(n^2)
Space: O(n)
"""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n-1) + [0]
        for i in range(n-2, -1, -1):
            minJumpsToEnd = n-1
            end_ind = min(i+nums[i]+1, n)
            for j in range(i+1, end_ind):
                jump = dp[j]
                minJumpsToEnd = jump if jump < minJumpsToEnd else minJumpsToEnd
            dp[i] = 1+minJumpsToEnd
        return dp[0]


soln = Solution()
print(soln.jump([2, 3, 1, 1, 4]))
print(soln.jump([2, 3, 0, 1, 4]))
print(soln.jump([2, 1, 0, 0]))
