"""
Problem Statement:
------------------
    There are n kids with candies. You are given an integer array candies, where each
    candies[i] represents the number of candies the ith kid has, and an integer extraCandies,
    denoting the number of extra candies that you have.

    Return a boolean array result of length n, where result[i] is true if, after giving the ith
    kid all the extraCandies, they will have the greatest number of candies among all the kids,
    or false otherwise.

    Note that multiple kids can have the greatest number of candies.

Examples:
---------

    Example 1:

        Input: candies = [2,3,5,1,3], extraCandies = 3
        Output: [true,true,true,false,true]
        Explanation: If you give all extraCandies to:
        - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
        - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
        - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
        - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
        - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

    Example 2:

        Input: candies = [4,2,1,1,2], extraCandies = 1
        Output: [true,false,false,false,false]
        Explanation: There is only 1 extra candy.
        Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

    Example 3:

        Input: candies = [12,1,12], extraCandies = 10
        Output: [true,false,true]

Approach:
---------
    For this solution, the idea is pretty simple. For any kid to have the greatest number of candies
    when handed the extra candies, then their initial candies plus the extra must be greater than or equal
    to the greatest initial amount of candy any kid has. Therefore, with this simple ideology, we can easily
    calculate a breakpoint candy count, which would be the minimum number of candy you must initially have to
    have the greatest number when handed the extra candies. This value is the difference between the maximum
    value of the candies array, and the number of the extra candies.

Complexity:
-----------
    Time: O(2n) => O(n) => We traverse the candies array once to find the max, and then
                           once again to convert the values to booleans with the breakpoint
    Space: O(1) => If we don't count the space of the result array
"""

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        breakpoint = max(candies) - extraCandies
        return [n>=breakpoint for n in candies]

    # A more "manual" approach :)
    def kidsWithCandies2(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = 0
        n_candies = 0
        for candy in candies:
            n_candies += 1
            if candy > max_candies:
                max_candies = candy

        breakpoint = max_candies - extraCandies
        result = [False] * n_candies
        for i, candy in enumerate(candies):
            if candy >= breakpoint:
                result[i] = True

        return result


soln = Solution()
print(soln.kidsWithCandies2(candies=[2, 3, 5, 1, 3], extraCandies=3))
print(soln.kidsWithCandies2(candies=[4, 2, 1, 1, 2], extraCandies=1))
print(soln.kidsWithCandies2(candies=[12, 1, 12], extraCandies=10))
