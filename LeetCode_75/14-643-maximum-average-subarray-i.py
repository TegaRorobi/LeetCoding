"""
Problem Statement:
------------------
    You are given an integer array nums consisting of n elements, and an integer k.

    Find a contiguous subarray whose length is equal to k that has the maximum average
    value and return this value. Any answer with a calculation error less than 10-5 will
    be accepted.


Examples:
---------
    Example 1:
        Input: nums = [1,12,-5,-6,50,3], k = 4
        Output: 12.75000
        Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

    Example 2:
        Input: nums = [5], k = 1
        Output: 5.00000


Constraints:
------------
    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104


Approach:
---------
    For this solution, I'll use a sliding window approach. I'll iterate over the array, and initially
    keep a sum of the first k elements in the array. While iterating, I'll add the next element to my
    'window' of elements, and remove the last item out of the window and calculate the sum of the new
    window. To be efficient, I'll just keep a pointer I'll use to know where I am in the iteration,
    and then simply add the next element to the already calculated sum, and then subtract the last
    element from this value.

    While doing so, I'll use another variable to keep track of the maximum sum of any k-length window
    I've come across at the end of the iteration. I'll then return the float resulting from the division
    of this number by k (the maximum average).


Complexity:
-----------
    Time: O(n)
    Space: O(1)

Note:
-----
    This problem is very similar to "1423. Maximum Points You Can Obtain from Cards",
    but this time we're returning an average, and we're considering the values inside
    the window as opposed to the ones outside the window.
"""

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi = total = sum(nums[:k])
        for i in range(len(nums)-k):
            total -= nums[i]
            total += nums[i+k]
            maxi = maxi if maxi > total else total
        return maxi / k


soln = Solution()
print(soln.findMaxAverage([1,12,-5,-6,50,3], k=4))
print(soln.findMaxAverage([5], k=1))
print(soln.findMaxAverage([7,4,5,8,8,3,9,8,7,6], k=7))
