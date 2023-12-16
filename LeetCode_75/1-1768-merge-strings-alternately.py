"""
Problem Statement:
------------------
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating
    order, starting with word1. If a string is longer than the other, append the additional letters
    onto the end of the merged string.

    Return the merged string.

Approach:
---------
    For this solution, I'll traverse both strings, with index pointers, up to the point of the shortest
    string. At the end of this, I'll add the remaining letters from the longer string if any.

Complexity:
-----------
    Time: O(m+n) => We traverse the strings only once
    Space: O(1)
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l1, l2 = len(word1), len(word2)
        for i in range(l1 if l1 < l2 else l2):
            res += word1[i] + word2[i]
        if i+1 < l1:
            res += word1[i+1:]
        elif i+1 < l2:
            res += word2[i+1:]
        return res

soln = Solution()
print(soln.mergeAlternately('abc', 'pqrst'))