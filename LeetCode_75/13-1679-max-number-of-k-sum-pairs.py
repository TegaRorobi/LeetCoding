"""
Problem Statement:
------------------
    You are given an integer array nums and an integer k.

    In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

    Return the maximum number of operations you can perform on the array.


Examples:
---------
    Example 1:
        Input: nums = [1,2,3,4], k = 5
        Output: 2
        Explanation: Starting with nums = [1,2,3,4]:
        - Remove numbers 1 and 4, then nums = [2,3]
        - Remove numbers 2 and 3, then nums = []
        There are no more pairs that sum up to 5, hence a total of 2 operations.

    Example 2:
        Input: nums = [3,1,3,4,3], k = 6
        Output: 1
        Explanation: Starting with nums = [3,1,3,4,3]:
        - Remove the first two 3's, then nums = [1,4,3]
        There are no more pairs that sum up to 6, hence a total of 1 operation.


Constraints:
------------
    1 <= nums.length <= 105
    1 <= nums[i] <= 109
    1 <= k <= 109



Approach:
---------
    For this solution, I'll take a similar approach to the famous 'Two Sum' problem.
    I'll iterate over the array, and then I'll use a hashmap to keep track of numbers that I need to
    make up a sum of k, and how many of each value I need (the keys would be the numbers I need, and
    then the values would be how many of such numbers I need). While iterating, if I find such a number,
    I'll decrement the corresponding value in the hashmap by 1, and increase the count so far, and if after
    decrementing, I find that I no longer need that number, I'll remove it from the hashmap. If I don't
    come across a number I needed before, then I'll subtract the number from k, and either add a new key
    of a number I now need, or increment the existing count if I already needed that newly calculated number.


Complexity:
-----------
    Time: O(n)
    Space: O(n)

"""

from typing import List

class Solution:

    def maxOperations(self, nums: List[int], k: int) -> int:
        # best performing solution, O(n) time, O(n) space
        n_operations = 0
        needed = {}
        for n in nums:
            if n in needed:
                n_operations += 1
                if needed[n] == 1:
                    needed.pop(n)
                else:
                    needed[n] = needed[n] - 1
            elif k-n > -1:
                needed[k-n] = needed.get(k-n, 0) + 1
        return n_operations


    def maxOperations2(self, nums: List[int], k: int) -> int:
        # O(n^2) time, O(1) space
        n_operations = 0
        i = 0
        while i < len(nums):
            nums_i = nums[i]
            j = i+1
            rem = k - nums_i
            while j < len(nums):
                nums_j = nums[j]
                if nums_j == rem:
                    n_operations += 1
                    nums.remove(nums_i)
                    i -= 1
                    nums.remove(nums_j)
                    break
                j += 1
            i += 1
        return n_operations


    def maxOperations3(self, nums: List[int], k: int) -> int:
        # O(n) time, O(n) space
        n_operations = 0
        needed = []
        for n in nums:
            if n in needed:
                needed.remove(n)
                n_operations += 1
            elif k-n > -1:
                needed.append(k-n)
        return n_operations


    def maxOperations4(self, nums: List[int], k: int) -> int:
        # O(nlogn) time, O(1) space
        nums=sorted(nums)
        l, r = 0, len(nums)-1
        res = 0
        while l<r:
            if nums[l]+nums[r] < k:
                l += 1
            elif nums[l]+nums[r]>k:
                r -= 1
            else:
                res += 1
                l += 1
                r -= 1
        return res


soln = Solution()
print(soln.maxOperations([1,2,3,4], 5))
print(soln.maxOperations([3,1,3,4,3], 6))
print(soln.maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3))