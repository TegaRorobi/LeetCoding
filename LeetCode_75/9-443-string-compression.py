"""
Problem Statement:
------------------
    Given an array of characters chars, compress it using the following algorithm:

    Begin with an empty string s. For each group of consecutive repeating characters in chars:

    If the group's length is 1, append the character to s.
    Otherwise, append the character followed by the group's length.

    The compressed string s should not be returned separately, but instead, be stored in the
    input character array chars. Note that group lengths that are 10 or longer will be split
    into multiple characters in chars.

    After you are done modifying the input array, return the new length of the array.

    You must write an algorithm that uses only constant extra space.


Examples:
---------
    Example 1:
        Input: chars = ["a","a","b","b","c","c","c"]
        Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
        Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

    Example 2:
        Input: chars = ["a"]
        Output: Return 1, and the first character of the input array should be: ["a"]
        Explanation: The only group is "a", which remains uncompressed since it's a single character.

    Example 3:
        Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
        Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".


Constraints:
------------
    1 <= chars.length <= 2000
    chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.


Approach:
---------
    For this solution, I'll iterate over the chars array as usual, but I'll use two variables to keep
    track of my state. 'prev' and 'cnt'. prev would simply store the last character I encountered. cnt
    would store the number of consecutively same characters I have currently seen.

    I'll use a 's' variable to store the compressed string. While iterating, if the character we
    encounter is the same as the previous one, then we'll increase the count, and if the character
    we encounter is not equal to the value in the prev variable, then we'll check if the count is > 1
    and then update s accordingly, and then reset the count (to 1, as we've just encountered a new character)


Complexity:
-----------
    Time: O(2n) => Worst case where the chars array contains only unique characters. We'll traverse once to
                   determine the compressed string, and then once again to modify the chars array with the
                   values in the compreses string in place as the problem says.
    Space: O(1)

"""

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ''
        cnt = 1
        prev = None
        for c in chars:
            if c == prev:
                cnt += 1
            else:
                if cnt > 1: # if the old count is greater than 1, add it and reset the count
                    s += str(cnt)
                    cnt = 1 # the new element we just encountered
                s += c
            prev = c
        if cnt != 1:
            s += str(cnt)

        ls = len(s)
        chars[ls:] = []
        i = 0
        while i < ls:
            chars[i] = s[i]
            i += 1
        return ls


    # truly O(n) solution, also O(1) space
    def compress2(self, chars: List[str]) -> int:
        lc = len(chars)
        ans = 0
        i = 0
        while i < lc:
            char = chars[i]
            count = 0
            while i < lc and chars[i] == char:
                count += 1
                i += 1
            chars[ans] = char
            ans += 1
            if count > 1:
                for num in str(count):
                    chars[ans] = num
                    ans += 1
        # chars[ans:] = [] # optional in the context of the question, getting rid of the extra values
        return ans


soln = Solution()
print(soln.compress2(["a","a","b","b","c","c","c"]))
print(soln.compress2(["a"]))
print(soln.compress2(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
