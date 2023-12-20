"""
Problem Statement:
------------------
    Given an integer array nums, return an array answer such that answer[i] is equal to the product
    of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.


Examples:
----------
    Example 1:
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]

    Example 2:
        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]


Constraints:
------------
    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow Up:
----------
    Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra
    space for space complexity analysis.)


Approach:
---------
    For this solution, we want to create an array where the value of the array at a particular position
    is the product of all elements in the input array except for the element at that position.
    This value also equates to the product all elements before a particular element, multiplied
    by the product of all elements after that element.

    The way we could do this in O(n) time without slicing the array and calculating the product on every
    iteration is as follows:
        We simply iterate in the forward direction once, and then the value for an index would be the product of
        all elements before that value. Nice, right? but we'll quickly find that this is incomplete. What about
        all elements after this element?🤔
    Simple, we do the same thing in the reverse direction 💡 where we calculate a running product and then multiply
    the values in the array we already have, by the running product of all elements after. We'll then update the
    running product with this value, and so on until we are done.


Complexity:
-----------
    Time: O(2n) => O(n) => We traverse the input array twice, once in the forward direction
                           and once in the reverse direction.
    Space: O(1) => If we don't count the space of the result array.

"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        res = [-1] * len(nums)
        curr = 1
        i = 0
        while i < ln:
            res[i] = curr
            curr *= nums[i]
            i += 1
        i = ln - 1
        curr = 1
        while i > -1:
            res[i] *= curr
            curr *= nums[i]
            i -= 1
        return res


soln = Solution()
print(soln.productExceptSelf([1,2,3,4]))
print(soln.productExceptSelf([-1,1,0,-3,3]))