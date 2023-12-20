"""
Problem Statement:
------------------
    Given a string s, reverse only all the vowels in the string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
    lower and upper cases, more than once.


Examples:
----------
    Example 1:
        Input: s = "hello"
        Output: "holle"

    Example 2:
        Input: s = "leetcode"
        Output: "leotcede"
 

Constraints:
------------
    1 <= s.length <= 3 * 105
    s consists of printable ASCII characters.


Approach1: (sliding window)
----------
    For this solution, we could use a sliding window technique with pointers initially at the beginning and
    the end of the string. For the sliding action, we move the left slider continuously until we zero
    in on a vowel. We can then pause, and then move the right pointer accordingly until we also zero in on
    a vowel. We'll also keep in mind that these pointers shouldn't pass each other.

    When both pointers are on vowels, we swap them, and immediately shift both pointers in (to avoid reswapping)
    and then continue the process, calibrating the left and right pointers, until we find another sweet
    spot to make another swap,... until the pointers cross each other and we terminate the loop.


Approach2:
----------
    We could also gather all the vowels in the input string into another string, say vowels for instance,
    and while doing this, we store the position of these vowels, as a serial array of numbers. We'll then
    reverse the 'vowels' string, and begin placing the reverse vowels in the saved indices. We may need to
    convert the input string to a list to achieve the item assignment and then join it and return the result.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = 'aeiouAEIOU'
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)


    def reverseVowels2(self, s: str) -> str:
        s = list(s)
        vowels, idx, ls = "", [], len(s)
        i = 0
        while i < ls:
            if s[i] in 'AaEeIiOoUu':
                idx.append(i)
                vowels += s[i]
            i += 1
        for vowel, indx in zip(vowels[::-1], idx):
            s[indx] = vowel
        return ''.join(s)


soln = Solution()
print(soln.reverseVowels('hello'))
print(soln.reverseVowels('LeetCode'))
print(soln.reverseVowels('Origami'))