"""
Problem Statement:
------------------
    Given an input string s, reverse the order of the words.

    A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

    Return a string of the words in reverse order concatenated by a single space.

    Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned
    string should only have a single space separating the words. Do not include any extra spaces.


Examples:
----------
    Example 1:
        Input: s = "the sky is blue"
        Output: "blue is sky the"

    Example 2:
        Input: s = "  hello world  "
        Output: "world hello"
        Explanation: Your reversed string should not contain leading or trailing spaces.

    Example 3:
        Input: s = "a good   example"
        Output: "example good a"
        Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Constraints:
------------
    1 <= s.length <= 104
    s contains English letters (upper-case and lower-case), digits, and spaces ' '.
    There is at least one word in s.


Approach1: (sliding window)
----------
    For this solution, we could use a sliding window technique with pointers initially at the end of the string
    one of these pointers would iterate over the array in reverse and continuously, and then the other
    would stop at an index next to the last word we encountered. How we can spot this is to use an
    in_word variable to determine our current state as we iterate.

    How we can turn on this switch is: if we weren't in a word before, and then we just encountered a character, then
    that character must be the end of a word, since we're iterating in reverse. Then we'll move the end pointer to the
    index after this one, to be ready for when we are out of the character zone, and then we push all the characters in
    our window to the resulting string, and then with a space in between.

    How we know we're out of the characters zone is that we would encounter an empty string or the end of the word,
    and then the in_word varible will still be true, from the last iteration.

"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        j = len(s)
        res = ''
        in_word=True
        for i in range(j-1, -1, -1):
            if s[i] == ' ':
                if in_word: # we just left the character zone of a word.
                    res += s[i+1:j] + ' '
                    j = i
                    in_word=False
                else: # we are in an empty space
                    j = i
            else:
                if i == 0:
                    return res + s[:j]
                elif not in_word: # we just entered into the character zone of a word.
                    in_word = True
                    j = i+1

    # pythonic one liner 🔥🔥
    def reverseWords2(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


soln = Solution()
print(soln.reverseWords("the sky is blue"))
print(soln.reverseWords("  hello world  "))
print(soln.reverseWords("a good   example"))