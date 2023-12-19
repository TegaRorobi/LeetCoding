"""
Problem Statement:
------------------
    You have a long flowerbed in which some of the plots are planted, and some are not.
    However, flowers cannot be planted in adjacent plots.

    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means
    not empty, and an integer n, return true if n new flowers can be planted in the flowerbed
    without violating the no-adjacent-flowers rule and false otherwise.


Examples:
----------
    Example 1:
        Input: flowerbed = [1,0,0,0,1], n = 1
        Output: true

    Example 2:
        Input: flowerbed = [1,0,0,0,1], n = 2
        Output: false
 

Constraints:
------------
    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length


Approach1:
---------
    There are a number of other solutions to this problem, but one of then is to iterate over the flowerbed, and
    check if is possible to plant in the current spot. We can do so if there is 
        - space on the left (or the left is the end) and there is
        - space on the right (or the right is the end) and there is
        - space in the current position we're in. [where a "space" is a 0]
    After all these checks, we can now plant in this spot by modifying the flowerbed array (or, more simply
    storing a prev variable to store what we intended to do with the last spot). On the next iteration, we
    will make all these checks and the fact that we've modified the flowerbed will suitably determine whether or not
    we can plant in subsequent spots. If any of the checks fail, we just continue with the iteration until we find
    a good spot. We'll also keep count of the spots we've planted in and compare it to the value n we're given,
    and then finally return the boolean response.


Approach2:
----------
    For this solution, we'll take a more "oblivious" approach. We'll just iterate, and if at any point the last
    spot we checked was free, and the current spot is free, we'll plant in the current spot we're in, and increase a
    count assuming the spot is ok to plant in (disregarding the next spot).

    The issue here is that: "what if there's a plant in the next spot?". How we handle this is to compare the
    status of the current spot with the previous spot. If there ever is, then we'll know we caused it to happen
    with a previous "oblivious" plant. We simply decrease the count, as one of the previous plants are now invalid.
    We'll then update our 'prev' variable as normal with the state of the current spot, ready for comparing in the
    next iteration. 
"""

from typing import List

class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        for i in range(len(flowerbed)):
            if (
                (flowerbed[i] == 0) and 
                (prev == 0) and
                (i+1==len(flowerbed) or flowerbed[i+1] == 0)
            ):
                prev = 1
                n -= 1
            else:
                prev = flowerbed[i]
        return n <= 0

    def canPlaceFlowers2(self, flowerbed: List[int], n: int) -> bool:
        prev, count = 0, 0

        for spot in flowerbed:
            if spot == 0:
                if prev == 0: # if there was space before we carry out...
                    count += 1 # oblivious planting
                    prev = 1 # now this spot will be marked as occupied for the checks of the next iteration
                else:
                    prev = 0 # the last spot was a 1, and this one is a 0. Move along..
            elif spot == 1:
                if prev == 1: # we planted wrongly earlier!
                    count -= 1
                prev = 1

        return count >= n # Fingers crossed we could plant enough 🤞


soln = Solution()
print(soln.canPlaceFlowers2([1, 0, 0, 0, 1], 1))
print(soln.canPlaceFlowers2([1, 0, 0, 0, 1], 2))
print(soln.canPlaceFlowers2([1, 0, 0, 0, 0, 1], 2))
print(soln.canPlaceFlowers2([0, 0], 1))
print(soln.canPlaceFlowers2([0, 0], 2))
