"""
Problem Statement:
------------------
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original string by
    deleting some (can be none) of the characters without disturbing the relative positions
    of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Examples:
---------
    Example 1:
        Input: s = "abc", t = "ahbgdc"
        Output: true

    Example 2:
        Input: s = "axc", t = "ahbgdc"
        Output: false


Constraints:
------------
    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.


Follow up:
----------
    Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to
    check one by one to see if t has its subsequence. In this scenario, how would you change your code?


Approach:
---------
    For this solution, I'll simply iterate over t, and keep a pointer, say i to denote where I am in the
    s string. If I come across the character I'm at in the s string while iterating over t, I'll shift the
    pointer forward, and start looking if I'll encounter that character. When I've found all the characters in
    s, I'll return True immediately and otherwise return False after completely iterating over t without success.


Complexity:
-----------
    Time: O(n)
    Space: O(1)

"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

soln = Solution()
print(soln.isSubsequence('abc', 'ahbgdc'))
print(soln.isSubsequence('axc', 'ahbgdc'))
