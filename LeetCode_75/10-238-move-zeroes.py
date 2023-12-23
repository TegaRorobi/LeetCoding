"""
Problem Statement:
------------------
    Given an integer array nums, move all 0's to the end of it while maintaining
    the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.


Examples:
---------
    Example 1:
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]

    Example 2:
        Input: nums = [0]
        Output: [0]


Constraints:
------------
    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1


Follow up:
----------
    Could you minimize the total number of operations done?


Approach:
---------
    For this solution, I'll use a two-pointer approach. I'll have two pointers, initially at the first
    and second elements. The first pointer would move up until the point where we find a zero, and then it'll
    stop and move the other pointer until we find the next non-zero number. When we do, we swap them, and
    increment just the first pointer as we're sure we aren't leaving behind any zero.

    if the first pointer ever catches up to the second one, then we'll just increment the second one
    to be ahead of the first by one index. We'll also add checks to make sure the pointer indices don't
    get too big and cause an IndexError

    The first pointer is essentially the divider between the zero and non-zero sides for the most part,
    while the second one fetches the non-zero values to be pushed behind the first pointer.


Complexity:
-----------
    Time: O(2n) => O(n) => We evaluate every element in the nums array at most twice
    Space: O(n)

"""

from typing import *

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 1
        ln = len(nums)
        while j < ln and i < ln:
            if nums[i] == 0: # when i is on a zero, find the next non-zero number (with j) to swap with
                while j < (ln-1) and nums[j] == 0: # calibrate j until it's on a non-zero number
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j = j if j > i+1 else i+1
        return nums


soln = Solution()
print(soln.moveZeroes([0, 1, 0, 3, 12]))
print(soln.moveZeroes([0, 1, 0, 7, 4, 0, 2, 1, 0, 0]))
print(soln.moveZeroes([0]))
print(soln.moveZeroes([4,2,4,0,0,3,0,5,1,0]))
print(soln.moveZeroes([0, 1]))