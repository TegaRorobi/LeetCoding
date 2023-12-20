"""
Problem Statement:
------------------
    Given an integer array nums, return true if there exists a triple of indices (i, j, k)
    such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


Examples:
----------
    Example 1:
        Input: nums = [1,2,3,4,5]
        Output: true
        Explanation: Any triplet where i < j < k is valid.

    Example 2:
        Input: nums = [5,4,3,2,1]
        Output: false
        Explanation: No triplet exists.

    Example 3:
        Input: nums = [2,1,5,0,4,6]
        Output: true
        Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:
------------
    1 <= nums.length <= 5 * 105
    -231 <= nums[i] <= 231 - 1


Follow Up:
----------
    Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?


Approach:
---------
    For this solution, while iterating over the array, we need to keep track of the minimum number so far,
    as well as the minimum number that's greater than this minimum number, and is to the right of it.

    On an initial look at this problem, a thought may arise. If we just take the minimum number at all times, and
    then start to make a build and get the number greater than than and then a final number even greater than
    that one, peradventure we find a new smallest value, do we forget about the previous build and start a new
    one? Some edge cases would definitely not pass if we do either or use this just like that.

    The workaround is that we do this, but we don't update the second smallest value just yet even when we find a
    new smallest. This value would only be updated if we find a value smaller that that. 

    But why does this work?

    Think of the second smallest value more like a guard, a threshold, a bar to beat, meaning that we are definitely
    sure that there's a value smaller than this, immediately we find a number larger than this, return True.

    How does this value get updated?
    Whenever we find a value less than it, but not less than the least value so far, we reduce the second
    smallest to that value

    What about the problem with continuing with or discarding a current build?
    With this setup, both builds will merge into each other, because of the second smallest(guard) value will always
    be valid, and will adjust accordingly


Complexity:
-----------
    Time: O(m+n) => We traverse the array only once
    Space: O(1)

"""

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


soln = Solution()
print(soln.increasingTriplet([1, 2, 3, 4]))
print(soln.increasingTriplet([5, 4, 3, 2, 1]))
print(soln.increasingTriplet([2, 1, 5, 0, 4, 6]))
print(soln.increasingTriplet([5, 1, 5, 5, 0, 8]))
