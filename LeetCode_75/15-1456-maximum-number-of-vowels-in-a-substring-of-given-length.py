"""
Problem Statement:
------------------
    Given a string s and an integer k, return the maximum number of vowel letters
    in any substring of s with length k.

    Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


Examples:
---------
    Example 1:
        Input: s = "abciiidef", k = 3
        Output: 3
        Explanation: The substring "iii" contains 3 vowel letters.

    Example 2:
        Input: s = "aeiou", k = 2
        Output: 2
        Explanation: Any substring of length 2 contains 2 vowels.

    Example 3:
        Input: s = "leetcode", k = 3
        Output: 2
        Explanation: "lee", "eet" and "ode" contain 2 vowels.


Constraints:
------------
    1 <= s.length <= 105
    s consists of lowercase English letters.
    1 <= k <= s.length


Approach:
---------
    For this solution, I'll implement a sliding window approach. I'll iterate over the inpur array,
    and initially evaluate the number of vowels in the first k elements. With this value obtained, I'll
    iterate over the rest elements and then add them to my window one by one, and remove the last element
    from the window. If the element being removed is a vowel, the count is reduced. If the element being
    added is a vowel, the count is increased. These two conditions are independent of each other.

    I'll use a separate variable to keep track of the maximum count so far, and at the end,
    simply return that value.


Complexity:
-----------
    Time: O(n)
    Space: O(1)

"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        curr = 0
        for c in s[:k]:
            if c in vowels:
                curr += 1
        maxc = curr

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                curr -= 1
            if s[i] in vowels:
                curr += 1
                maxc = curr if curr > maxc else maxc

        return maxc


soln = Solution()
print(soln.maxVowels('abciiidef', k=3))
print(soln.maxVowels('aeiou', k=2))
print(soln.maxVowels('leetcode', k=3))